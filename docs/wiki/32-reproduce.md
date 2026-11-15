# 32 — как воспроизвести прогон

Полный цикл с нуля. Занимает 3–5 минут (без загрузки изображений).

## Подготовка

```powershell
cd "H:\susa ai 500\argymaq.kg"
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
New-Item -ItemType Directory -Force -Path work\audit, data, research\raw | Out-Null
```

## Прогон

```powershell
# 1. Скрипт навыка webmaster: уровень сайта
python "C:\Users\Hiall\.config\opencode\skills\seo-specialist-webmaster\scripts\site_audit.py" site https://argymaq.kg/ --out work\audit

# 2. Расширенный краул 15 URL
python scripts\crawl_full.py

# 3. Проверки уровня сайта
python scripts\site_checks.py

# 4. Вес изображений
python scripts\images_head.py

# 5. Конкуренты
python scripts\competitors.py

# 6. Бенчмарк
python scripts\benchmark.py

# 7. Семантика
python scripts\semantics_core.py

# 8. База знаний
python scripts\build_kb.py

# 9. Сводка
python scripts\kb_query.py summary
```

## Ожидаемый вывод

```
run_id = 1
pages: 1
competitors: ok
images: ok
issues: 54
pages: 14
competitors: 7
images: 54
db: data\seo.db
jsonl: data\seo_kb.jsonl
```

## Что пересоздаётся с нуля

Если нужно начать заново:

```powershell
Remove-Item data\seo.db, data\seo.db-wal, data\seo.db-shm -ErrorAction SilentlyContinue
Remove-Item work\audit\*.json, work\audit\*.md, work\audit\*.csv -ErrorAction SilentlyContinue
python scripts\build_kb.py
```

Внимание: удаление файлов только по подтверждению. Скрипты выше перезаписывают результаты, а не удаляют.

## Проверка целостности

```powershell
# все скрипты компилируются
Get-ChildItem scripts\*.py | ForEach-Object { python -m py_compile $_.FullName; "$($_.Name): $LASTEXITCODE" }

# база отвечает
python scripts\kb_query.py summary
```

## Ограничения

| Что | Почему |
|---|---|
| GET изображений | ~30 КБ/с на этом хосте — используется HEAD |
| PageSpeed Insights | требует браузер или API |
| Живая выдача | CAPTCHA, обход запрещён |
| Wordstat | требует авторизации |

## Периодичность

| Как часто | Что перепроверять |
|---|---|
| После правок | `crawl_full.py`, `images_head.py`, `benchmark.py`, `build_kb.py` |
| Ежемесячно | `competitors.py` (динамика конкурентов) |
| Ежеквартально | полный прогон + новый отчёт |