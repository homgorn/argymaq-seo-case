#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Перенос страниц кейса из pages/kase/argymaq-kg/ в корень и замена ссылок."""
import io
import os
import shutil
import sys

ROOT = r"H:\susa ai 500\argymaq.kg\site\src\pages"

PAIR = [
    ("kase/argymaq-kg/audit.astro", "audit.astro"),
    ("kase/argymaq-kg/plan.astro", "plan.astro"),
    ("kase/argymaq-kg/work.astro", "work.astro"),
    ("kase/argymaq-kg/result.astro", "result.astro"),
    ("kase/argymaq-kg/index.astro", "case.astro"),
]

for src, dst in PAIR:
    s = os.path.join(ROOT, src)
    d = os.path.join(ROOT, dst)
    if os.path.exists(s):
        shutil.move(s, d)
        print("moved", src, "->", dst)
    else:
        print("MISSING", src)

# удаляем оставшийся каталог kase
for root, dirs, files in os.walk(os.path.join(ROOT, "kase")):
    for f in files:
        print("REMOVE:", os.path.join(root, f))

REPLACEMENTS = [
    ("from '../../../layouts/", "from '../layouts/"),
    ("from '../../../components/", "from '../components/"),
    ("from '../../../data/", "from '../data/"),
    ("/kase/argymaq-kg/audit/", "/audit/"),
    ("/kase/argymaq-kg/plan/", "/plan/"),
    ("/kase/argymaq-kg/work/", "/work/"),
    ("/kase/argymaq-kg/result/", "/result/"),
    ("/kase/argymaq-kg/", "/"),
]

for root, dirs, files in os.walk(ROOT):
    for f in files:
        if not f.endswith(".astro"):
            continue
        p = os.path.join(root, f)
        t = io.open(p, encoding="utf-8").read()
        orig = t
        for old, new in REPLACEMENTS:
            t = t.replace(old, new)
        if t != orig:
            with io.open(p, "w", encoding="utf-8", newline="") as fh:
                fh.write(t)
            print("updated", os.path.relpath(p, ROOT))

# удаляем kase целиком
shutil.rmtree(os.path.join(ROOT, "kase"), ignore_errors=True)
print("done")