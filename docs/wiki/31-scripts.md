# 31 — скрипты

10 программ в `scripts/`. Все на стандартной библиотеке Python 3, запускаются из корня проекта.

## site_audit.py (из навыка webmaster)

| Команда | Что делает |
|---|---|
| `site` | проверки уровня сайта: robots, sitemap, зеркала, SSL, 404, favicon, title/description/H1 главной |
| `audit` | `site` + обход страниц + сводка |
| `crawl` | только обход, `pages.json` |
| `report` | сводка по `pages.json` |
| `urls` | точечная проверка списка URL |

```bash
python scripts/site_audit.py site https://argymaq.kg/ --out work/audit
python scripts/site_audit.py audit https://argymaq.kg/ --out work/audit --max-pages 100
```

Результаты: `site_report.md`, `summary.md`, `issues.csv`, `pages.json`.

## crawl_full.py

Расширенный паук: дополнительно собирает schema.org (JSON-LD), счётчики, hreflang, OG, Twitter, H1/H2/H3, изображения, блоки текста, якоря ссылок, заголовки.

```bash
python scripts/crawl_full.py
```

Результат: `work/audit/crawl_full.json` + по файлу `.meta.json` на каждый URL в `research/raw/`.

## site_checks.py

Проверки уровня сайта: скорость (5 замеров), заголовки безопасности, зеркала, сжатие, robots, AI-краулеры, сервисные страницы, маркеры главной, список CSS/JS, SSL.

```bash
python scripts/site_checks.py
```

Результат: `work/audit/site_checks.json`.

## images_head.py

Вес изображений через HEAD-запросы (сервер отдаёт корректный Content-Length только без Range).

```bash
python scripts/images_head.py
```

Результат: `work/audit/images_head.json`.

## images_exact.py

Вес изображений через GET (медленно, 30 КБ/с на этом хосте). Нужен, только если HEAD недоступен.

```bash
python scripts/images_exact.py
```

Результат: `work/audit/images_exact.json`.

## images_audit.py

Первая версия аудита изображений (HEAD + Range). Оставлена для истории: сервер на Range отвечает некорректно.

## competitors.py

Сбор метрик конкурентов: title, description, H1, JSON-LD, метрики, OG, hreflang, цены, скорость.

```bash
python scripts/competitors.py
```

Результат: `research/raw/competitors.json`.

## benchmark.py

Сравнение argymaq.kg с конкурентами: агрегаты + постраничная таблица.

```bash
python scripts/benchmark.py
```

Результат: `research/competitor-benchmark.md`.

## report_pages.py

Сводный разбор `crawl_full.json` в читаемый отчёт.

```bash
python scripts/report_pages.py
```

Результат: `work/audit/pages_overview.md`.

## semantics_core.py

Семантическое ядро: 38 фраз, 5 кластеров, подсказки поисковых систем.

```bash
python scripts/semantics_core.py
```

Результат: `data/keywords.json` + таблица `keywords` в БД.

## build_kb.py

Сборка базы знаний: pages, issues, competitors, images, JSONL.

```bash
python scripts/build_kb.py
```

Результат: `data/seo.db`, `data/seo_kb.jsonl`.

## kb_query.py

Доступ к базе: summary, issues, sql, fts.

```bash
python scripts/kb_query.py summary
python scripts/kb_query.py issues critical
python scripts/kb_query.py sql "select count(*) from pages"
python scripts/kb_query.py fts "horseback"
```

## Требования

| Что | Как |
|---|---|
| Python | 3.8+ |
| Зависимости | только стандартная библиотека |
| Кодировка | `PYTHONUTF8=1` для Windows |

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
```