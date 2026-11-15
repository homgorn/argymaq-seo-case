#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Чинит структуру README: рамки в блоках кода и стрелки, пострадавшие от кодировки."""
import io
import re

p = r"H:\susa ai 500\argymaq.kg\README.md"
t = io.open(p, encoding="utf-8").read()

# 1. Заменяем битые символы рамок (U+FFFD и подобные) внутри code fences
def fix_tree(block):
    lines = block.split("\n")
    out = []
    depth_map = {
        "site/": "", "docs/": "", "scripts/": "", "research/": "", "data/": "",
    }
    for ln in lines:
        # определяем отступ по αρχному символу
        m = re.match(r'^([^\w]*)(.*)$', ln)
        prefix = m.group(1) if m else ""
        if prefix and set(prefix) <= set("\u2502\u251c\u2514\u2500\u2003 \ufffd?") and any(c in prefix for c in "\ufffd?"):
            # заменяем мусор на правильные символы по длине
            clean = re.sub(r'[^\s]', '', prefix) or ""
            new_prefix = ""
            for ch in prefix:
                new_prefix += " "  # упрощаем: делаем отступ пробелами
            ln = new_prefix + ln[len(prefix):]
        out.append(ln)
    return "\n".join(out)

# проще: заменить все code-блоки с деревом на чистые ASCII-деревья
new_tree = """```
argymaq-seo-case/
|-- site/                   the static report website (Astro 5 + Tailwind 4)
|   |-- src/pages/          17 routes
|   |-- src/components/     MetricCard, BeforeAfter, Phase, PriceCard, Steps
|   |-- src/data/           services, packages, case data as JSON
|   `-- dist/               built output (git-ignored)
|-- docs/
|   |-- architecture/       site architecture and design system
|   |-- reports/            the audit report for the owner (RU + EN)
|   |-- research/           market prices, reporting patterns, GEO, local maps
|   `-- wiki/               multi-level LLM wiki of every finding
|-- scripts/                11 Python scripts that reproduce the audit
|-- research/               raw competitor data and benchmark
`-- data/                   SQLite knowledge base + JSONL export
```"""

t = re.sub(r"```\s*\nargymaq-seo-case/\n.*?\n```", new_tree, t, flags=re.S)

# 2. Стрелка, пострадавшая от кодировки
t = t.replace("**before \u00c2 after**", "**before \u2192 after**")
t = t.replace("**before  after**", "**before \u2192 after**")
t = re.sub(r"\*\*before[^A-Za-z]{0,4}after\*\*", "**before \u2192 after**", t)

io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("fixed README.md")
print()
print(t[t.index("## What is inside"):t.index("## Quick start")])