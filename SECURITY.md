# Security Policy

## Supported versions

| Version | Supported |
|---|---|
| `main` (latest) | yes |

This is a static audit report. There is no running service or server-side code.

## Reporting a vulnerability

Do **not** open a public issue for anything sensitive. Use a private contact
route — see the contacts listed in the fork's own repository settings, or the
maintainer's private channels.

If you find an exposed credential in this repository or its history, treat it
as compromised: rotating it takes priority over any other action.

## Scope

| In scope | Out of scope |
|---|---|
| Secrets committed to this repository | Findings about argymaq.kg — that site is the subject, not the project |
| Dependencies with known high-severity CVEs | Audit methodology opinions |
| XSS in the built static pages | Third-party services mentioned in the reports |

## Dependencies

```bash
cd site
npm audit --omit=dev
```