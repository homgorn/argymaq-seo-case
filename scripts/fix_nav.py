#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Header и Footer: все внутренние ссылки темы base path."""
import io
import re

ROOT = r"H:\susa ai 500\argymaq.kg\site\src\components"

# Header
p = ROOT + r"\Header.astro"
t = io.open(p, encoding="utf-8").read()
t = t.replace("const nav = [\n  { label: 'Аудит', href: '/audit/' },\n  { label: 'План', href: '/plan/' },\n  { label: 'Что сделали', href: '/work/' },\n  { label: 'Результат', href: '/result/' },\n];\nconst base = import.meta.env.BASE_URL.replace(/\\/$/, '');",
"""const base = import.meta.env.BASE_URL.replace(/\\/$/, '');
const link = (p) => `${base}${p}`;

const nav = [
  { label: 'Аудит', href: link('/audit/') },
  { label: 'План', href: link('/plan/') },
  { label: 'Что сделали', href: link('/work/') },
  { label: 'Результат', href: link('/result/') },
];""")
io.open(p, "w", encoding="utf-8", newline="").write(t)
print("header done")

# Footer — то же самое
p = ROOT + r"\Footer.astro"
t = io.open(p, encoding="utf-8").read()
t = t.replace("const nav = [\n  { label: 'Аудит', href: '/audit/' },\n  { label: 'План', href: '/plan/' },\n  { label: 'Что сделали', href: '/work/' },\n  { label: 'Результат', href: '/result/' },\n];\nconst base = import.meta.env.BASE_URL.replace(/\\/$/, '');",
"""const base = import.meta.env.BASE_URL.replace(/\\/$/, '');
const link = (p) => `${base}${p}`;

const nav = [
  { label: 'Аудит', href: link('/audit/') },
  { label: 'План', href: link('/plan/') },
  { label: 'Что сделали', href: link('/work/') },
  { label: 'Результат', href: link('/result/') },
];""")
# Если base в Footer ещё не добавлен, добавляем перед <footer> / после импорта данных
if "const base = import.meta.env.BASE_URL" not in t:
    t = t.replace("const nav = [",
                  "const base = import.meta.env.BASE_URL.replace(/\\/$/, '');\nconst link = (p) => `${base}${p}`;\nconst nav = [", 1)
    t = t.replace("href: '/audit/' },", "href: link('/audit/') },")
    t = t.replace("href: '/plan/' },", "href: link('/plan/') },")
    t = t.replace("href: '/work/' },", "href: link('/work/') },")
    t = t.replace("href: '/result/' },", "href: link('/result/') },")
io.open(p, "w", encoding="utf-8", newline="").write(t)
print("footer done")

for name in ("Header.astro", "Footer.astro"):
    p = ROOT + "\\" + name
    print("=" * 40, name)
    print(io.open(p, encoding="utf-8").read()[:800])