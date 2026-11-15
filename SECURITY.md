# Security Policy

## Supported versions

| Version | Supported |
|---|---|
| `main` (latest) | yes |
| any tagged release | until the next release |

This is a static documentation and audit repository. There is no running
service, no database, and no server-side code to patch.

## Reporting a vulnerability

Report vulnerabilities privately — do **not** open a public issue.

- **Email:** refertur@yandex.ru
- **Telegram:** @realhikaz
- **WhatsApp:** +996 555 707 267

Include:

1. what the issue is (secret exposure, dependency with a known CVE, XSS in the
   static build, supply-chain concern);
2. the file or dependency affected, with a link;
3. how it can be triggered;
4. whether you consider it exploitable.

Response target: within 72 hours.

## What counts as an issue here

| In scope | Out of scope |
|---|---|
| Secrets committed to git history | Findings about `argymaq.kg` — that site is not ours |
| Dependencies with known high-severity CVEs | Best-practice suggestions on the audit methodology |
| XSS or injection in the built static pages | Performance advice on the client site |
| Anything that could publish private data | Third-party services the docs mention |

## Secrets

No secrets are stored in this repository. `.env` files are git-ignored. If a
credential is ever found in history, treat it as compromised: rotate it first,
then report it here.

## Dependencies

The site is built with `npm`. CI runs `npm ci` on every push and pull request.
There is no automated dependency-audit workflow yet; run it locally:

```bash
cd site
npm audit --omit=dev
```