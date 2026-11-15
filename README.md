<!-- Language: English is the primary README. Translations follow. -->
<div align="center">

**English** · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [中文](README.zh.md) · [日本語](README.ja.md)

</div>

---

# argymaq-seo-case
**Full SEO audit of a Kyrgyz tourism website, packaged as a client-ready static report and a portfolio case study.**

Live site: **https://homgorn.github.io/argymaq-seo-case/**

![Audit](https://img.shields.io/badge/audit-54%20issues-critical) ![Pages](https://img.shields.io/badge/pages-17%20built-success) ![Stack](https://img.shields.io/badge/Astro-5.18-ff5d01) ![License](https://img.shields.io/badge/license-MIT-blue)

---

## What this is

A complete, reproducible SEO audit of **argymaq.kg** — a horseback riding tour operator in Karakol, Kyrgyzstan — turned into two deliverables:

1. **A client-facing static website** (Astro, 17 pages) that explains the findings in plain language, with charts, before/after comparisons, and a phased plan. Built for an owner who does not work in SEO.
2. **A full audit dataset** — every measurement, script, and source, so the work can be re-run and verified.

The case is presented as **before → after**: what was found, what it means for revenue, and what gets fixed first.

### The numbers that started it

| Metric | Before | Source |
|---|---|---|
| Image weight on one tour page | **150.4 MB** | measured, HEAD requests on 54 files |
| Median server response | **4.33 s** | measured, 5 runs |
| Meta descriptions | **0 of 14 pages** | measured |
| schema.org blocks | **0 across 15 URLs** | measured |
| Analytics installed | **none** | measured |
| Contact forms | **0** | measured |

## What is inside

```
argymaq-seo-case/
|-- site/                   the static report website (Astro 5 + Tailwind 4)
|   |-- src/pages/          17 routes
|   |-- src/components/     MetricCard, BeforeAfter, Phase, PriceCard, Steps
|   |-- src/data/           services, packages, case data as JSON
|   `-- dist/               built output (git-ignored)
|-- docs/
|   |-- architecture/       site architecture and design system
|   |-- reports/            the audit report for the owner (RU + EN)
|   |-- research/           market prices, reporting patterns, GEO, local maps
|   `-- wiki/               multi-level LLM wiki of every finding
|-- scripts/                11 Python scripts that reproduce the audit
|-- research/               raw competitor data and benchmark
`-- data/                   SQLite knowledge base + JSONL export
```

## Quick start

```bash
git clone https://github.com/homgorn/argymaq-seo-case.git
cd argymaq-seo-case/site
npm install
npm run dev        # local preview
npm run build      # production build into dist/
npm run check      # TypeScript and Astro checks
```

Re-run the audit:

```bash
python scripts/crawl_full.py
python scripts/site_checks.py
python scripts/images_head.py
python scripts/competitors.py
python scripts/benchmark.py
python scripts/build_kb.py
python scripts/verify_site.py
```

## Documentation

| Document | What it covers |
|---|---|
| [Architecture](docs/architecture/00-architecture.md) | 17-page sitemap, design system, data model |
| [Skill plan](docs/architecture/01-skill-plan.md) | which specialists apply at which stage |
| [Audit report (RU)](docs/reports/seo-audit-2026-11-15.md) | the full report delivered to the client |
| [Audit report (EN)](docs/reports/seo-audit-2026-11-15.en.md) | English edition of the same report |
| [Prices, Kyrgyzstan](docs/research/market-prices-kr/00-prices.md) | market rates in som, with sources and dates |
| [Client reporting](docs/research/client-reporting/00-reporting.md) | how agencies present reports that get read |
| [GEO / AI search](docs/research/geo-ai-search/00-geo.md) | measuring visibility in ChatGPT, Perplexity, Google AI |
| [Local maps](docs/research/local-maps/00-maps.md) | Yandex Maps, 2GIS, Google Business Profile |
| [Case study structure](docs/research/case-studies/00-case-study.md) | what makes a portfolio convert |
| [LLM wiki index](docs/wiki/40-index-portfolio.md) | every document, cross-linked |

## Reading the source labels

Every claim in the docs carries a mark:

| Mark | Meaning |
|---|---|
| **[measured]** | verified by a direct request; the figure is reproducible |
| **[reported]** | taken from an external source with URL and date |
| **[inferred]** | a logical conclusion, not a direct measurement |
| **[panel]** | requires access the audit did not have |

No figure is invented. Where data was unavailable, the gap is stated rather than filled.

## License

MIT — see [LICENSE](LICENSE). The audit data and reports are provided as-is, for reference.

The `argymaq.kg` site and brand belong to their owner. This repository contains measurements and recommendations, not their content.