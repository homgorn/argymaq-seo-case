#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сравнение argymaq.kg с конкурентами ниши «конные туры Каракол».

Источники:
  work/audit/crawl_full.json          — собственный краул (14.11.2026)
  research/raw/competitors.json       — выборка конкурентов (14.11.2026)

Результат: research/competitor-benchmark.md + агрегаты в stdout.
"""
import json
import os
import re

ROOT = r"H:\susa ai 500\argymaq.kg"
MINE = os.path.join(ROOT, "work", "audit", "crawl_full.json")
COMP = os.path.join(ROOT, "research", "raw", "competitors.json")
OUT_MD = os.path.join(ROOT, "research", "competitor-benchmark.md")

PRICE_RE = re.compile(r"(?:\$|€)\s?\d|\d[\d\s,.]{1,7}\s?(?:сом|KGS|USD|usd|\$)")


def share(rows, pred):
    if not rows:
        return 0
    return 100 * sum(1 for r in rows if pred(r)) // len(rows)


def avg(rows, key):
    vals = [r[key] for r in rows if isinstance(r.get(key), (int, float))]
    return round(sum(vals) / len(vals), 1) if vals else 0


def main():
    mine_raw = json.load(open(MINE, encoding="utf-8"))["pages"]
    comp_raw = json.load(open(COMP, encoding="utf-8"))["targets"]

    mine_rows, comp_rows, detail = [], [], []

    for p in mine_raw:
        if p.get("status") != 200 or "wp-json" in p["url"]:
            continue
        blob = " ".join(b[1] for b in (p.get("blocks_sample") or []))
        r = {
            "site": "argymaq.kg",
            "url": p["url"].replace("https://argymaq.kg", "") or "/",
            "title_len": p.get("title_len") or 0,
            "desc_len": len(p.get("meta_description") or ""),
            "h1": p.get("h1_count") or 0,
            "words": p.get("words_total") or 0,
            "img": p.get("img_total") or 0,
            "noalt": p.get("img_no_alt") or 0,
            "ld": ",".join(p.get("ldjson_types") or []) or "-",
            "metrika": bool((p.get("counters") or {}).get("metrika")),
            "og": bool(p.get("og")),
            "hl": len(p.get("hreflang") or []),
            "sec": p.get("elapsed") or 0,
            "html": p.get("html_bytes") or 0,
            "price": bool(PRICE_RE.search(blob)),
            "int": p.get("internal_unique") or 0,
        }
        mine_rows.append(r)
        detail.append(r)

    for c in comp_raw:
        if c.get("status") != 200:
            continue
        r = {
            "site": c["name"],
            "url": c["url"][:58],
            "title_len": c["title_len"],
            "desc_len": c["desc_len"],
            "h1": c["h1_count"],
            "words": c.get("text_blocks") or 0,
            "img": c.get("img") or 0,
            "noalt": c.get("img_noalt") or 0,
            "ld": ",".join(c.get("ldjson") or []) or "-",
            "metrika": bool(c.get("metrika")),
            "og": bool(c.get("og")),
            "hl": c.get("hreflang") or 0,
            "sec": c.get("elapsed") or 0,
            "html": c.get("html_bytes") or 0,
            "price": bool(c.get("currency_mention")),
            "int": c.get("internal_links") or 0,
        }
        comp_rows.append(r)
        detail.append(r)

    agg = [
        ("метрика", "argymaq.kg", "конкуренты"),
        ("страниц в выборке", len(mine_rows), len(comp_rows)),
        ("title, знаков (сред.)", avg(mine_rows, "title_len"), avg(comp_rows, "title_len")),
        ("description заполнен, %", share(mine_rows, lambda r: r["desc_len"] > 0),
         share(comp_rows, lambda r: r["desc_len"] > 0)),
        ("description, знаков (сред.)", avg(mine_rows, "desc_len"), avg(comp_rows, "desc_len")),
        ("JSON-LD есть, %", share(mine_rows, lambda r: r["ld"] != "-"),
         share(comp_rows, lambda r: r["ld"] != "-")),
        ("Open Graph, %", share(mine_rows, lambda r: r["og"]),
         share(comp_rows, lambda r: r["og"])),
        ("hreflang, шт. (сред.)", avg(mine_rows, "hl"), avg(comp_rows, "hl")),
        ("аналитика (Метрика/GA), %", share(mine_rows, lambda r: r["metrika"]),
         share(comp_rows, lambda r: r["metrika"])),
        ("цена на странице, %", share(mine_rows, lambda r: r["price"]),
         share(comp_rows, lambda r: r["price"])),
        ("H1, шт. (сред.)", avg(mine_rows, "h1"), avg(comp_rows, "h1")),
        ("текстовых блоков (сред.)", avg(mine_rows, "words"), avg(comp_rows, "words")),
        ("изображений (сред.)", avg(mine_rows, "img"), avg(comp_rows, "img")),
        ("без alt, % от изображений",
         round(100 * sum(r["noalt"] for r in mine_rows) / max(1, sum(r["img"] for r in mine_rows))),
         round(100 * sum(r["noalt"] for r in comp_rows) / max(1, sum(r["img"] for r in comp_rows)))),
        ("время ответа, сек (сред.)", avg(mine_rows, "sec"), avg(comp_rows, "sec")),
        ("HTML, КБ (сред.)", round(avg(mine_rows, "html") / 1024, 1),
         round(avg(comp_rows, "html") / 1024, 1)),
    ]

    md = ["# Бенчмарк: argymaq.kg против конкурентов ниши",
          "",
          "Замер: 14.11.2026. Источники — собственный краул "
          "(`work/audit/crawl_full.json`) и выборка конкурентов "
          "(`research/raw/competitors.json`). Регион продвижения: Каракол.",
          "",
          "## Сводные показатели", "",
          "| " + " | ".join(str(x) for x in agg[0]) + " |",
          "|---|---|---|"]
    for name, a, b in agg[1:]:
        md.append("| %s | %s | %s |" % (name, a, b))
    md += ["", "## Постранично", "",
           "| сайт | URL | title | desc | H1 | блоков | img | без alt | разметка | Метр. | OG | hl | сек | HTML | цена |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in detail:
        md.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            r["site"], r["url"], r["title_len"], r["desc_len"], r["h1"], r["words"],
            r["img"], r["noalt"], r["ld"][:34] or "-", "Y" if r["metrika"] else "N",
            "Y" if r["og"] else "N", r["hl"], r["sec"], r["html"],
            "Y" if r["price"] else "N"))
    md.append("")
    open(OUT_MD, "w", encoding="utf-8").write("\n".join(md))

    w = [26, 18, 18]
    print("%-*s %*s %*s" % (w[0], agg[0][0], w[1], agg[0][1], w[2], agg[0][2]))
    for name, a, b in agg[1:]:
        print("%-*s %*s %*s" % (w[0], name, w[1], a, w[2], b))
    print("\n-> " + OUT_MD)


if __name__ == "__main__":
    main()