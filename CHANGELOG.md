# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Nothing yet.

## [0.1.0] — 2026-11-15

First public release: the complete audit and the client-facing report site.

### Added

**Audit**
- Local audit scripts: `site_audit.py` integration, plus `crawl_full.py`,
  `site_checks.py`, `images_head.py`, `images_exact.py`, `competitors.py`,
  `benchmark.py`, `semantics_core.py`, `build_kb.py`, `kb_query.py`,
  `report_pages.py`, `verify_site.py`.
- SQLite knowledge base (`data/seo.db`) with `pages`, `issues`, `competitors`,
  `images`, `keywords`, `rankings` and a full-text index over pages.
- JSONL export of the knowledge base (`data/seo_kb.jsonl`).
- Semantic core: 38 phrases across 5 clusters, with search suggestions.
- Competitor benchmark across 7 operators in the Karakol niche.
- Market price research for Kyrgyzstan, in som, with sources and dates.

**Report site**
- 17-page static site built with Astro 5 and Tailwind 4.
- Pages: home, six services, packages and prices, process, about, contacts, and
  a five-page case study (overview, audit, plan, implementation, results).
- Components: `MetricCard`, `BeforeAfter`, `Phase`, `PriceCard`,
  `ServiceCard`, `Steps`, `Header`, `Footer`.
- Charts on the results page: server response time and image weight per page.
- JSON-LD across all pages: `Organization`, `WebSite`, `Service`, `ItemList`,
  `Offer`, `HowTo`, `Article`, `FAQPage`, `ContactPage`, `AboutPage`.
- GitHub Actions: CI (install, type check, build) and Pages deployment.

**Documentation**
- Audit report for the owner, in Russian and English.
- Architecture and design system for the report site.
- Skill application plan.
- LLM wiki: 5 levels, 22 documents, cross-linked.
- Research notes: client reporting patterns, GEO/AI search, local maps,
  case-study structure, Kyrgyz market prices.
- `AGENTS.md` with the working rules for this repository.

### Notes
- All figures in the documentation carry a source mark: `[measured]`,
  `[reported]`, `[inferred]`, or `[panel]`.
- Values marked as targets rather than results are labelled as such; no
  measurement is presented as an outcome before it exists.