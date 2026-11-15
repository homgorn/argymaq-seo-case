#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Точный вес изображений argymaq.kg (GET, многопоточно).

HEAD на этом сервере отдаёт неверный Content-Length (206 + 2 байта),
поэтому размеры снимаем реальным GET-запросом в 6 потоков.
Результат: work/audit/images_exact.json
"""
import json
import os
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
ROOT = r"H:\susa ai 500\argymaq.kg"
OUT = os.path.join(ROOT, "work", "audit", "images_exact.json")


def one(item):
    src, pages = item
    req = urllib.request.Request(src, headers={"User-Agent": UA,
                                              "Accept-Encoding": "identity"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read()
            return {"src": src, "http": src.startswith("http://"),
                    "ext": os.path.splitext(urllib.parse.urlsplit(src).path)[1].lower(),
                    "bytes": len(data), "status": r.status,
                    "ctype": r.headers.get("Content-Type"),
                    "cache": r.headers.get("Cache-Control"), "pages": pages}
    except Exception as e:
        return {"src": src, "http": src.startswith("http://"),
                "ext": os.path.splitext(urllib.parse.urlsplit(src).path)[1].lower(),
                "bytes": 0, "status": 0, "ctype": None, "cache": None,
                "pages": pages, "error": str(e)}


def main():
    d = json.load(open(os.path.join(ROOT, "work", "audit", "crawl_full.json"),
                       encoding="utf-8"))
    uniq = {}
    for p in d["pages"]:
        pg = p["url"].replace("https://argymaq.kg", "") or "/"
        for i in (p.get("images") or []):
            s = i.get("src") or ""
            if not s or s.startswith("data:"):
                continue
            uniq.setdefault(s, [])
            if pg not in uniq[s]:
                uniq[s].append(pg)
    items = list(uniq.items())
    print("уникальных изображений: %d" % len(items))
    with ThreadPoolExecutor(max_workers=6) as ex:
        rows = list(ex.map(one, items, chunksize=1))
    ok = [r for r in rows if r["bytes"] > 0]
    total = sum(r["bytes"] for r in ok)
    print("скачано: %d / %d" % (len(ok), len(rows)))
    print("суммарный вес: %.1f МБ" % (total / 1048576))
    print("средний: %.0f КБ" % (total / max(1, len(ok)) / 1024))
    print("тяжелее 300 КБ: %d (тяжелее 1 МБ: %d)" % (
        sum(1 for r in ok if r["bytes"] > 307200),
        sum(1 for r in ok if r["bytes"] > 1048576)))
    print("PNG: %d | JPG: %d | без Cache-Control: %d" % (
        sum(1 for r in ok if r["ext"] == ".png"),
        sum(1 for r in ok if r["ext"] == ".jpg"),
        sum(1 for r in ok if not r["cache"])))
    print("\nтоп-15:")
    for r in sorted(ok, key=lambda x: -x["bytes"])[:15]:
        print("  %8.0f КБ  %-7s %s" % (r["bytes"] / 1024, r["ctype"], r["src"][-78:]))
    json.dump({"total_bytes": total, "unique": len(rows),
               "images": sorted(rows, key=lambda x: -x["bytes"])},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\nsaved", OUT)


if __name__ == "__main__":
    main()