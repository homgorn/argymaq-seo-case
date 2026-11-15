#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
p = r"H:\susa ai 500\argymaq.kg\site\src\pages\index.astro"
t = io.open(p, encoding="utf-8").read()
before = t.count("</span></span>")
t = t.replace("</span></span>", "</span>")
io.open(p, "w", encoding="utf-8", newline="").write(t)
print("removed", before, "duplicate closing spans")
print("remaining:", t.count("</span></span>"))