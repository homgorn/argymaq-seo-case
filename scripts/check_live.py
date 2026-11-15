#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка живого сайта Refertur (homgorn.github.io/argymaq-seo-case)."""
import re
import sys
import urllib.error
import urllib.request

BASE = "https://homgorn.github.io/argymaq-seo-case"
PATHS = [
    "/", "/audit/", "/plan/", "/work/", "/result/",
]
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

ok, bad = 0, []
print("%-12s %5s %6s %4s %5s %5s" % ("маршрут", "код", "байт", "H1", "LD", "og"))
print("-" * 50)

for path in PATHS:
    url = BASE + path
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read()
            status = r.status
    except urllib.error.HTTPError as e:
        print("%-12s %5s  ОШИБКА" % (path, e.code))
        bad.append((path, "HTTP %s" % e.code))
        continue
    except Exception as e:
        print("%-12s %5s  %s" % (path, "-", e))
        bad.append((path, str(e)))
        continue

    h = body.decode("utf-8", "replace")
    h1 = len(re.findall(r"(?is)<h1[\s>]", h))
    ld = len(re.findall(r"(?is)application/ld\+json", h))
    og = len(re.findall(r'(?is)property="og:', h))
    mark = "ok" if (h1 == 1 and ld > 0 and og >= 3) else "!!"
    if mark == "!!":
        bad.append((path, "H1=%d LD=%d OG=%d" % (h1, ld, og)))
    else:
        ok += 1
    print("%-12s %5s %6d %4d %5d %5d  %s" % (
        path, status, len(body), h1, ld, og, mark))

print()
print("годных: %d из %d" % (ok, len(PATHS)))
if bad:
    print("проблемы:")
    for p, why in bad:
        print("  -", p, "->", why)
else:
    print("все маршруты в порядке")