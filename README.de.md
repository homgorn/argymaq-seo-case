<!-- Sprache: Deutsch. Die primäre README ist Englisch. -->
<div align="center">

[English](README.md) · [Русский](README.ru.md) · [Español](README.es.md) · **Deutsch** · [Français](README.fr.md) · [中文](README.zh.md) · [日本語](README.ja.md)

</div>

---

# argymaq-seo-case

**Vollständiges SEO-Audit einer kirgisischen Tourismus-Website, aufbereitet als Kundenbericht und Portfolio-Case.**

Live: **https://homgorn.github.io/argymaq-seo-case/**

![Audit](https://img.shields.io/badge/Audit-54%20Probleme-critical) ![Seiten](https://img.shields.io/badge/Seiten-17-success) ![Stack](https://img.shields.io/badge/Astro-5.18-ff5d01) ![Lizenz](https://img.shields.io/badge/Lizenz-MIT-blue)

---

## Worum es geht

Ein vollständiges, reproduzierbares SEO-Audit von **argymaq.kg** — einem Anbieter für Reittouren in Karakol, Kirgistan — in zwei Ergebnissen:

1. **Eine statische Website** (Astro, 17 Seiten), die die Befunde in einfacher Sprache erklärt: mit Diagrammen, Vorher-/Nachher-Vergleichen und einem Stufenplan. Für einen Eigentümer geschrieben, der nicht im SEO arbeitet.
2. **Der vollständige Datensatz** — jede Messung, jedes Skript und jede Quelle, damit die Arbeit überprüfbar bleibt.

Der Fall ist als **Vorher → Nachher** erzählt: was gefunden wurde, was es für den Umsatz bedeutet und was zuerst behoben wird.

### Die Ausgangszahlen

| Kennzahl | Vorher | Quelle |
|---|---|---|
| Bildgewicht auf einer Tourseite | **150,4 MB** | gemessen, HEAD-Requests auf 54 Dateien |
| Mediane Serverantwort | **4,33 s** | gemessen, 5 Läufe |
| Meta-Descriptions | **0 von 14 Seiten** | gemessen |
| schema.org-Blöcke | **0 auf 15 URLs** | gemessen |
| Installierte Analytik | **keine** | gemessen |
| Kontaktformulare | **0** | gemessen |

## Inhalt

```
argymaq-seo-case/
|-- site/                   statische Berichts-Website (Astro 5 + Tailwind 4)
|   |-- src/pages/          17 Routen
|   |-- src/components/     MetricCard, BeforeAfter, Phase, PriceCard, Steps
|   |-- src/data/           Leistungen, Pakete, Falldaten als JSON
|   `-- dist/               Build-Ausgabe (nicht in git)
|-- docs/
|   |-- architecture/       Website-Architektur und Designsystem
|   |-- reports/            Bericht für den Eigentümer (RU + EN)
|   |-- research/           Marktpreise, Berichtsmuster, GEO, Karten
|   `-- wiki/               mehrstufiges LLM-Wiki aller Befunde
|-- scripts/                11 Python-Skripte, die das Audit reproduzieren
|-- research/               Rohdaten zu Wettbewerbern und Benchmark
`-- data/                   SQLite-Wissensbasis + JSONL-Export
```

## Schnellstart

```bash
git clone https://github.com/homgorn/argymaq-seo-case.git
cd argymaq-seo-case/site
npm install
npm run dev        # lokale Vorschau
npm run build      # Build in dist/
npm run check      # Typprüfung
```

Audit erneut ausführen:

```bash
python scripts/crawl_full.py
python scripts/site_checks.py
python scripts/images_head.py
python scripts/competitors.py
python scripts/benchmark.py
python scripts/build_kb.py
python scripts/verify_site.py
```

## Dokumentation

| Dokument | Inhalt |
|---|---|
| [Architektur](docs/architecture/00-architecture.md) | Sitemap mit 17 Seiten, Designsystem, Datenmodell |
| [Kompetenzplan](docs/architecture/01-skill-plan.md) | wer in welcher Phase eingesetzt wird |
| [Bericht (RU)](docs/reports/seo-audit-2026-11-15.md) | vollständiger Bericht für den Kunden |
| [Bericht (EN)](docs/reports/seo-audit-2026-11-15.en.md) | englische Ausgabe desselben Berichts |
| [Preise, Kirgistan](docs/research/market-prices-kr/00-prices.md) | Marktpreise in Som, mit Quellen und Daten |
| [Kundenberichte](docs/research/client-reporting/00-reporting.md) | wie Agenturen Berichte gestalten, die gelesen werden |
| [GEO / KI-Suche](docs/research/geo-ai-search/00-geo.md) | Sichtbarkeit in ChatGPT, Perplexity, Google AI messen |
| [Lokale Karten](docs/research/local-maps/00-maps.md) | Yandex Maps, 2GIS, Google Business Profile |
| [Fallstruktur](docs/research/case-studies/00-case-study.md) | was ein Portfolio konvertieren lässt |
| [Wiki-Index](docs/wiki/40-index-portfolio.md) | alle Dokumente mit Querverweisen |

## Quellmarkierungen

| Marke | Bedeutung |
|---|---|
| **[measured]** | durch direkte Anfrage geprüft; die Zahl ist reproduzierbar |
| **[reported]** | aus externer Quelle mit URL und Datum |
| **[inferred]** | logische Schlussfolgerung, keine direkte Messung |
| **[panel]** | erfordert Zugang, den das Audit nicht hatte |

Keine Zahl ist erfunden. Wo Daten fehlten, wird die Lücke benannt, nicht gefüllt.

## Lizenz

MIT — siehe [LICENSE](LICENSE). Daten und Berichte dienen als Referenz.

Die Website `argymaq.kg` und ihre Marke gehören ihrem Eigentümer. Dieses Repository enthält Messungen und Empfehlungen, nicht deren Inhalte.