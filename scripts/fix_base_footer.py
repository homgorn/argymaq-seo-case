#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Мелкие правки после ребрендинга chrome: Base og:site_name, Footer typo."""
import io

ROOT = r"H:\susa ai 500\argymaq.kg\site\src"

p = ROOT + r"\layouts\Base.astro"
t = io.open(p, encoding="utf-8").read()
t = t.replace('content="Refertur.net" />', 'content="argymaq.kg — аудит" />')
io.open(p, "w", encoding="utf-8", newline="").write(t)

p = ROOT + r"\components\Footer.astro"
t = io.open(p, encoding="utf-8").read()
t = t.replace("само сайт", "сам сайт")
io.open(p, "w", encoding="utf-8", newline="").write(t)

print("done")