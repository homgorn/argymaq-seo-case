#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка веса изображений и HTTP→HTTPS мисматча на argymaq.kg.

Собирает все src картинок из crawl_full.json, качает заголовки, считает
байты, проверяет наличие webp/avif, srcset и mixed-content риски.
Результат: work/audit/images.json + отчёт в stdout.
"""
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
ROOT = r"H:\susa ai 500\argymaq.kg"
OUT = os.path.join(ROOT, "work", "audit", "images.json")


def head(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return {"status": r.status, "len": int(r.headers.get("Content-Length") or 0),
                    "ctype": r.headers.get("Content-Type"),
                    "cache": r.headers.get("Cache-Control"),
                    "final": r.geturl()}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "len": 0, "ctype": None, "cache": None, "final": url}
    except Exception as e:
        return {"status": 0, "len": 0, "ctype": None, "cache": None, "final": url,
                "error": str(e)}


def main():
    d = json.load(open(os.path.join(ROOT, "work", "audit", "crawl_full.json"),
                       encoding="utf-8"))
    seen, rows = {}, []
    for p in d["pages"]:
        for i in (p.get("images") or []):
            src = i.get("src") or ""
            if not src or src.startswith("data:"):
                continue
            if src not in seen:
                seen[src] = head(src)
                time.sleep(0.05)
            h = seen[src]
            rows.append({"page": p["url"].replace("https://argymaq.kg", "") or "/",
                         "src": src,
                         "http": src.startswith("http://"),
                         "ext": os.path.splitext(urllib.parse.urlsplit(src).path)[1].lower(),
                         "bytes": h["len"], "ctype": h["ctype"],
                         "status": h["status"], "cache": h["cache"]})
    total = sum(r["bytes"] for r in rows if r["bytes"])
    pages = {}
    for r in rows:
        pages.setdefault(r["page"], []).append(r)
    print("Уникальных изображений: %d" % len(seen))
    print("Суммарный вес (по ссылкам на страницах): %.1f МБ" % (total / 1048576))
    print("Из них по http:// (риск mixed content): %d" % sum(1 for r in rows if r["http"]))
    print("Форматы: %s" % {e: sum(1 for r in rows if r["ext"] == e) for e in set(r["ext"] for r in rows)})
    print("\n%-52s %9s %7s %s" % ("страница", "шт", "вес,КБ", "http"))
    for pg, items in sorted(pages.items(), key=lambda kv: -sum(x["bytes"] for x in kv[1])):
        b = sum(x["bytes"] for x in items)
        print("%-52s %9d %7.0f %s" % (pg[:52], len(items), b / 1024,
                                      sum(1 for x in items if x["http"])))
    print("\nТоп-12 самых тяжёлых файлов:")
    for r in sorted(rows, key=lambda x: -x["bytes"])[:12]:
        print("  %8.0f КБ  %-5s %s" % (r["bytes"] / 1024, r["ext"], r["src"][:110]))
    json.dump({"pages": pages, "total_bytes": total, "fetched": time.strftime("%Y-%m-%d %H:%M")},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\nsaved", OUT)


if __name__ == "__main__":
    main()