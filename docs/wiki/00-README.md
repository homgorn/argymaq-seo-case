# 00 — README вики argymaq.kg

Многоуровневый индекс знаний по SEO-аудиту сайта argymaq.kg (регион Каракол).
Каждый документ самодостаточен: его можно прочитать без контекста чата.

## Уровень 0 — вход

| Документ | Что внутри |
|---|---|
| [00-README](00-README.md) | как устроена вики, правила чтения |
| [01-index-root](01-index-root.md) | корневой индекс: все разделы и файлы |
| [02-glossary](02-glossary.md) | термины и сокращения |
| [03-facts-verified](03-facts-verified.md) | только измеренные факты с методом замера |
| [04-open-questions](04-open-questions.md) | что неизвестно и требует владельца |

## Уровень 1 — аудит

| Документ | Что внутри |
|---|---|
| [10-audit-summary](10-audit-summary.md) | executive summary, топ-5 проблем, оценка |
| [11-technical](11-technical.md) | индексируемость, скорость, безопасность, изображения |
| [12-content-meta](12-content-meta.md) | title, description, H1, объём текста, alt |
| [13-competitors](13-competitors.md) | бенчмарк с 7 конкурентами ниши |
| [14-semantics](14-semantics.md) | семантическое ядро, кластеры, целевые страницы |
| [15-local-geo](15-local-geo.md) | локальное SEO по Караколу, топонимы |
| [16-legal-eeat](16-legal-eeat.md) | юридические страницы и E-E-A-T |
| [17-images](17-images.md) | 54 изображения, 408 МБ, разбор |

## Уровень 2 — план

| Документ | Что внутри |
|---|---|
| [20-plan-p0](20-plan-p0.md) | критичные правки недели 1 |
| [21-plan-p1](21-plan-p1.md) | контент и структура, недели 2–4 |
| [22-plan-p2](22-plan-p2.md) | скорость и качество, недели 4–8 |
| [23-plan-p3](23-plan-p3.md) | ссылки, GEO, масштабирование |
| [24-snippets](24-snippets.md) | готовые meta description, title, alt, JSON-LD |

## Уровень 3 — данные

| Документ | Что внутри |
|---|---|
| [30-data-schema](30-data-schema.md) | схема SQLite-базы и как ей пользоваться |
| [31-scripts](31-scripts.md) | 10 скриптов: что делают, как запускать |
| [32-reproduce](32-reproduce.md) | как воспроизвести прогон с нуля |
| [33-sources](33-sources.md) | источники: URL, даты, что взято |

## Сырые артефакты

| Путь | Формат |
|---|---|
| `data/seo.db` | SQLite (pages, issues, competitors, images, keywords, rankings, pages_fts) |
| `data/seo_kb.jsonl` | JSONL, по строке на объект |
| `data/keywords.json` | JSON, семантика |
| `work/audit/*.json` | сырые замеры краула |
| `work/audit/*.md` | отчёты скрипта |
| `research/*.md` | бенчмарк |
| `docs/reports/seo-audit-2026-11-15.md` | главный отчёт для владельца (RU) |
| `docs/reports/seo-audit-2026-11-15.en.md` | главный отчёт для владельца (EN) |