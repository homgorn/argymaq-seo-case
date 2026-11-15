#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Вес изображений argymaq.kg через http.client HEAD (без Range).

Сервер на заголовок Range отвечает 206 с телом в 2 байта, поэтому
Content-Length выглядит как 2. Чистый HEAD даёт настоящий размер.
Результат: work/audit/images_head.json
"""
import http.client
import json
import os
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
ROOT = r"H:\susa ai 500\argymaq.kg"
OUT = os.path.join(ROOT, "work", "audit", "images_head.json")


def head(src):
    u = urllib.parse.urlsplit(src)
    host = u.hostname
    path = u.path + (("?" + u.query) if u.query else "")
    conn_cls = http.client.HTTPSConnection if u.scheme == "https" else http.client.HTTPConnection
    out = {"src": src, "http": u.scheme == "http",
           "ext": os.path.splitext(u.path)[1].lower(),
           "bytes": 0, "status": 0, "ctype": None, "cache": None}
    for attempt in range(3):
        try:
            c = conn_cls(host, timeout=30)
            c.request("HEAD", path, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
            r = c.getresponse()
            r.read()
            out.update(status=r.status, ctype=r.getheader("Content-Type"),
                       cache=r.getheader("Cache-Control"))
            if r.status == 200:
                out["bytes"] = int(r.getheader("Content-Length") or 0)
                c.close()
                return out
            if r.status in (301, 302, 307, 308):
                loc = r.getheader("Location")
                c.close()
                if loc:
                    src = urllib.parse.urljoin(src, loc)
                    u = urllib.parse.urlsplit(src)
                    host, path = u.hostname, u.path + (("?" + u.query) if u.query else "")
                    conn_cls = (http.client.HTTPSConnection if u.scheme == "https"
                                else http.client.HTTPConnection)
                    continue
            c.close()
            return out
        except Exception as e:
            out["error"] = str(e)
            time.sleep(0.5)
    return out


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
    items = [(s, pages) for s, pages in uniq.items()]
    with ThreadPoolExecutor(max_workers=8) as ex:
        rows = list(ex.map(lambda a: head(a[0]), items))
    for r, (s, pages) in zip(rows, items):
        r["pages"] = pages
    ok = [r for r in rows if r["bytes"] > 0]
    total = sum(r["bytes"] for r in ok)
    per_page = {}
    for r in rows:
        for pg in r["pages"]:
            per_page[pg] = per_page.get(pg, 0) + r["bytes"]
    print("изображений уникальных: %d (размер получен: %d)" % (len(rows), len(ok)))
    print("суммарный вес: %.1f МБ | средний: %.0f КБ" % (
        total / 1048576, total / max(1, len(ok)) / 1024))
    print(">300 КБ: %d | >1 МБ: %d | >5 МБ: %d | >10 МБ: %d" % (
        sum(1 for r in ok if r["bytes"] > 307200),
        sum(1 for r in ok if r["bytes"] > 1048576),
        sum(1 for r in ok if r["bytes"] > 5 * 1048576),
        sum(1 for r in ok if r["bytes"] > 10 * 1048576)))
    print("PNG: %d | JPG: %d | webp/avif: %d" % (
        sum(1 for r in ok if r["ext"] == ".png"),
        sum(1 for r in ok if r["ext"] in (".jpg", ".jpeg")),
        sum(1 for r in ok if r["ext"] in (".webp", ".avif"))))
    print("без Cache-Control: %d" % sum(1 for r in ok if not r["cache"]))
    print("\nВес всех картинок страницы:")
    for pg, b in sorted(per_page.items(), key=lambda kv: -kv[1]):
        print("  %8.1f МБ  %s" % (b / 1048576, pg))
    print("\nТоп-15:")
    for r in sorted(ok, key=lambda x: -x["bytes"])[:15]:
        print("  %8.1f МБ  %-6s %s [%d стр.]" % (
            r["bytes"] / 1048576, r["ext"], r["src"][-66:], len(r["pages"])))
    json.dump({"total_bytes": total, "unique": len(rows), "per_page": per_page,
               "images": sorted(rows, key=lambda x: -x["bytes"])},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\nsaved", OUT)


if __name__ == "__main__":
    main()