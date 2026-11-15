# LLM-вики проекта: индекс

Многоуровневый индекс всех знаний проекта. Каждый документ самодостаточен.

## Уровень 0 — вход

| Документ | Что внутри |
|---|---|
| [00-README](00-README.md) | как устроена вики |
| [01-index-root](01-index-root.md) | корневой индекс |
| [02-glossary](02-glossary.md) | термины |
| [03-facts-verified](03-facts-verified.md) | измеренные факты |
| [04-open-questions](04-open-questions.md) | пробелы |

## Уровень 1 — аудит argymaq.kg

| Документ | Что внутри |
|---|---|
| [10-audit-summary](10-audit-summary.md) | executive summary |
| [11-technical](11-technical.md) | техника |
| [12-content-meta](12-content-meta.md) | контент |
| [13-competitors](13-competitors.md) | конкуренты |
| [14-semantics](14-semantics.md) | семантика |
| [15-local-geo](15-local-geo.md) | локальность |
| [16-legal-eeat](16-legal-eeat.md) | право, E-E-A-T |
| [17-images](17-images.md) | изображения |

## Уровень 2 — план внедрения

| Документ | Что внутри |
|---|---|
| [20-plan-p0](20-plan-p0.md) | неделя 1 |
| [21-plan-p1](21-plan-p1.md) | недели 2–4 |
| [22-plan-p2](22-plan-p2.md) | недели 4–8 |
| [23-plan-p3](23-plan-p3.md) | ссылки, GEO |
| [24-snippets](24-snippets.md) | готовые тексты |

## Уровень 3 — данные

| Документ | Что внутри |
|---|---|
| [30-data-schema](30-data-schema.md) | схема SQLite |
| [31-scripts](31-scripts.md) | 11 скриптов |
| [32-reproduce](32-reproduce.md) | воспроизведение |
| [33-sources](33-sources.md) | источники |

## Уровень 4 — архитектура сайта-портфолио

| Документ | Что внутри |
|---|---|
| [40-architecture](../architecture/00-architecture.md) | карта сайта, дизайн-система, стек, данные |
| [41-skill-plan](../architecture/01-skill-plan.md) | какие скиллы и когда |

## Уровень 5 — исследования

| Документ | Что внутри |
|---|---|
| [50-prices-kr](../research/market-prices-kr/00-prices.md) | цены рынка КР в сомах |
| [51-reporting](../research/client-reporting/00-reporting.md) | как подают отчёты |
| [52-geo](../research/geo-ai-search/00-geo.md) | GEO/AEO: продвижение под нейронки |
| [53-maps](../research/local-maps/00-maps.md) | Яндекс Карты, 2GIS, Google Maps |
| [54-case-study](../research/case-studies/00-case-study.md) | структура портфолио и кейсов |

## Связи между документами

```
Аудит (уровень 1) ──► План (уровень 2) ──► Кейс на сайте (уровень 4)
       │                                        ▲
       └──► Исследования (уровень 5) ───────────┘
                 │
                 ├── цены → пакеты на сайте
                 ├── отчёты → структура кейса
                 ├── GEO → услуга и раздел
                 └── карты → услуга и раздел
```

## Термины, которые нужно знать

| Термин | Значение |
|---|---|
| **GEO** | Generativ Engine Optimization — оптимизация под ответы ИИ |
| **AEO** | Answer Engine Optimization — оптимизация под поиск-ответы |
| **NAP** | Name, Address, Phone — единые контактные данные |
| **P0 / P1 / P2 / P3** | приоритеты внедрения |
| **Share of voice** | доля упоминаний бренда среди всех упоминаний |
| **Citation rate** | % ответов ИИ, где процитирован сайт |
| **Mention rate** | % ответов ИИ, где назван бренд |

## Правила работы с вики

1. Каждый факт помечен: **[измерено]** / **[сообщено]** / **[выведено]** / **[панель]**.
2. Цены — с датой замера.
3. Источники — с URL.
4. Ничего не выдумываем.
5. Обновляем документ, а не создаём копию.