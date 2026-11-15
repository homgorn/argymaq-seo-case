# Contributing

## What this repository is

A reproducible SEO audit of a Kyrgyz tourism site, plus the static site that
presents it. Two kinds of contribution are useful:

1. **Corrections to measurements.** If a figure is wrong, show how you measured
   it and the script will be re-run.
2. **Improvements to the site.** Layout, accessibility, performance, clarity of
   explanation.

## Local development

```bash
cd site
npm install
npm run dev
```

Build and check before submitting:

```bash
npm run check
npm run build
```

Re-running the audit (Python 3.8+, standard library only):

```bash
python scripts/crawl_full.py
python scripts/build_kb.py
python scripts/verify_site.py
```

## Commit convention

Conventional commits:

```
feat(site): add before/after chart to the case page
fix(data): correct image weight for the 5-day tour
docs(wiki): document the GEO measurement method
```

Subject in lowercase, imperative, no trailing period. Say what changed, not
that work happened.

## Pull requests

- One concern per pull request.
- Describe what you measured, and how a reviewer can reproduce it.
- Screenshots for any visual change.
- Update `docs/wiki/` when adding a finding, so the knowledge base stays
  consistent.

## Rules

1. **Do not invent figures.** Every number in `docs/` carries a source mark.
   If you cannot measure it, mark it `[panel]` or `[inferred]`.
2. **Do not delete** without discussion. Open an issue first for anything that
   removes content, data, or a script.
3. **Do not copy** third-party text or images into `docs/` or `site/public/`.
   Quote with attribution and a URL.
4. **No LLM tooling mentions** in public-facing text (site pages, README, docs
   the client reads). This is a hard rule; see `AGENTS.md`.
5. **Keep the plain-language rule.** If a term needs explaining, explain it in
   the same sentence.

## Questions

- Email: refertur@yandex.ru
- Telegram: @realhikaz