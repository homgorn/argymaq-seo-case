#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Финальная проверка собранного сайта: description, JSON-LD, дубли, ссылки."""
import glob
import io
import json
import os
import re

ROOT = r"H:\susa ai 500\argymaq.kg\site\dist"
pages = sorted(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True))

print("страниц:", len(pages))
print()

hdr = ("страница", "title", "desc", "H1", "canon", "og", "ld")
print("%-38s %6s %6s %4s %6s %4s %4s" % hdr)
print("-" * 78)

descs, titles, problems = {}, {}, []

for p in pages:
    rel = "/" + os.path.relpath(p, ROOT).replace("\\", "/")
    if rel.endswith("/index.html"):
        rel = rel[:-10] or "/"
    with io.open(p, encoding="utf-8") as f:
        h = f.read()

    t = re.search(r"(?is)<title>(.*?)</title>", h)
    title = (t.group(1).strip() if t else "")
    d = re.search(r'(?is)<meta\s+name="description"\s+content="(.*?)"', h)
    desc = (d.group(1).strip() if d else "")
    h1s = len(re.findall(r"(?is)<h1[\s>]", h))
    canon = 1 if re.search(r'(?is)rel="canonical"', h) else 0
    og = len(re.findall(r'(?is)property="og:', h))
    ld = len(re.findall(r'(?is)application/ld\+json', h))

    # JSON-LD валиден?
    bad_ld = 0
    for m in re.finditer(r'(?is)<script[^>]+application/ld\+json[^>]*>(.*?)</script>', h):
        try:
            json.loads(m.group(1).strip())
        except Exception:
            bad_ld += 1
            problems.append("битый JSON-LD: %s" % rel)

    print("%-38s %6d %6d %4d %6d %4d %4d" % (
        rel[:38], len(title), len(desc), h1s, canon, og, ld))

    descs.setdefault(desc, []).append(rel)
    titles.setdefault(title, []).append(rel)

    if len(desc) < 80:
        problems.append("description короткий (%d): %s" % (len(desc), rel))
    if len(title) < 10:
        problems.append("title короткий (%d): %s" % (len(title), rel))
    if h1s != 1:
        problems.append("H1 = %d: %s" % (h1s, rel))
    if not canon:
        problems.append("нет canonical: %s" % rel)
    if og < 3:
        problems.append("мало og-тегов (%d): %s" % (og, rel))
    if ld == 0:
        problems.append("нет JSON-LD: %s" % rel)

print()
dups = {k: v for k, v in descs.items() if len(v) > 1 and k}
if dups:
    print("ДУБЛИ DESCRIPTION:")
    for k, v in dups.items():
        print("  %s -> %s" % (k[:70], ", ".join(v)))
else:
    print("дублей description нет")

dupt = {k: v for k, v in titles.items() if len(v) > 1 and k}
if dupt:
    print("ДУБЛИ TITLE:")
    for k, v in dupt.items():
        print("  %s -> %s" % (k[:70], ", ".join(v)))
else:
    print("дублей title нет")

print()
if problems:
    print("ПРОБЛЕМЫ (%d):" % len(problems))
    for x in problems:
        print("  -", x)
else:
    print("проблем нет")