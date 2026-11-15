#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Обновляет Footer: добавляет адрес и ссылки на карты."""
import io

PATH = r"H:\susa ai 500\argymaq.kg\site\src\components\Footer.astro"

old = """      <div class="flex flex-col gap-2 text-[13.5px]">
        <a
          href={site.contacts.whatsappLink}
          target="_blank"
          rel="noopener"
          class="contact-chip"
        >
          <span aria-hidden="true">💬</span> {site.contacts.whatsapp}
        </a>
        <a href={`mailto:${site.contacts.email}`} class="contact-chip">
          <span aria-hidden="true">✉️</span> {site.contacts.email}
        </a>
        <a
          href={site.contacts.telegramLink}
          target="_blank"
          rel="noopener"
          class="contact-chip"
        >
          <span aria-hidden="true">➤</span> {site.contacts.telegram}
        </a>
      </div>"""

new = """      <div class="flex flex-col gap-2 text-[13.5px]">
        <a
          href={site.contacts.whatsappLink}
          target="_blank"
          rel="noopener"
          class="contact-chip"
        >
          <span aria-hidden="true">💬</span> {site.contacts.whatsapp}
        </a>
        <a href={`mailto:${site.contacts.email}`} class="contact-chip">
          <span aria-hidden="true">✉️</span> {site.contacts.email}
        </a>
        <a
          href={site.contacts.telegramLink}
          target="_blank"
          rel="noopener"
          class="contact-chip"
        >
          <span aria-hidden="true">➤</span> {site.contacts.telegram}
        </a>
      </div>

      <div class="flex flex-col gap-1.5 text-[12.5px]" style="color: var(--color-muted);">
        <span class="font-semibold" style="color: var(--color-fg);">Адрес</span>
        <p style="margin: 0; max-width: 220px; line-height: 1.5;">{site.contacts.address}</p>
        <div class="flex flex-wrap gap-x-4 gap-y-1 pt-1">
          <a href={site.contacts.mapGoogle} target="_blank" rel="noopener" class="map-link">Google Maps</a>
          <a href={site.contacts.map2gis} target="_blank" rel="noopener" class="map-link">2GIS</a>
          <a href={site.contacts.mapYandex} target="_blank" rel="noopener" class="map-link">Яндекс Карты</a>
        </div>
      </div>"""

with io.open(PATH, encoding="utf-8") as f:
    t = f.read()
if old in t:
    t = t.replace(old, new, 1)
    print("contacts block updated")
else:
    print("PATTERN NOT FOUND")

css_old = """  .contact-chip:hover {
    border-color: var(--color-ok);
    color: var(--color-ok);
    transform: translateY(-1px);
  }
</style>"""
css_new = """  .contact-chip:hover {
    border-color: var(--color-ok);
    color: var(--color-ok);
    transform: translateY(-1px);
  }
  .map-link {
    color: var(--color-muted);
    text-decoration: none;
    border-bottom: 1px dotted var(--color-muted);
    transition: all 0.16s ease;
    font-size: 12.5px;
  }
  .map-link:hover {
    color: var(--color-accent);
    border-color: var(--color-accent);
  }
</style>"""

if css_old in t:
    t = t.replace(css_old, css_new, 1)
    print("css updated")
else:
    print("CSS PATTERN NOT FOUND")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(t)