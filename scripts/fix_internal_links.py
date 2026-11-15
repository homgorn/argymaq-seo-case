#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Пропускает все .astro файлы: prefixes внутренних ссылок через base из import.meta.env.BASE_URL."""
import io
import os
import re

ROOT = r"H:\susa ai 500\argymaq.kg\site\src"

# В шаблонах Astro: href="/audit/" -> href={`${base}/audit/`}
pat = re.compile(r'href="/([^"]*)"')

def add_base_import(content):
    # вставляем перед закрывающим --- фронта matterа первую попавшуюся строга
    lines = content.splitlines()
    if lines[0].strip() != "---":
        return content, False
    insert_at = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            insert_at = i
            break
    if insert_at is None:
        return content, False
    fm = lines[: insert_at]
    if not any("import.meta.env.BASE_URL" in line for line in fm):
        fm.append("const base = import.meta.env.BASE_URL.replace(/\\/$/, '');")
    return "\n".join(fm + lines[insert_at:]) + ("\n" if content.endswith("\n") else ""), True

for root, dirs, files in os.walk(ROOT):
    for f in files:
        if not f.endswith(".astro"):
            continue
        p = os.path.join(root, f)
        t = io.open(p, encoding="utf-8").read()

        # 1. подстановка base: все внутренние ссылки на один уровень
        def repl(m):
            inner = m.group(1)
            if inner.startswith("http"):
                return m.group(0)
            return "href={`${base}/" + inner + "`}"

        new_t = pat.sub(repl, t)

        # 2. добавление const base
        if new_t != t:
            new_t, changed = add_base_import(new_t)
            if not changed:
                print("WARN: frontmatter not found", p)
                continue
            with io.open(p, "w", encoding="utf-8", newline="") as fh:
                fh.write(new_t)
            print("updated", p)
        else:
            # всё равно проверим, что base задан
            if "import.meta.env.BASE_URL" not in t:
                pass

print("done")