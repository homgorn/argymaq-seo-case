#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Добавляет блок «Источники данных» в главную страницу отчёта."""
import io
import sys

p = r"H:\susa ai 500\argymaq.kg\site\src\pages\index.astro"
t = io.open(p, encoding="utf-8").read()

block = """
  <!-- ИСТОЧНИКИ -->
  <section class="wrap pb-10">
    <div class="box">
      <div class="box-tag">Источники данных</div>
      <div class="grid gap-4 sm:grid-cols-2" style="font-size:13.5px; line-height:1.6;">
        <div>
          <div class="text-[11px] uppercase tracking-[.08em] font-semibold" style="color:var(--color-muted); margin-bottom:6px;">Измерено мной · 14–15.11.2026</div>
          <ul style="margin:0; padding-left:18px;">
            <li><a href="https://argymaq.kg/" target="_blank" rel="noopener" class="src-link">argymaq.kg</a> — главная, заголовки, размер HTML</li>
            <li><a href="https://argymaq.kg/our-tours/" target="_blank" rel="noopener" class="src-link">argymaq.kg/our-tours/</a> — структура каталога</li>
            <li><a href="https://argymaq.kg/robots.txt" target="_blank" rel="noopener" class="src-link">robots.txt</a> · <a href="https://argymaq.kg/wp-sitemap.xml" target="_blank" rel="noopener" class="src-link">wp-sitemap.xml</a></li>
            <li>Веса изображений — HEAD-запросы к 54 файлам в медиатеке</li>
          </ul>
        </div>
        <div>
          <div class="text-[11px] uppercase tracking-[.08em] font-semibold" style="color:var(--color-muted); margin-bottom:6px;">Сравнение с рынком · 14.11.2026</div>
          <ul style="margin:0; padding-left:18px;">
            <li><a href="https://destinationkarakol.com/tours/horseback-riding" target="_blank" rel="noopener" class="src-link">destinationkarakol.com</a></li>
            <li><a href="https://hikingkyrgyzstan.com/one-day-horseback-riding-from-karakol" target="_blank" rel="noopener" class="src-link">hikingkyrgyzstan.com</a></li>
            <li><a href="https://silkwaytrips.com/kyrgyzstan/tours/horseback-riding-in-karakol-gorge-and-hot-springs" target="_blank" rel="noopener" class="src-link">silkwaytrips.com</a></li>
            <li><a href="https://cbtkarakol.com/" target="_blank" rel="noopener" class="src-link">cbtkarakol.com</a></li>
          </ul>
        </div>
      </div>
    </div>
  </section>

"""

anchor = "  <!-- ДИСКЛЕЙМЕР -->"
if anchor in t:
    t = t.replace(anchor, block + anchor, 1)
    print("block inserted")
else:
    print("anchor NOT found")
    sys.exit(1)

css = "  .src-link {\n    color: var(--color-accent);\n    text-decoration: none;\n    border-bottom: 1px dotted var(--color-accent);\n  }\n  .src-link:hover {\n    text-decoration: none;\n    border-bottom-style: solid;\n  }\n"
if "  .src-link {" not in t:
    t = t.replace("</style>", css + "</style>", 1)
    print("css added")
else:
    print("css already present")

io.open(p, "w", encoding="utf-8", newline="").write(t)
print("saved", p)