# Contributing

## What this repository is

A static audit report for one website: `argymaq.kg`. Contributions are useful
when they fix something measurable — a wrong figure, a broken link, a missing
fact — not when they expand scope.

## Before submitting

```bash
cd site
npm run check
npm run build

cd ..
python scripts/check_live.py
python scripts/verify_site.py
```

## Commit convention

Conventional Commits:

```
fix(data): correct measured image weight for the 5-day tour page
feat(site): add measurement note to the results page
docs(wiki): document the GEO measurement method
```

## Pull requests

- One concern per pull request.
- Describe what was measured and how a reviewer can reproduce it.
- Screenshots for any visual change.
- Update `docs/wiki/` when a finding is added or changed.

## Rules

1. **Do not invent figures.** Every number carries a source mark.
2. **No personal contacts** in this repository's public content.
3. **Plain language**: if a term needs explaining, explain it in the same sentence.
4. **One page, one purpose**: pages document the audit, not anything else.