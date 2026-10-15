"""Erzeugt die drei Abbildungen der Arbeit aus den JSON-Protokollen der Experimente.

Aufruf aus dem Projektwurzelverzeichnis::

    python src/plots.py                  # liest src/results, schreibt src/results/plots
                                         # und kopiert die PDFs nach science/
    python src/plots.py <results> <ziel> # eigene Ordner (ziel = zusätzlicher Kopierordner)
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RESULTS = Path(__file__).resolve().parent / "results"
DEFAULT_COPY = ROOT / "science"
GAP = 440
FIGURES = ("abb_budget.pdf", "abb_skalierung.pdf", "abb_erklaerter_anteil.pdf")


def _load(results: Path, name: str) -> dict:
    return json.loads((results / f"{name}.json").read_text(encoding="utf-8"))["results"]


def plot_budget(results: Path, out: Path) -> None:
    rows = _load(results, "e2_budgetsweep")["zeilen"]
    finite = [r for r in rows if r["budget"] is not None]
    xs = [r["budget"] for r in finite] + [max(r["budget"] for r in finite) + 20]
    ordered = finite + [r for r in rows if r["budget"] is None]
    net = [r["nettonutzen"] for r in ordered]

    def share(row):
        names = row["gewaehlt"]
        amount = 60 + 230 * ("Frachtzuordnung" in names) + 150 * ("Produktgruppe" in names)
        return 100 * amount / GAP

    fig, (top, bottom) = plt.subplots(2, 1, figsize=(6, 5.5), sharex=True)
    top.step(xs, net, where="post", marker="o")
    top.set_ylabel("Nettonutzen (T€)")
    bottom.step(xs, [share(r) for r in ordered], where="post", marker="o", color="tab:green")
    bottom.set_ylabel("Erklärter Anteil (%)")
    bottom.set_xlabel("Integrationsbudget (T€)")
    bottom.set_xticks(xs)
    bottom.set_xticklabels([str(x) for x in xs[:-1]] + ["∞"])
    for axis in (top, bottom):
        axis.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(out / "abb_budget.pdf")
    plt.close(fig)


def plot_scaling(results: Path, out: Path) -> None:
    rows = _load(results, "e3_skalierung")["zeilen"]
    n = [r["n"] for r in rows]
    fig, (top, bottom) = plt.subplots(1, 2, figsize=(8, 3.5))
    top.semilogy(n, [r["sat_median_s"] * 1000 for r in rows], marker="o", label="Entscheider (Median)")
    top.fill_between(n, [min(i["sat_s"] for i in r["instanzen"]) * 1000 for r in rows],
                     [max(i["sat_s"] for i in r["instanzen"]) * 1000 for r in rows], alpha=0.25)
    top.semilogy(n, [r["bf_median_s"] * 1000 for r in rows], marker="s", label="Aufzählung (Median)")
    top.set_xlabel("Zahl der Optionen $n$")
    top.set_ylabel("Laufzeit (ms)")
    top.legend()
    top.grid(alpha=0.3, which="both")
    bottom.plot(n, [r["aufrufe_median"] for r in rows], marker="o", color="tab:red")
    bottom.set_xlabel("Zahl der Optionen $n$")
    bottom.set_ylabel("Entscheideraufrufe")
    bottom.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(out / "abb_skalierung.pdf")
    plt.close(fig)


def plot_explained(results: Path, out: Path) -> None:
    stages = _load(results, "e4_erklaerter_anteil")["stufen"]
    labels = [s["stufe"] for s in stages]
    explained = [s["erklaert_prozent"] for s in stages]
    fig, axis = plt.subplots(figsize=(6, 3.8))
    axis.bar(labels, explained, label="erklärt", color="tab:green")
    axis.bar(labels, [100 - e for e in explained], bottom=explained, label="unerklärt", color="tab:gray")
    axis.set_ylabel(f"Anteil an der Abweichung von {GAP} T€ (%)")
    axis.legend(loc="lower right")
    plt.setp(axis.get_xticklabels(), rotation=15, ha="right")
    fig.tight_layout()
    fig.savefig(out / "abb_erklaerter_anteil.pdf")
    plt.close(fig)


def main(results: Path, copy_to: Path | None) -> None:
    out = results / "plots"
    out.mkdir(parents=True, exist_ok=True)
    plot_budget(results, out)
    plot_scaling(results, out)
    plot_explained(results, out)
    if copy_to is not None:
        copy_to.mkdir(parents=True, exist_ok=True)
        for name in FIGURES:
            shutil.copy2(out / name, copy_to / name)


if __name__ == "__main__":
    res = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_RESULTS
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_COPY
    main(res, dst)
