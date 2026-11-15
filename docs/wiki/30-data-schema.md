# 30 — схема базы знаний

SQLite: `data/seo.db`. Создаётся скриптом `scripts/build_kb.py`.

## Таблицы

### audit_run

| Поле | Тип | Что |
|---|---|---|
| id | INTEGER PK | номер прогона |
| site | TEXT | домен |
| region | TEXT | регион продвижения |
| run_at | TEXT | дата и время |
| tool | TEXT | какие методики применены |
| note | TEXT | примечание |

### pages

| Поле | Тип | Что |
|---|---|---|
| id | INTEGER PK | — |
| run_id | INTEGER | ссылка на прогон |
| url | TEXT UNIQUE | URL страницы |
| status | INTEGER | HTTP-код |
| title | TEXT | title |
| title_len | INTEGER | длина title |
| description | TEXT | meta description |
| desc_len | INTEGER | длина description |
| h1 | TEXT | H1 через « \|\| » |
| h1_count | INTEGER | число H1 |
| canonical | TEXT | canonical |
| meta_robots | TEXT | meta robots |
| lang | TEXT | атрибут lang |
| viewport | INTEGER | есть ли viewport |
| words | INTEGER | слов в тексте |
| text_len | INTEGER | символов текста |
| images | INTEGER | изображений |
| images_no_alt | INTEGER | без alt |
| internal_links | INTEGER | уникальных внутренних |
| external_links | INTEGER | внешних |
| ldjson | TEXT | типы schema.org |
| ldjson_broken | INTEGER | битый JSON |
| has_og | INTEGER | есть Open Graph |
| has_twitter | INTEGER | есть Twitter Card |
| hreflang | INTEGER | количество hreflang |
| ttfb | REAL | время ответа |
| html_bytes | INTEGER | размер HTML |
| metrika | INTEGER | есть Метрика |
| ga_gtm | INTEGER | есть GA/GTM |
| fb_pixel | INTEGER | есть FB Pixel |
| has_form | INTEGER | есть форма |
| fetched_at | TEXT | дата замера |

### issues

| Поле | Тип | Что |
|---|---|---|
| id | INTEGER PK | — |
| run_id | INTEGER | прогон |
| severity | TEXT | critical / warning / notice |
| category | TEXT | indexing, meta, content, tech, speed, legal, analytics, geo, commercial |
| page | TEXT | страница или «весь сайт» |
| title | TEXT | краткое название |
| fact | TEXT | измеренный факт |
| fix | TEXT | что делать |
| priority | INTEGER | 1 — критично, 2 — важно, 3 — по возможности |

### competitors

| Поле | Тип |
|---|---|
| id, run_id | INTEGER |
| name, url | TEXT |
| status | INTEGER |
| title_len, desc_len, h1_count | INTEGER |
| ldjson | TEXT |
| metrika, og | INTEGER |
| hreflang | INTEGER |
| prices | INTEGER |
| ttfb | REAL |
| html_bytes, images | INTEGER |

### images

| Поле | Тип |
|---|---|
| id, run_id | INTEGER |
| src | TEXT |
| ext | TEXT |
| bytes | INTEGER |
| status | INTEGER |
| cache_header | TEXT |
| pages | TEXT (через «\|») |
| http | INTEGER (по http://) |

### keywords

| Поле | Тип |
|---|---|
| id, run_id | INTEGER |
| phrase | TEXT |
| intent | TEXT (commercial / informational / brand) |
| volume | INTEGER (NULL, требует Wordstat) |
| source | TEXT |
| target_page | TEXT |
| cluster | TEXT |
| note | TEXT |

### rankings

| Поле | Тип |
|---|---|
| id, run_id | INTEGER |
| phrase | TEXT |
| engine | TEXT (yandex / google) |
| position | INTEGER |
| url | TEXT |
| checked_at | TEXT |
| source | TEXT |

### pages_fts (FTS5)

Полнотекстовый индекс по `url`, `title`, `h1`, `description`.

## Запросы

```bash
# сводка
python scripts/kb_query.py summary

# все критичные проблемы
python scripts/kb_query.py issues critical

# произвольный SQL
python scripts/kb_query.py sql "select url, words from pages order by words limit 5"

# полнотекстовый поиск
python scripts/kb_query.py fts "horseback"
```

## JSONL

`data/seo_kb.jsonl` — по строке на объект, поле `_table` указывает таблицу.

```bash
# сколько записей
wc -l data/seo_kb.jsonl

# только проблемы
grep '"_table": "issues"' data/seo_kb.jsonl | head -5
```