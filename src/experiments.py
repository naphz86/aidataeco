"""Experimente E1-E5 der Arbeit (Abschnitt „Experimentelle Auswertung“).

Aufruf aus dem Projektwurzelverzeichnis (nach ``pip install -e ".[dev]"``)::

    python src/kapitel_experimente.py            # schreibt nach src/results/
    python src/kapitel_experimente.py <ordner>   # anderes Ausgabeverzeichnis

Geschrieben werden ``e1_fallstudie.json`` ... ``e5_reproduzierbarkeit.json`` und
``zusammenfassung.json``. Die Abbildungen erzeugt anschließend ``src/plots.py``.
"""

from __future__ import annotations

import itertools
import random
import resource
import statistics
import sys
import time
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Optional, Sequence

from aidataeco.casestudy import MarginCase, margin_case
from aidataeco.evaluation import Cause, explained_share
from aidataeco.experiment import ExperimentRecord, run_experiment
from aidataeco.integration import IntegrationOption, select_integrations

DEFAULT_OUT = Path(__file__).resolve().parent / "results"

BUDGETS = [None, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
E2_REPEATS = 5
E3_SIZES = [4, 5, 6, 7, 8, 9, 10]
E3_SEEDS = [1, 2, 3]
E5_REPEATS = 5

CASE_OPTIONS = (
    IntegrationOption("Frachtzuordnung", 230, 80),
    IntegrationOption("Produktgruppe", 150, 60, ("Stammdaten-Mapping",)),
    IntegrationOption("Stammdaten-Mapping", 0, 40),
    IntegrationOption("Rabatt-Feindaten", 0, 30),
)


def _options_json(options: Sequence[IntegrationOption]) -> List[dict]:
    return [{"name": o.name, "gain": o.gain, "cost": o.cost, "requires": list(o.requires)}
            for o in options]


def brute_force(options: Sequence[IntegrationOption], budget: Optional[int]):
    """Exakte Referenz: Aufzählung aller 2^n Teilmengen."""
    best_net, best_set = 0, ()
    for mask in range(1 << len(options)):
        chosen = [o for i, o in enumerate(options) if mask >> i & 1]
        names = {o.name for o in chosen}
        cost = sum(o.cost for o in chosen)
        if budget is not None and cost > budget:
            continue
        if any(r not in names for o in chosen for r in o.requires):
            continue
        net = sum(o.gain - o.cost for o in chosen)
        if net > best_net:
            best_net, best_set = net, tuple(sorted(names))
    return best_net, best_set


def random_instance(n: int, seed: int):
    rng = random.Random(seed)
    options: List[IntegrationOption] = []
    for i in range(n):
        requires = ()
        if i > 0 and rng.random() < 0.2:
            requires = (f"o{rng.randrange(i)}",)
        options.append(IntegrationOption(f"o{i}", rng.randint(0, 100), rng.randint(1, 60), requires))
    return options, int(0.4 * sum(o.cost for o in options))


def _median_time(function, repeats: int):
    times, result = [], None
    for _ in range(repeats):
        start = time.perf_counter()
        result = function()
        times.append(time.perf_counter() - start)
    return statistics.median(times), result


# ---------------------------------------------------------------- E1 bis E5
def e1(case: MarginCase) -> ExperimentRecord:
    def run(config, inputs):
        return {
            "abweichung": str(case.gap),
            "db2_erwartet": str(case.expected_db2),
            "db2_tatsaechlich": str(case.actual_db2),
            "anteile": {c.name: str(c.amount / case.gap) for c in case.causes},
            "erklaerter_anteil": str(case.explained_share),
        }
    return run_experiment("e1_fallstudie", {}, {}, run)


def e2() -> ExperimentRecord:
    def run(config, inputs):
        rows = []
        for budget in BUDGETS:
            seconds, plan = _median_time(lambda: select_integrations(CASE_OPTIONS, budget), E2_REPEATS)
            ref_net, ref_set = brute_force(CASE_OPTIONS, budget)
            rows.append({
                "budget": budget, "gewaehlt": sorted(plan.selected), "kosten": plan.total_cost,
                "nettonutzen": plan.net_value, "aufrufe": plan.calls,
                "referenz_menge": list(ref_set), "referenz_netto": ref_net,
                "uebereinstimmung_netto": plan.net_value == ref_net, "zeit_median_s": seconds,
            })
        return {"zeilen": rows, "alle_netto_gleich": all(r["uebereinstimmung_netto"] for r in rows)}
    return run_experiment("e2_budgetsweep", {"budgets": BUDGETS, "repeats": E2_REPEATS},
                          {"optionen": _options_json(CASE_OPTIONS)}, run)


def e3() -> ExperimentRecord:
    def run(config, inputs):
        rows = []
        for n in E3_SIZES:
            instances = []
            for seed in E3_SEEDS:
                options, budget = random_instance(n, seed)
                start = time.perf_counter()
                plan = select_integrations(options, budget)
                sat_s = time.perf_counter() - start
                start = time.perf_counter()
                ref_net, _ = brute_force(options, budget)
                bf_s = time.perf_counter() - start
                instances.append({"seed": seed, "netto_sat": plan.net_value, "netto_ref": ref_net,
                                  "gleich": plan.net_value == ref_net, "aufrufe": plan.calls,
                                  "sat_s": sat_s, "bf_s": bf_s})
            rows.append({
                "n": n, "instanzen": instances,
                "sat_median_s": statistics.median(i["sat_s"] for i in instances),
                "bf_median_s": statistics.median(i["bf_s"] for i in instances),
                "aufrufe_median": int(statistics.median(i["aufrufe"] for i in instances)),
                "alle_gleich": all(i["gleich"] for i in instances),
            })
        return {"zeilen": rows}
    return run_experiment("e3_skalierung", {"groessen": E3_SIZES, "seeds": E3_SEEDS}, {}, run)


def e4(case: MarginCase) -> ExperimentRecord:
    def run(config, inputs):
        explained = {"Rabatte": Fraction(1)}
        stages = [("Ausgangslage (nur Rabatte)", dict(explained)),
                  ("+ Frachtzuordnung", {**explained, "Expressfracht": Fraction(1)}),
                  ("+ Produktgruppe", {**explained, "Expressfracht": Fraction(1), "Produktmix": Fraction(1)})]
        out = []
        for label, visible in stages:
            causes = tuple(Cause(c.name, c.amount, visible.get(c.name, Fraction(0))) for c in case.causes)
            share = explained_share(causes, case.gap)
            out.append({"stufe": label, "erklaert": str(share),
                        "erklaert_prozent": round(float(share) * 100, 2),
                        "unerklaert_T_eur": str(case.gap * (1 - share))})
        return {"stufen": out}
    return run_experiment("e4_erklaerter_anteil", {}, {}, run)


def e5(case: MarginCase) -> ExperimentRecord:
    def run(config, inputs):
        records = [e1(case) for _ in range(E5_REPEATS)]
        return {"ergebnisse_gleich": len({r.to_json() for r in records}) == 1,
                "fingerprints_gleich": len({r.fingerprint() for r in records}) == 1,
                "fingerprint": records[0].fingerprint()}
    return run_experiment("e5_reproduzierbarkeit", {"wiederholungen": E5_REPEATS}, {}, run)


def main(out: Path) -> Dict[str, Path]:
    start = time.perf_counter()
    case = margin_case()
    paths = {r.name: r.write(out) for r in (e1(case), e2(), e3(), e4(case), e5(case))}
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024  # Linux: KiB -> MiB
    from aidataeco.experiment import canonical_json
    summary = out / "zusammenfassung.json"
    summary.write_text(canonical_json({"gesamtzeit_s": time.perf_counter() - start,
                                       "peak_rss_MiB": peak}) + "\n", encoding="utf-8")
    paths["zusammenfassung"] = summary
    return paths


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    for name, path in main(target).items():
        print(f"{name}: {path}")
