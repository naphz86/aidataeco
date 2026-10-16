# Wann ist das Datennetz gut genug für KI?

**Ein ökonomischer und formaler Ansatz zur verantwortbaren Nutzung von KI in Unternehmen**

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-72%20passed-4c1)](tests/)
[![Test Coverage](https://img.shields.io/badge/Test%20Coverage-100%25-brightgreen)](doc/coverage/index.html)
[![scicov](https://img.shields.io/badge/scicov-10-ff69b4)](doc/coverage/index.html)

Dieses Repository enthält eine wissenschaftliche Arbeit über die Frage, wann das Datennetz eines Unternehmens für eine bestimmte KI-Anwendung gut genug ist. Im Mittelpunkt steht nicht die Suche nach fehlerfreien Daten oder einem perfekten Modell. Entscheidend ist, ob die verbleibende Unsicherheit für den jeweiligen Zweck und die möglichen Folgen einer Entscheidung vertretbar ist.

Die Arbeit verbindet ein formales Modell von Datennetzen und Data Products mit einer wirtschaftlichen Betrachtung von Fehlerbudgets, einer Fallstudie zur Margenanalyse und einem schrittweisen Vorgehen für Organisationen. KI wird dabei zunächst als Hinweis- und Gegenprüfungswerkzeug verstanden. Abweichungen zwischen KI-Antwort und Unternehmensanalyse können auf Datenlücken hinweisen, aber auch eine unvollständige interne Analyse sichtbar machen.

> **Leitgedanke:** Nicht nur fragen, ob die KI gut genug ist, sondern ob das Datennetz für diese konkrete Frage gut genug ist.

## Inhaltsverzeichnis

- [Überblick](#überblick)
- [Kernaussagen](#kernaussagen)
- [Inhalt der Arbeit](#inhalt-der-arbeit)
- [Fallstudie: Sinkende Marge](#fallstudie-sinkende-marge)
- [Formales Modell und wirtschaftliche Perspektive](#formales-modell-und-wirtschaftliche-perspektive)
- [Vertrauensstufen](#vertrauensstufen)
- [Data Products und Verantwortlichkeiten](#data-products-und-verantwortlichkeiten)
- [Projektstruktur](#projektstruktur)
- [Voraussetzungen](#voraussetzungen)
- [Python-API](#python-api)
- [Quellcode und Tests](#quellcode-und-tests)
- [Quellen und weiterführende Arbeiten](#quellen-und-weiterführende-arbeiten)
- [Erwerb](#erwerb)

## Überblick

Die Verlässlichkeit einer KI-Antwort entsteht nicht allein durch das KI-Modell. Sie hängt auch davon ab, ob relevante Daten zugänglich, aktuell, fachlich verständlich und miteinander verbunden sind. Wenn zum Beispiel Frachtkosten in einem Logistiksystem liegen, aber keiner Bestellung zugeordnet werden können, kann eine KI eine Margenveränderung nicht vollständig erklären – unabhängig davon, wie gut sie formuliert.

Die Arbeit behandelt die Datenlandschaft als ein **Datennetz**: Datenbestände und Dokumente bilden Knoten; fachliche Beziehungen, Joins und Transformationen bilden Kanten. Ein **Data Product** stellt einen für einen Geschäftsbereich relevanten und wiederverwendbaren Teil dieses Netzes bereit. Es bündelt:

1. **Daten** und ihre Granularität,
2. **Bedeutung** wie Definitionen, Synonyme und fachliche Regeln,
3. **Label** mit Eigentümerschaft, Qualität, Aktualität, Zugriff und Version.

Auf dieser Grundlage wird eine KI-Antwort nach dem Verwendungszweck bewertet. Ein Hinweis für eine fachliche Prüfung darf größere Unsicherheit haben als eine Handlung, die ohne menschliche Kontrolle ausgelöst wird. Die notwendige Qualität ist daher an die **Stakes** – die möglichen wirtschaftlichen und organisatorischen Folgen – und an ein anwendungsbezogenes **Error Budget** gebunden.

## Kernaussagen

- **Fehlerfreiheit ist keine realistische Voraussetzung.** Entscheidend ist, ob der mögliche Fehler für den konkreten Einsatz klein genug ist.
- **Die Frage bestimmt den erforderlichen Reifegrad.** Dasselbe Datennetz kann für eine Trendbeobachtung genügen und für eine Kunden- oder Preisentscheidung unzureichend sein.
- **Das Datennetz ist mehr als eine Sammlung von Tabellen.** Beziehungen zwischen Quellen, Definitionen, Zugriff und Aktualität sind ebenso wichtig wie die Daten selbst.
- **Ein plausibler Text ist kein Korrektheitsnachweis.** Antworten sollten Definition, Quelle und Datenstichtag erkennen lassen und gegen eine belastbare Referenz geprüft werden.
- **KI kann schon vor vollständiger Datenreife nützlich sein.** Als Hinweis oder Gegenprüfung unterstützt sie die Analyse, ohne selbst als alleinige Entscheidungsinstanz zu gelten.
- **Abweichungen sind Diagnoseanlässe.** Ursachen können fehlende Daten, fehlende Attribute, Definitionskonflikte, veraltete Daten oder Fehler in der eigenen Analyse sein.
- **Data Products ermöglichen Wiederverwendung.** Gemeinsame Daten und Definitionen können mehrere Anwendungen versorgen, statt in jedem Projekt neu aufgebaut zu werden.
- **Verantwortung braucht benannte Personen.** Bedeutung, Lieferung und Freigabe der jeweiligen Anwendung sind getrennte Verantwortungsbereiche.
- **Autonomie wird stufenweise aufgebaut.** Automatisierte Handlungen erfordern strengere Qualitätsnachweise, Freigaben und Protokollierung als unverbindliche Hinweise.

## Inhalt der Arbeit

Die LaTeX-Arbeit entwickelt das Konzept in folgender Reihenfolge:

1. **Ausgangslage: KI-Ambition und Datenreife** – ordnet den im Webinar beschriebenen Abstand zwischen KI-Einsatz und Datenreife ein.
2. **Fallstudie: Warum sinkt die Marge?** – zeigt an einem konkreten Beispiel, wie eine teilweise richtige Erklärung eine falsche Maßnahme nahelegen kann.
3. **Formales Modell des Datennetzes** – beschreibt Datenbestände, Beziehungen, Einflussgrößen, Data Products und Provenance.
4. **Fehlerzusammensetzung und „gut genug“** – führt Error Budget, Stakes und anwendungsbezogene Anforderungen ein.
5. **Abweichungen als Chance** – betrachtet Unterschiede zwischen KI-Antwort und interner Analyse als diagnostisches Signal und entwickelt einen Lernkreislauf.
6. **Das Data Product als gemeinsame Grundlage** – konkretisiert Daten, Granularität, Meaning und Label anhand eines Beispiels.
7. **Verantwortung und Freigabe** – erläutert Data Owner, Data Product Owner und Use-Case Owner.
8. **Schrittweises Vorgehen in der Praxis** – beschreibt den Aufbau und unterscheidet Schwerpunkte für Mittelstand und Großunternehmen.
9. **Stolperfallen, Fortschrittsmessung und Checkliste** – gibt Prüffragen und Kennzahlen für die praktische Anwendung.
10. **Experimentelle Auswertung** – prüft die ausführbare Umsetzung an der Fallstudie und an synthetischen Instanzen (Budgetabhängigkeit der Integrationsauswahl, Skalierung, erklärter Anteil, Reproduzierbarkeit) und dokumentiert Hardware, Versuchsaufbau, Ergebnisse und Grenzen.
11. **Diskussion, Ausblick, Schlussfolgerung und Glossar** – ordnet die Befunde ein, nennt offene Forschungsfragen und fasst die Arbeit ausführlich zusammen.
12. **Anhang** – enthält formale Erweiterungen und eine Beweisskizze zur Value of Information (VOI).

Das vollständige Inhaltsverzeichnis steht auch am Anfang des [PDFs](science/aidataeco.pdf).

## Fallstudie: Sinkende Marge

Die illustrative Webinar-Fallstudie betrachtet einen Maschinenbauzulieferer. Der Umsatz steigt von 10,0 Mio. € auf 11,0 Mio. €, während die Deckungsbeitragsmarge II von 28 % auf 24 % fällt. Die daraus abgeleitete DB-II-Differenz beträgt 440 T€.

| Ursache | Betrag | Anteil an der Differenz | Sichtbar für die KI? |
|---|---:|---:|---|
| Expressfracht nach Lieferengpass | 230 T€ | ca. 52 % | Nein – im Logistiksystem nicht mit den Aufträgen verbunden |
| Ungünstiger Produktmix | 150 T€ | ca. 34 % | Nein – Produktgruppe im zugänglichen Datennetz nicht vorhanden |
| Gestiegene Rabatte | 60 T€ | ca. 14 % | Ja – in den Vertriebsdaten sichtbar |
| **Gesamt** | **440 T€** | **100 %** | |

Die KI erkennt den Rabattanstieg und empfiehlt unter anderem, Konditionen mit Großkunden neu zu verhandeln. Der betroffene Kunde Nord erzielt 2,0 Mio. € Umsatz; die Expresslieferungen waren nicht durch ihn verursacht. Ohne Prüfung hätte eine plausible, aber unvollständige Erklärung damit eine unverhältnismäßige Maßnahme nahelegen können.

Der Fall verdeutlicht den Unterschied zwischen **Hinweis** und **Gesamterklärung**: Der Rabattanstieg war ein wahrer Hinweis, erklärte aber nur einen kleineren Teil der Differenz. Für eine allgemeine Auffälligkeitsanalyse kann das genügen, für eine konkrete Kundenmaßnahme nicht unbedingt.

## Formales Modell und wirtschaftliche Perspektive

### Datennetz

Die Arbeit modelliert ein Datennetz als gerichteten Multigraphen $G=(V,E)$:

- Knoten \(V\) repräsentieren Tabellen, Datensätze oder Dokumente mit Attributen, Qualitätsmerkmalen und Aktualität.
- Kanten \(E\) repräsentieren Joins, Mappings oder Transformationen, die Daten fachlich miteinander verbinden.
- Für eine Frage \(q\) benennt ein Domänenexperte die wesentlichen Einflussgrößen \(S_q\). Nur ein Teil davon kann im tatsächlich zugänglichen Netz beobachtbar sein.

Eine KI-Anwendung erzeugt auf Basis einer Frage und des zugänglichen Netzes eine Antwort. Die Arbeit unterscheidet dabei die tatsächlich verfügbare Datengrundlage von einer gedachten vollständigen Referenz. Das ist ein Modell zur strukturierten Diskussion von Abdeckung und Fehlerquellen, kein Beweis, dass sich jede reale Geschäftswahrheit vollständig erfassen lässt.

### Fehler und Error Budget

Die konzeptionelle Fehlerzerlegung unterscheidet:

- **fehlende Einflussgrößen** – wesentliche Treiber fehlen im genutzten Datennetz;
- **Definitionsabweichungen** – gleich benannte Kennzahlen haben verschiedene Bedeutungen;
- **zufällige Fehler** – beispielsweise durch Datenqualität oder Aktualisierungsverzögerungen.

Ein Error Budget beschreibt, welcher erwartete Verlust für eine konkrete Entscheidung noch akzeptabel ist. Die zentrale Bedingung lautet:

$$
\mathbb{E}[L(\hat y,y^*)] \leq \varepsilon W,
$$

wobei \(L\) den Verlust aus der Antwortabweichung, \(W\) die Stakes und \(\varepsilon\) den für den Anwendungsfall festgelegten Anteil bezeichnet. Die konkrete Verlustfunktion und Schwelle müssen fachlich bestimmt werden; die Formel setzt **keinen** universellen Schwellenwert fest.

### Abweichungen und Value of Information

Eine Abweichung zwischen der KI-Antwort und einer internen Analyse ist nicht automatisch ein Modellfehler. Sie kann auf fehlende Quellen oder Attribute, unklare Definitionen, veraltete Daten oder eine unvollständige eigene Analyse hinweisen. Die Arbeit beschreibt, wie dieser Befund in einen Kreislauf aus Prüfung, Verbesserung und erneuter Messung einfließen kann.

Die **Value of Information (VOI)** betrachtet, ob der erwartete zusätzliche Nutzen einer Datenintegration deren Kosten rechtfertigt. Das ist als Entscheidungsrahmen gedacht; eine belastbare Anwendung benötigt konkrete Annahmen zu Kosten, Nutzen, Unsicherheit und möglichen Handlungsalternativen.

## Vertrauensstufen

Die Arbeit unterscheidet vier stufenweise Nutzungsarten:

| Stufe | Rolle der KI | Typische Kontrolle |
|---|---|---|
| 1 | **Hinweis** | Eine Person prüft die angezeigte Auffälligkeit eigenständig. |
| 2 | **Gegenprüfung** | KI-Ergebnis und interne Analyse werden verglichen; Unterschiede werden untersucht. |
| 3 | **Vorbereitung von Entscheidungen** | Qualität, Quelle, Definition und Datenstichtag sind nachvollziehbar; ein Mensch entscheidet. |
| 4 | **Automatisierte Handlung** | Ausdrückliche Freigabe, hohe Zuverlässigkeit, Protokollierung und Eingriffsmöglichkeit sind erforderlich. |

Die Stufen sind keine automatisch verdienten Zertifizierungen und kein allgemeines Gütesiegel für ein Modell oder Data Product. Die Freigabe wird pro Anwendung anhand von Stakes, Testfällen, Datenlage und Aufsicht entschieden.

## Data Products und Verantwortlichkeiten

### Bestandteile eines Data Products

Das Beispiel „Sales Result 360“ bündelt die Datengrundlage für Fragen zu Umsatz, Marge und deren Einflussfaktoren:

1. **Daten und Granularität:** etwa eine Zeile je Auftragsposition, ergänzt um Kunde, Produkt, Zeit, Vertrieb, Lieferung, Fracht, Plan und Vorjahr.
2. **Meaning:** Kennzahlendefinitionen wie DB I und DB II, Synonyme wie „Marge“, Zurechnungsregeln für Fracht und Vergleichszeiträume.
3. **Label:** fachlicher Kontakt, Qualitäts- und Aktualitätsangaben, Zugriffsrechte, Version und bekannte Einschränkungen.

Eine festgelegte semantische Regel ersetzt nicht die technische Verknüpfung zwischen Quellsystemen. Für eine belastbare Margenanalyse braucht es sowohl verständliche Definitionen als auch passende, überprüfbare Datenbeziehungen.

### Drei Verantwortlichkeiten vor dem Go-live

| Rolle | Hauptverantwortung |
|---|---|
| **Data Owner** | Definiert fachliche Bedeutung, Kennzahlen, Ausnahmen und Synonyme. |
| **Data Product Owner** | Verantwortet Lieferung, Vollständigkeit, Aktualität, Prüfung und Berechtigungen des Data Products. |
| **Use-Case Owner** | Genehmigt die Anwendung, verantwortet Testfragen und Error Budget und legt fest, wann ein Mensch entscheidet. |

In einem kleineren Unternehmen kann eine Person mehrere Rollen ausüben. Die Entscheidungen und Zuständigkeiten sollten trotzdem explizit dokumentiert sein. Wenn nicht klar ist, wer Definition, Lieferung oder Freigabe verantwortet, fehlt eine wichtige Grundlage für den Go-live.

## Projektstruktur

```text
aidataeco/
├── README.md
├── LICENSE
├── pyproject.toml
├── src/
│   ├── experiments.py   # Experimente E1-E5
│   ├── plots.py                 # Abbildungen aus den JSON-Protokollen
│   └── results/                 # JSON-Protokolle der Experimente
│       └── plots/               # erzeugte Abbildungen (PDF)
├── tests/
└── science/
    ├── aidataeco.tex
    ├── aidataeco.pdf
    ├── aidataeco.synctex.gz
    └── abb_*.pdf                # Kopien der Abbildungen für die TeX-Arbeit
```

Im Arbeitsverzeichnis können zusätzlich lokale LaTeX-Hilfsdateien wie `.aux`, `.log`, `.toc`, `.out`, `.fls` und `.fdb_latexmk` entstehen. Sie sind Build-Artefakte und keine eigenständigen Quellen der Arbeit.

| Datei | Zweck |
|---|---|
| [`science/aidataeco.tex`](science/aidataeco.tex) | Maßgebliche editierbare Quelle der deutschen Arbeit. |
| [`science/aidataeco.pdf`](science/aidataeco.pdf) | Daraus erzeugte Lesefassung; nach Änderungen an der TeX-Quelle neu bauen. |
| [`science/aidataeco.synctex.gz`](science/aidataeco.synctex.gz) | SyncTeX-Zuordnung zwischen PDF und TeX-Quelle für unterstützte Editoren. |
| [`src/`](src) | Python-Bausteine zur Arbeit (siehe [Software und Tests](#software-und-tests)). |
| [`tests/`](tests) | Automatisierte Tests mit `pytest`. |
| [`src/results/`](src/results) | JSON-Protokolle der Experimente (mit Fingerabdruck) und Plots. |
| [`pyproject.toml`](pyproject.toml) | Paket-, Abhängigkeits-, pytest- und Coverage-Konfiguration. |
| [`LICENSE`](LICENSE) | Nutzungsbedingungen für die Inhalte dieses Repositories. |
| [`.gitignore`](.gitignore) | Ignorierte lokale Umgebungs- und Build-Dateien. |

Die englische Konzeptdatei, auf der die inhaltliche Ausarbeitung beruht, ist **nicht** Teil dieses Repositorys. Die Arbeit und dieses Repository enthalten daher keine automatisch synchronisierte Übersetzung.

## Voraussetzungen

Für das Erstellen der PDF-Datei benötigt man:

- eine TeX-Distribution, beispielsweise [MiKTeX](https://miktex.org/) unter Windows oder [TeX Live](https://www.tug.org/texlive/) unter Linux/macOS;
- `latexmk`;
- den für das Dokument benötigten LaTeX-Paketbestand. Verwendet werden unter anderem `babel`, `lmodern`, `amsmath`, `amssymb`, `amsthm`, `geometry`, `graphicx`, `hyperref`, `booktabs`, `listings`, `xcolor`, `enumitem` und `microtype`.

Die Arbeit ist UTF-8-kodiert und mit `pdflatex`/`latexmk` aufgebaut. Für den Python-Code wird Python ab 3.11 benötigt, siehe [Software und Tests](#software-und-tests); für die PDF ist keine Python-Laufzeit nötig.

## Python-API

Das Paket `aidataeco` bildet die Konzepte der Arbeit als kleine, typisierte Bausteine ab. Installiere das Projekt zunächst wie unter [Software und Tests](#software-und-tests) beschrieben. Die Beispiele importieren direkt aus `aidataeco`; `src` ist nur das Verzeichnis des Quellcodes.

```python
from aidataeco.model import Node, Edge, DataNetwork, Meaning, Label, DataProduct
```

Geldbeträge, Anteile und Wahrscheinlichkeiten werden intern mit `fractions.Fraction` exakt gerechnet. Ein `float` wie `0.1` wird über seine Dezimaldarstellung als `1/10` übernommen. Nicht belegte Werte bleiben `None`; fehlende Quellen, Provenance oder Verantwortliche werden nicht als Erfolg interpretiert. Ungültige Eingaben führen in der Regel zu `ValueError`.

### Datennetz und Data Product

`Node` beschreibt einen Datenbestand, `Edge` eine fachliche Verknüpfung oder Transformation. `DataNetwork` prüft eindeutige Knotennamen und gültige Kanten. `DataProduct` bündelt ein Teilnetz, seine Bedeutung und sein Verantwortungs- und Qualitätslabel.

```python
from datetime import date
from fractions import Fraction

from aidataeco.model import DataNetwork, DataProduct, Edge, Label, Meaning, Node

edges = (
  Edge("ERP", "Auftragsposition", "Join über Auftrags-ID"),
  Edge("Auftragsposition", "Produktstamm", "Join über Produkt-ID"),
)
network = DataNetwork(
  nodes=(
    Node("ERP", frozenset({"Umsatz", "Rabatt"}), Fraction(98, 100), date(2026, 9, 30)),
    Node("Auftragsposition", frozenset({"Auftrags-ID", "Produkt-ID"})),
    Node("Produktstamm", frozenset({"Produktgruppe"})),
    Node("Logistik", frozenset({"Expressfracht"})),
  ),
  edges=edges,
)
product = DataProduct(
  name="Sales Result 360",
  network=network,
  node_names=frozenset({"ERP", "Auftragsposition", "Produktstamm"}),
  edges=edges,
  meaning=Meaning(
    definitions={"DB II": "Umsatz abzüglich variabler Kosten"},
    synonyms={"Marge": "DB II"},
    rules=("Fracht wird der verursachenden Auftragsposition zugeordnet",),
  ),
  label=Label("Controlling", "3.0", frequency_days=1, quality=Fraction(98, 100)),
)

print(product.meaning.resolve("Marge"))
print(product.is_closed([("ERP", "Produktstamm")]))  # True: Join-Pfad ist vorhanden
print(product.missing_links([("Auftragsposition", "Logistik")]))
# (("Auftragsposition", "Logistik"),): Die Frachtquelle ist noch nicht verbunden.
```

`Provenance` dokumentiert Quelle, Datenstichtag und verwendete Definitionen. `Answer` verbindet diese Provenance mit einem Ergebniswert. `None` bei `Answer.value` steht für eine unbeantwortete Frage, nicht für den Zahlenwert null.

```python
from datetime import date
from fractions import Fraction

from aidataeco.model import Answer, Provenance

answer = Answer(
  Fraction(24),
  Provenance(
    sources=(("Sales Result 360", "3.0"),),
    cutoff=date(2026, 9, 30),
    rules=("DB II = Umsatz abzüglich variable Kosten",),
  ),
)
```

### Error Budget

`ErrorBudget` bildet die Gut-genug-Bedingung `erwarteter Verlust <= epsilon * Stakes` ab. Die Schwelle wird pro Einsatz festgelegt; das Modul setzt keinen universellen Grenzwert.

```python
from fractions import Fraction

from aidataeco.errorbudget import ErrorBudget, good_enough_linear

budget = ErrorBudget(stakes=100_000, epsilon=Fraction(1, 100))
print(budget.limit)  # 1000
print(good_enough_linear(cost_per_unit=250, expected_abs_error=3, budget=budget))
# True: 250 * 3 = 750 liegt innerhalb des Budgets von 1000.
```

Für eine explizite Fehlerzerlegung stehen `ErrorDecomposition` mit `total` und `expected`, `missing_bias` für nicht beobachtete Einflussgrößen sowie `lipschitz_bound` für eine Abstandsschranke zur Verfügung.

### Antworten evaluieren

`ReferenceCase` beschreibt Frage, Referenzwert, Toleranz und optionales Gewicht. `evaluate` liefert Bestehensquote, Provenance-Abdeckung und Zahl unbeantworteter Fragen getrennt zurück; diese Kennzahlen werden bewusst nicht zu einer Gesamtnote verrechnet.

```python
from datetime import date
from fractions import Fraction

from aidataeco.evaluation import ReferenceCase, evaluate
from aidataeco.model import Answer, Provenance

cases = [
  ReferenceCase("DB-II-Marge Q3", 24, Fraction(1, 2), weight=3),
  ReferenceCase("Rabattquote Q3", 10, 1, weight=1),
]
provenance = Provenance(
  sources=(("Sales Result 360", "3.0"),),
  cutoff=date(2026, 9, 30),
  rules=("DB II = Umsatz abzüglich variable Kosten",),
)
answers = [Answer(Fraction(47, 2), provenance), Answer(None)]
result = evaluate(cases, answers)

print(result.pass_rate)             # 3/4
print(result.provenance_coverage)    # 1/2
print(result.unanswered)            # 1
```

Weitere Kennzahlen sind `explained_share` für den erklärten Anteil eines Effekts, `attribute_completeness` für fehlende Attribute und `is_fresh` für die Aktualität eines Datenbestands. Unbekannte Aktualität zählt nicht als aktuell.

### Abweichungen diagnostizieren

Die Diagnosefunktionen aktualisieren Hypothesen über mögliche Ursachen einer Abweichung. Bayes-Rechnungen bleiben exakt; Nutzen und Integrationskosten können anschließend mit der VOI-Bedingung verglichen werden.

```python
from fractions import Fraction

from aidataeco.diagnosis import bayes_update, expected_gain, integration_rational

posterior = bayes_update(
  {"Quelle fehlt": Fraction(1, 2), "Analyse unvollständig": Fraction(1, 2)},
  {"Quelle fehlt": Fraction(3, 4), "Analyse unvollständig": Fraction(1, 4)},
)
gain = expected_gain(posterior, {"Quelle fehlt": 3_000, "Analyse unvollständig": 0})
print(posterior)                    # Quelle fehlt: 3/4, Analyse unvollständig: 1/4
print(gain)                         # 2250
print(integration_rational(gain, 2_000))  # True: erwarteter Zusatznutzen deckt die Kosten.
```

`DeviationCause` klassifiziert Befunde wie fehlende Quelle, fehlendes Attribut oder veraltete Daten und stellt über `response` eine passende Reaktion bereit. `Deviation` und `processed_deviations` erfassen, ob ein Befund dokumentiert bearbeitet wurde.

### Governance und Freigabe

`Accountabilities` hält Data Owner, Data Product Owner und Use-Case Owner fest. `release_blockers` prüft die Nachweise abhängig von der gewünschten `ReliabilityLevel`; eine leere Liste bedeutet nur, dass nach dem Modell kein Hindernis fehlt, nicht, dass eine formelle oder regulatorische Freigabe erteilt wurde.

```python
from aidataeco.governance import (
  Accountabilities, Evidence, ReliabilityLevel, release_blockers,
)

owners = Accountabilities("Leitung Controlling", "Datenteam", "Fachbereich")
evidence = Evidence(
  kpis_defined=True,
  provenance_available=True,
  quality_measurable=True,
  error_budget_met=True,
  human_decides=True,
)
print(release_blockers(ReliabilityLevel.DECISION_PREPARATION, owners, evidence))
# []
```

Für `AUTOMATED_ACTION` sind zusätzlich ausdrückliche Freigabe, Protokollierung und ein Eingriffspfad erforderlich. Fehlende Nachweise bleiben standardmäßig `False`.

### Datenintegrationen auswählen

`select_integrations` optimiert erwarteten Zusatznutzen abzüglich Kosten und berücksichtigt Budget sowie Abhängigkeiten. Das Standard-Backend ist `DpllBackend`; für Vergleichs- und Integrationstests kann ein `SatBackend` explizit übergeben werden.

```python
from aidataeco.integration import IntegrationOption, select_integrations

options = [
  IntegrationOption("Fracht", gain=230, cost=40, requires=("Join",)),
  IntegrationOption("Join", gain=0, cost=20),
  IntegrationOption("Produktgruppe", gain=150, cost=60),
  IntegrationOption("Teuer", gain=50, cost=80),
]
plan = select_integrations(options, budget=70)
print(plan.selected)   # ("Fracht", "Join")
print(plan.net_value) # 170
print(plan.total_cost)  # 60
```

Nutzen, Kosten und Budget müssen nichtnegative ganze Zahlen in derselben Einheit sein, beispielsweise T€. Eine Option mit `requires=("Join",)` wird nur ausgewählt, wenn auch `Join` ausgewählt werden kann. Ungültige Namen oder Abhängigkeiten führen zu `ValueError`.

### Fallstudie und reproduzierbare Protokolle

`margin_case()` liefert die illustrative Margenfallstudie aus der Arbeit. Die Werte sind Angaben des Beispiels, keine unabhängig erhobenen Unternehmensdaten.

```python
from aidataeco.casestudy import margin_case

case = margin_case()
print(case.gap)             # 440 (T€)
print(case.explained_share) # 3/22, rund 13,6 Prozent
```

Für eigene Läufe erstellt `run_experiment` ein `ExperimentRecord` mit Eingaben, Konfiguration, Ergebnissen, Versionsangaben und Fingerprint. `write` speichert es als JSON; `Fraction`-Werte werden dabei exakt als Bruchtext serialisiert.

```python
from pathlib import Path

from aidataeco.casestudy import margin_case
from aidataeco.experiment import run_experiment

case = margin_case()
record = run_experiment(
  name="margenfall",
  config={"unit": "T€"},
  inputs={"case": "Q3 2026"},
  function=lambda config, inputs: {
    "gap": case.gap,
    "explained_share": case.explained_share,
  },
)
path = record.write(Path("src/results"))
print(path, record.fingerprint())
```

Die zentralen Klassen und Funktionen sind in den Modulen `model`, `errorbudget`, `diagnosis`, `governance`, `evaluation`, `integration`, `casestudy` und `experiment` definiert. Für vollständige Signaturen und Randfälle sind die Docstrings maßgeblich.

## Quellcode und Tests

`src/` setzt das Dokumentmodell als typisierte, exakt rechnende (`fractions.Fraction`) Python-Bausteine um. Fehlende Evidenz zählt nie als Erfolg: unbekannte Qualität, fehlende Provenance, unbeantwortete Testfragen und fehlende Verantwortliche werden als solche ausgewiesen, ungültige Eingaben lösen `ValueError` aus.

| Modul | Inhalt aus der Arbeit |
|---|---|
| `model` | Datennetz, Data Product, Label, Provenance, Antworten |
| `errorbudget` | Stakes, Error Budget, Fehlerzerlegung, Gut-genug-Bedingung |
| `diagnosis` | Abweichung als Bayes-Indikator, Lern-Loop, VOI-Bedingung, Abweichungsursachen |
| `governance` | Vertrauensstufen, drei Verantwortlichkeiten, Freigabehindernisse |
| `evaluation` | Bestehensquote, erklärter Anteil, Provenance-Abdeckung, Vollständigkeit, Aktualität |
| `integration` | Auswahl von Datenquellen unter Budget und Abhängigkeiten (Erweiterung der VOI-Bedingung) |
| `experiment` | reproduzierbares Protokoll von Eingaben, Konfiguration, Versionen, Resultaten |
| `casestudy` | illustrative Fallstudie zur sinkenden Marge mit den Zahlen der Arbeit |

### Wiederverwendung von subgraph-sat-solver-econ

Entscheider, Schaltkreisbausteine und die Formel der Rechenlücke werden nicht neu geschrieben, sondern aus [`subgraph-sat-solver-econ`](https://github.com/naphz86/subgraph-sat-solver-econ) importiert (`subgraph_sat_solver_econ`): `integration` formuliert nur das Problem und nutzt `Problem`, `maximize` und `DpllBackend`; `evaluation` berechnet den erklärten Anteil mit `computation_gap` und `total_output`. Die Abhängigkeit steht in `pyproject.toml`. Damit das Referenzprojekt unter diesem Namen importierbar ist, braucht es dort die Paketabbildung `package-dir = { subgraph_sat_solver_econ = "src" }` (siehe dessen `pyproject.toml`).

### Experimente ausführen

```bash
python src/experiments.py   # E1-E5, schreibt src/results/*.json
python src/plots.py                 # Abbildungen nach src/results/plots/ und Kopie nach science/
```

Die Kosten und Abhängigkeiten der Integrationsoptionen in den Experimenten sind Annahmen; die Laufzeiten hängen von der Hardware ab (siehe Abschnitt „Experimentelle Auswertung“ der Arbeit).

### Installieren und testen

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install -e ".[dev]"
pytest
```

`pytest` führt alle Tests aus und erzeugt den Coverage-Bericht (Zeilen und Zweige) als HTML unter `doc/coverage/index.html`. Der Bericht ist ein Build-Artefakt und wird bei Bedarf neu erzeugt.

## Quellen und weiterführende Arbeiten

Die Arbeit führt die folgenden Quellen im Literaturverzeichnis:

1. **Michael Sullmann (BE-terna).** Webinar *Data Product and AI in Controlling*, Oktober 2026. Grundlage für die im Text als Webinar-Angaben gekennzeichneten Inhalte und die illustrative Fallstudie.
2. **Stephan Epp.** *Wirtschaftliche Konsequenzen eines effizienten SAT-Solvers*, 12. Oktober 2026. [Repository](https://github.com/naphz86/subgraph-sat-solver-econ).
3. **Stephan Epp.** *Wirtschaftssysteme unter Unsicherheit*, 3. September 2026. [Repository und Wissenschaftsordner](https://github.com/naphets86/odd/tree/main/science/uncrtecos).

Die Arbeiten [2] und [3] sind ergänzende wissenschaftliche Vorarbeiten des Autors. Ihre Nennung bedeutet nicht, dass die vorliegende Arbeit ein SAT-Solver- oder ein Wirtschaftssystem-Simulationspaket enthält.

## Erwerb

Der Preis für diese Software beträgt 4.945.000,00 EUR.

### Zahlungsinformationen

Name: Stephan Epp
IBAN: DE24 5003 1900 0012 5603 20 BIC: BBVADEFFXXX
