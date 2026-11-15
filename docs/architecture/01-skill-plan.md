# План прохода по скиллам

Какие скиллы применять на каждом этапе и что именно они дают. Из 260+ доступных — только те, что реально нужны этому проекту.

## Принцип отбора

| Критерий | Как проверяем |
|---|---|
| Даёт артефакт | после применения остаётся файл или решение |
| Не дублирует | не делает то же, что уже сделали скрипты |
| Соответствует этапу | дизайн — на этапе дизайна, не раньше |
| Экономит контекст | не грузим всё сразу |

## Этап 0 — выбранные и уже применённые

| Скилл | Что дал | Статус |
|---|---|---|
| `seo-specialist-webmaster` | методика 10 этапов, чек-лист аудита, скрипт `site_audit.py` | применён |
| `seo-audit-mia` | фреймворк аудита, формат отчёта, 3 аудитории | применён |
| `blueprint-repo-github-classic` | структура репозитория, README на 7 языков, правила no-LLM | применён (архитектура) |
| `blueprint-site-astro-cloudflare` | стек Astro 7 + Tailwind v4, золотые правила | применён (архитектура) |
| `ui-ux-pro-max-nextlevel` | база дизайн-решений, 120 UX-гайдлайнов, 74 шрифтовые пары | применён (дизайн-система) |

## Этап 1 — дизайн и вёрстка

| Скилл | Когда | Что даёт |
|---|---|---|
| `frontend-design-anthropic` | перед версткой главной | эстетическое направление, чтобы не вышло «шаблонно» |
| `ui-styling-nextlevel` | на этапе компонентов | Tailwind-паттерны, доступные компоненты |
| `design-system-nextlevel` | если нужен UI-kit | трёхслойные токены: primitive → semantic → component |
| `canvas-design-anthropic` | если нужны статичные визуалы (обложки кейсов) | PNG/PDF макеты |

## Этап 2 — контент

| Скилл | Когда | Что даёт |
|---|---|---|
| `landing-page-mia-ru` | тексты главной, услуг, цен | модульные секции, формулы |
| `copy-anatomy-mia-ru` | разобрать удачные тексты конкурентов | шаблоны из чужого текста |
| `ai-humanizer-mia-ru` | проверить, что тексты не звучат «по-роботски» | оценка AI-паттернов |
| `seo-research-hyperfx` | семантика и контент-план | ключи, конкуренты, AI-видимость |
| `schema-markup-alireza` | микроразметка сайта | JSON-LD, валидация |

## Этап 3 — SEO сайта-портфолио

| Скилл | Когда | Что даёт |
|---|---|---|
| `aeo-alireza` | под AI-поиск | цитируемость, E-E-A-T |
| `site-architecture-alireza` | структура URL и перелинковка | кластеры, хабы |
| `programmatic-seo-alireza` | если страниц будет много (шаблоны под услуги/города) | генерация страниц |
| `blueprint-verify-gates` | перед деплоем | гейты качества |

## Этап 4 — GitHub и деплой

| Скилл | Когда | Что даёт |
|---|---|---|
| `blueprint-repo-github-classic` | упаковка репозитория | README 7 языков, topics, LICENSE, security |
| `blueprint-guardrails` | перед любым удалением | протокол двойного подтверждения |
| `blueprint-verify-gates` | перед релизом | secret scan, build, tests, Lighthouse |
| `blueprint-decompose-agents` | если работа пойдёт параллельно | декомпозиция, спавн агентов |

## Этап 5 — поддержка и развитие

| Скилл | Когда | Что даёт |
|---|---|---|
| `seo-specialist-webmaster` | ежемесячно | этапы 8–10: ссылки, GEO, рост |
| `research-mattpocock` | когда нужен быстрый ресёрч | сбор фактов в markdown |
| `deep-research-alireza` | сложные вопросы рынка | 3+ источника на утверждение |
| `verify-this-cursor` | проверить спорное утверждение | VERIFIED / NOT VERIFIED |

## Не применяем (и почему)

| Скилл | Почему нет |
|---|---|
| `figma-*` (6 шт) | нет доступа к Figma-файлам, работаем в коде |
| `pptx-anthropic`, `google-slides-cursor`, `slides-nextlevel` | формат — сайт, не презентация |
| `docx-anthropic` | отчёт нужен в вебе, не в Word |
| `render-*` (3 шт) | деплой на GitHub Pages, не на Render |
| `cloudflare-deploy-openai`, `wrangler` | GitHub Pages, не Cloudflare |
| `netlify-deploy-openai`, `vercel-deploy-openai` | GitHub Pages |
| `sentry-openai` | нет Sentry |
| `x-*` (4 шт) | нет X/Meta-интеграций в этой задаче |
| `figma-*`, `winui-*`, `aspnet-*` | другой стек |
| видео-скиллы (20+) | не нужны для статичного сайта |
| `notion-*` | нет Notion |
| `prime-agent` | работаем в этой сессии |

## Порядок применения (если продолжаем)

```
1. frontend-design-anthropic      → эстетика главной
2. ui-styling-nextlevel           → компоненты и токены
3. landing-page-mia-ru            → тексты
4. schema-markup-alireza          → разметка
5. aeo-alireza                    → AI-видимость
6. site-architecture-alireza      → структура
7. blueprint-verify-gates         → гейты
8. blueprint-repo-github-classic  → упаковка
9. blueprint-guardrails           → безопасность
```

Каждый шаг оставляет артефакт в `docs/` или `site/`.