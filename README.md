# argymaq.kg — аудит сайта и план внедрения

**Static audit report for the [argymaq.kg](https://argymaq.kg) website** — a horseback tour operator in Karakol, Kyrgyzstan.

The case is presented as a standalone client-facing report, not as a portfolio piece:
what was found, what each issue means for revenue, and in what order to fix.

**Live report:** https://homgorn.github.io/argymaq-seo-case/

## What this repository is

- A reproducible SEO audit of `argymaq.kg` (measured 14–15 November 2026).
- A static website presenting the audit: findings in plain language, a phased plan, and the measurements behind every claim.
- The scripts and data required to re-run the audit.

The site does not advertise any agency or sell anything. It documents one website, one audit.

## The numbers that started it

| Metric | Found | Source |
|---|---|---|
| Image weight on one tour page | **150.4 MB** | measured, HEAD requests on 54 files |
| Median server response time | **4.33 s** | measured, 5 runs |
| Meta descriptions | **0 of 14 pages** | measured |
| schema.org markup blocks | **0 across 15 URLs** | measured |
| Analytics installed | **none** | measured |
| Contact forms | **0** | measured |

Deep-audit findings (infrastructure): the site exposes the administrator login (`ARGYMAQKG` via the REST API and `/?author=1`), the exact WordPress version (`7.1.4`) in the generator meta tag and RSS feed, and the login form at `/wp-login.php` without rate limiting. `xmlrpc.php` is correctly blocked.

## What is inside

```
argymaq.kg-audit/   This case only. Developer portfolio lives in homgorn/homgorn.github.io
├── site/           Static report site (Astro 5 + Tailwind 4)      ← built to docs/, served by Pages
├── docs/
│   ├── reports/    Audit reports (RU, EN)
│   ├── research/   Competitor benchmark, GEO, local maps, market prices
│   ├── wiki/       LLM-readable wiki of the audit findings
│   └── STATUS.md   Project status
├── scripts/        11 Python scripts reproducing the audit
├── research/       Raw competitor data
└── data/           SQLite knowledge base + JSONL export
```

## Reading the report

| Section | Route | What it answers |
|---|---|---|
| Contents | `/` | What was measured and how this report is built |
| Audit | `/audit/` | What was found, severity by severity |
| Plan | `/plan/` | What to fix first, in four priority bands |
| Work | `/work/` | What has been done so far |
| Results | `/result/` | The before-figures, measured |

## Source marks in the docs

| Mark | Meaning |
|---|---|
| **[measured]** | verified by direct request; reproducible |
| **[reported]** | taken from an external source with URL and date |
| **[inferred]** | logical conclusion, not a direct measurement |
| **[panel]** | requires panel access the audit did not have |

No figure is invented. Where data was unavailable, the gap is stated, not filled.

## Re-run the audit

```bash
cd site
npm install
npm run build            # build the report into dist/, served from docs/
npm run check            # type check

cd ..
python scripts/crawl_full.py
python scripts/site_checks.py
python scripts/images_head.py
python scripts/competitors.py
python scripts/benchmark.py
python scripts/build_kb.py
```

## Documentation

| Document | What it covers |
|---|---|
| [Audit report (RU)](docs/reports/seo-audit-2026-11-15.md) | The report delivered to the client |
| [Audit report (EN)](docs/reports/seo-audit-2026-11-15.en.md) | Same report in English |
| [Architecture](docs/architecture/00-architecture.md) | Original design system and sitemap (historical) |
| [Prices, Kyrgyzstan](docs/research/market-prices-kr/00-prices.md) | Market rates in som, with sources and dates |
| [Reporting patterns](docs/research/client-reporting/00-reporting.md) | How agencies present reports that clients read |
| [GEO / AI search](docs/research/geo-ai-search/00-geo.md) | Measuring visibility in ChatGPT / Perplexity / Google AI |
| [Local maps](docs/research/local-maps/00-maps.md) | Yandex Maps, 2GIS, Google Business Profile |
| [LLM wiki index](docs/wiki/40-index-portfolio.md) | Every document, cross-linked |
| [Status](docs/STATUS.md) | What is done and what is not |

## License

MIT — see [LICENSE.txt](LICENSE.txt). The audit findings are reproducible and provided as-is.

`argymaq.kg` and its content belong to their owner. This repository contains measurements and recommendations about one website, not its content.