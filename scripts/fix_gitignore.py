#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Добавляет исключения для PNG-ассетов опубликованного сайта в docs/."""
import io
import sys

p = r"H:\susa ai 500\argymaq.kg\.gitignore"
t = io.open(p, encoding="utf-8").read()

additions = "!docs/*.png\n!docs/**/*.png"

old_block = "*.png\n!site/public/*.png"

if old_block in t:
    t = t.replace(old_block, old_block + "\n" + additions, 1)
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)
    print("patched .gitignore after the png block")
else:
    t += "\n" + additions + "\n"
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)
    print("appended PNG exceptions to .gitignore")

for i, line in enumerate(t.splitlines(), 1):
    if "png" in line:
        print("%3d: %s" % (i, line))
