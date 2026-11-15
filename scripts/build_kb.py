#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Локальная база знаний аудита: SQLite + JSONL.

Собирает артефакты аудита argymaq.kg в одну БД, чтобы по ней можно было
искать: страницы, проблемы, метрики, конкурентов, ссылки, изображения.

Таблицы:
  audit_run     — прогон аудита (кто, когда, что за сайт)
  pages         — паспорт страницы (мета, H1, объём, скорость, счётчики)
  issues        — найденные проблемы (severity, категория, страница, факт)
  competitors   — конкуренты и их метрики
  images        — изображения и их вес
  keywords      — семантическое ядро / спрос (заполняется исследователем)
  rankings      — позиции (заполняется по выгрузкам панелей)

Запуск:  python scripts/build_kb.py
Проверка: python scripts/kb_query.py "select count(*) from pages"
"""
import json
import os
import sqlite3
import sys
import time

ROOT = r"H:\susa ai 500\argymaq.kg"
DB = os.path.join(ROOT, "data", "seo.db")
JSONL = os.path.join(ROOT, "data", "seo_kb.jsonl")

SCHEMA = """
PRAGMA journal_mode=WAL;

CREATE TABLE IF NOT EXISTS audit_run (
  id INTEGER PRIMARY KEY,
  site TEXT, region TEXT, run_at TEXT, tool TEXT, note TEXT
);

CREATE TABLE IF NOT EXISTS pages (
  id INTEGER PRIMARY KEY,
  run_id INTEGER,
  url TEXT UNIQUE,
  status INTEGER,
  title TEXT, title_len INTEGER,
  description TEXT, desc_len INTEGER,
  h1 TEXT, h1_count INTEGER,
  canonical TEXT, meta_robots TEXT,
  lang TEXT, viewport INTEGER,
  words INTEGER, text_len INTEGER,
  images INTEGER, images_no_alt INTEGER,
  internal_links INTEGER, external_links INTEGER,
  ldjson TEXT, ldjson_broken INTEGER,
  has_og INTEGER, has_twitter INTEGER, hreflang INTEGER,
  ttfb REAL, html_bytes INTEGER,
  metrika INTEGER, ga_gtm INTEGER, fb_pixel INTEGER,
  has_price INTEGER, has_form INTEGER,
  fetched_at TEXT
);

CREATE TABLE IF NOT EXISTS issues (
  id INTEGER PRIMARY KEY,
  run_id INTEGER,
  severity TEXT,        -- critical | warning | notice
  category TEXT,        -- indexing, meta, content, tech, speed, legal, analytics, geo, commercial
  page TEXT,
  title TEXT,
  fact TEXT,            -- измеренный факт
  fix TEXT,
  priority INTEGER
);

CREATE TABLE IF NOT EXISTS competitors (
  id INTEGER PRIMARY KEY,
  run_id INTEGER,
  name TEXT, url TEXT, status INTEGER,
  title_len INTEGER, desc_len INTEGER, h1_count INTEGER,
  ldjson TEXT, metrika INTEGER, og INTEGER, hreflang INTEGER,
  prices INTEGER, ttfb REAL, html_bytes INTEGER, images INTEGER
);

CREATE TABLE IF NOT EXISTS images (
  id INTEGER PRIMARY KEY,
  run_id INTEGER,
  src TEXT, ext TEXT, bytes INTEGER, status INTEGER,
  cache_header TEXT, pages TEXT, http INTEGER
);

CREATE TABLE IF NOT EXISTS keywords (
  id INTEGER PRIMARY KEY,
  run_id INTEGER,
  phrase TEXT, intent TEXT, volume INTEGER, source TEXT,
  target_page TEXT, cluster TEXT, note TEXT
);

CREATE TABLE IF NOT EXISTS rankings (
  id INTEGER PRIMARY KEY,
  run_id INTEGER,
  phrase TEXT, engine TEXT, position INTEGER, url TEXT,
  checked_at TEXT, source TEXT
);

CREATE VIRTUAL TABLE IF NOT EXISTS pages_fts USING fts5(
  url, title, h1, description, content='pages', content_rowid='id'
);

CREATE INDEX IF NOT EXISTS ix_issues_sev ON issues(severity, category);
CREATE INDEX IF NOT EXISTS ix_pages_url ON pages(url);
"""


def main():
    if os.path.exists(DB):
        # не пересоздаём с нуля: только схема
        pass
    con = sqlite3.connect(DB)
    con.executescript(SCHEMA)
    cur = con.cursor()

    cur.execute("SELECT id FROM audit_run ORDER BY id DESC LIMIT 1")
    row = cur.fetchone()
    if row:
        run_id = row[0]
    else:
        cur.execute("INSERT INTO audit_run(site, region, run_at, tool, note) "
                    "VALUES(?,?,?,?,?)",
                    ("argymaq.kg", "Каракол (Кыргызстан)", time.strftime("%Y-%m-%d %H:%M"),
                     "seo-specialist-webmaster + seo-audit-mia + локальные скрипты",
                     "полный технический SEO-аудит"))
        run_id = cur.lastrowid
    print("run_id =", run_id)

    # --- pages
    cf = os.path.join(ROOT, "work", "audit", "crawl_full.json")
    if os.path.exists(cf):
        d = json.load(open(cf, encoding="utf-8"))
        for p in d["pages"]:
            if p.get("status") != 200 or "wp-json" in p["url"]:
                continue
            cur.execute("""INSERT OR REPLACE INTO pages
              (run_id,url,status,title,title_len,description,desc_len,h1,h1_count,
               canonical,meta_robots,lang,viewport,words,text_len,images,images_no_alt,
               internal_links,external_links,ldjson,ldjson_broken,has_og,has_twitter,
               hreflang,ttfb,html_bytes,metrika,ga_gtm,fb_pixel,has_form,fetched_at)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                        (run_id, p["url"], p["status"], p.get("title"), p.get("title_len"),
                         p.get("meta_description"), len(p.get("meta_description") or ""),
                         " || ".join(p.get("h1") or []), p.get("h1_count"),
                         p.get("canonical"), p.get("meta_robots"), p.get("lang"),
                         1 if p.get("viewport") else 0,
                         p.get("words_total"), p.get("text_len"),
                         p.get("img_total"), p.get("img_no_alt"),
                         p.get("internal_unique"), len(p.get("external_links") or []),
                         ",".join(p.get("ldjson_types") or []),
                         1 if p.get("ldjson_broken") else 0,
                         1 if p.get("og") else 0,
                         1 if p.get("twitter") else 0,
                         len(p.get("hreflang") or []),
                         p.get("elapsed"), p.get("html_bytes"),
                         1 if (p.get("counters") or {}).get("metrika") else 0,
                         1 if (p.get("counters") or {}).get("gtm_ga") else 0,
                         1 if (p.get("counters") or {}).get("fb_pixel") else 0,
                         p.get("forms") or 0,
                         d.get("fetched_at")))
        print("pages:", cur.rowcount if cur.rowcount > 0 else "ok")

    # --- competitors
    co = os.path.join(ROOT, "research", "raw", "competitors.json")
    if os.path.exists(co):
        d = json.load(open(co, encoding="utf-8"))
        for c in d["targets"]:
            if c.get("status") != 200:
                continue
            cur.execute("""INSERT INTO competitors
              (run_id,name,url,status,title_len,desc_len,h1_count,ldjson,metrika,og,
               hreflang,prices,ttfb,html_bytes,images)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                        (run_id, c["name"], c["url"], c["status"], c["title_len"],
                         c["desc_len"], c["h1_count"], ",".join(c.get("ldjson") or []),
                         1 if c.get("metrika") else 0, 1 if c.get("og") else 0,
                         c.get("hreflang"), 1 if c.get("currency_mention") else 0,
                         c.get("elapsed"), c.get("html_bytes"), c.get("img")))
        print("competitors: ok")

    # --- images
    im = os.path.join(ROOT, "work", "audit", "images_head.json")
    if os.path.exists(im):
        d = json.load(open(im, encoding="utf-8"))
        for r in d["images"]:
            cur.execute("""INSERT INTO images
              (run_id,src,ext,bytes,status,cache_header,pages,http)
              VALUES(?,?,?,?,?,?,?,?)""",
                        (run_id, r["src"], r["ext"], r["bytes"], r["status"],
                         r.get("cache"), "|".join(r.get("pages") or []),
                         1 if r.get("http") else 0))
        print("images: ok")

    # --- issues: собираем из отчётов аудита
    # дедупликация: одинаковая проблема описывается один раз на весь сайт,
    # а не на каждую страницу
    def add(sev, cat, page, title, fact, fix, prio):
        key = (sev, cat, title)
        if key in _seen:
            return
        _seen.add(key)
        cur.execute("""INSERT INTO issues(run_id,severity,category,page,title,fact,fix,priority)
                       VALUES(?,?,?,?,?,?,?,?)""",
                    (run_id, sev, cat, page, title, fact, fix, prio))

    _seen = set()
    pages_rows = cur.execute(
        "SELECT url,title,desc_len,h1_count,words,ldjson,metrika,canonical,meta_robots,"
        "images,images_no_alt,ttfb,has_og FROM pages WHERE run_id=?", (run_id,)).fetchall()
    for (url, title, dlen, h1n, words, ld, metr, can, robots, ni, nalt, ttfb, og) in pages_rows:
        if dlen == 0:
            add("critical", "meta", url, "Пустой meta description",
                "description отсутствует на всех страницах сайта",
                "Прописать уникальные description 140–160 знаков с топонимом Каракол и УТП", 1)
        if h1n == 0:
            add("critical", "meta", url, "Нет H1",
                "На странице отсутствует заголовок H1",
                "Добавить один H1 с ключевым запросом страницы", 1)
        if h1n > 1:
            add("warning", "meta", url, "Несколько H1 (%d)" % h1n,
                "На странице %d заголовка H1 — размывается смысловой центр" % h1n,
                "Оставить один H1, остальные перевести в H2/H3", 2)
        if words < 300:
            add("warning", "content", url, "Мало текста: %d слов" % words,
                "Объём текста ниже порога 300 слов для коммерческой страницы",
                "Расширить описание маршрута: программа по дням, что входит, сложность, "
                "сезон, снаряжение, FAQ", 2)
        if not ld:
            add("critical", "tech", url, "Нет микроразметки JSON-LD",
                "На странице нет ни одного блока schema.org",
                "Внедрить TouristTrip/Product+Offer, BreadcrumbList, Organization, "
                "LocalBusiness, FAQPage, WebSite+SearchAction", 1)
        if not metr:
            add("critical", "analytics", url, "Нет счётчика аналитики",
                "На сайте не установлены Яндекс Метрика и GA4/GTM — данные о трафике "
                "и поведении не собираются",
                "Установить Яндекс Метрику (Вебвизор, цели) и GA4 через GTM", 1)
        if nalt:
            add("warning", "content", url, "Изображения без alt: %d из %d" % (nalt, ni),
                "Ни одно изображение не имеет alt-атрибута",
                "Прописать alt по шаблону «что на фото + локация + маршрут»", 2)
        if ttfb and ttfb > 2:
            add("warning", "speed", url, "Медленный ответ: %.1f c" % ttfb,
                "TTFB выше 2 секунд",
                "Кэширование страниц (WP Super Cache/LiteSpeed), OPcache, CDN", 2)
        if not og:
            add("warning", "tech", url, "Нет Open Graph",
                "Соцсети и мессенджеры не получают карточку ссылки",
                "Добавить og:title/description/image/url/type + twitter:card", 2)

    add("critical", "indexing", "весь сайт",
        "Нет приоритетных sitemap и hreflang для RU/KY/EN",
        "sitemap отдаёт 13 URL; нет hreflang, хотя контент англоязычный при lang=ru-RU",
        "Согласовать language-версии, добавить hreflang, разделить sitemap по типам", 1)
    add("critical", "tech", "весь сайт",
        "Нет ни одного блока schema.org на 15 проверенных URL",
        "Проверено 15 URL (главная, 8 страниц, таксономии, автор, ?p=19) — ld+json 0",
        "Внедрить JSON-LD на уровне темы/плагина", 1)
    add("critical", "speed", "изображения",
        "Изображения не оптимизированы",
        "54 уникальных PNG общим весом 408 МБ, средний 7.7 МБ; на странице тура "
        "до 150 МБ картинок; webp/avif нет",
        "Пережать в WebP (640/1024/1600), убрать исходники 12–15 МБ, включить "
        " srcset и lazy-load", 1)
    add("critical", "tech", "/",
        "Смешанный контент: картинки по http://",
        "На главной и /our-tours/ часть изображений отдаётся по http:// "
        "при https-сайте",
        "Заменить все http:// на https:// (или protocol-relative) в медиатеке и "
        "настройках Elementor", 1)
    add("warning", "tech", "/",
        "HTML lang=ru-RU при англоязычном контенте",
        "ru-RU назначен, весь текст на английском",
        "Поставить en (или en-KG) либо сделать языковые версии", 2)
    add("warning", "tech", "/",
        "Нет сжатия ответа",
        "Content-Encoding отсутствует: HTML 142 КБ отдаётся без gzip/br",
        "Включить gzip/brotli на nginx", 2)
    add("warning", "tech", "/",
        "Нет заголовков безопасности и кэширования",
        "Нет HSTS, CSP, X-Content-Type-Options, Cache-Control для HTML и статики",
        "Добавить заголовки на nginx + Cache-Control на /wp-content/uploads/", 2)
    add("warning", "tech", "/",
        "Нет редиректа главной-дубля ?p=19",
        "?p=19 отдаёт 200 и полностью дублирует главную",
        "301 с ?p=N на канонический URL либо запрет в robots", 2)
    add("warning", "indexing", "/blog/",
        "Служебные страницы в индексе",
        "В sitemap: /category/без-рубрики/, /author/argymaqkg/, запись "
        "«Привет, мир» с дефолтным комментарием",
        "Удалить демо-запись и комментарий, закрыть пустые архивы, оставить "
        "полезное", 2)
    add("critical", "indexing", "весь сайт",
        "Страница-двойник: /blog/ отдаёт контент 3-дневного тура",
        "Title /blog/ = «3-Day Horseback Tour: Lesnoye…», то есть блог подменяет "
        "страницу тура",
        "Развести: /blog/ — список статей, тур — отдельная страница /3-day-…", 1)
    add("warning", "commercial", "все страницы туров",
        "Нет цен, дат, программы и условий бронирования",
        "Ни на одной странице тура нет цены, длительности в цифрах, включённых "
        "услуг и CTA-формы",
        "Добавить блок «что входит / цена / даты / как забронировать» + форму", 1)
    add("critical", "analytics", "весь сайт",
        "Нет целей и конверсий",
        "Форм на сайте нет (0 input), единственный канал связи — WhatsApp",
        "Добавить формы (бронь, обратный звонок) с целями в Метрике", 1)
    add("warning", "legal", "весь сайт",
        "Нет юридических страниц",
        "Отсутствуют политика конфиденциальности, согласие на обработку ПД, "
        "оферта, реквизиты",
        "Опубликовать privacy policy, cookie-баннер, реквизиты в подвале", 2)
    add("warning", "geo", "весь сайт",
        "Нет привязки к региону и локальных сигналов",
        "В тексте нет топонима Каракол на главной (H1 «HORSEBACK RIDING»), "
        "нет адреса, телефона, карты",
        "Добавить адрес/телефон/карту, LocalBusiness schema, страницу контактов, "
        "регион в Яндекс Вебмастере", 1)
    add("notice", "content", "/",
        "Текст написан на английском при русскоязычном домене .kg",
        "Домен .kg, регион Каракол, но весь контент английский; русской версии нет",
        "Решить языковую стратегию: EN как основная + RU-версия под локальный спрос",
        3)

    con.commit()
    # JSONL-выгрузка знаний
    with open(JSONL, "w", encoding="utf-8") as f:
        for table in ("pages", "issues", "competitors", "images"):
            cols = [c[1] for c in cur.execute("PRAGMA table_info(%s)" % table)]
            for row in cur.execute("SELECT * FROM %s" % table):
                f.write(json.dumps({"_table": table,
                                    **dict(zip(cols, row))}, ensure_ascii=False) + "\n")
    print("issues:", cur.execute("SELECT count(*) FROM issues").fetchone()[0])
    print("pages:", cur.execute("SELECT count(*) FROM pages").fetchone()[0])
    print("competitors:", cur.execute("SELECT count(*) FROM competitors").fetchone()[0])
    print("images:", cur.execute("SELECT count(*) FROM images").fetchone()[0])
    print("db:", DB)
    print("jsonl:", JSONL)
    con.close()


if __name__ == "__main__":
    main()