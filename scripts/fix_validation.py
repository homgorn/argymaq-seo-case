#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Правки по итогам валидации: длинные description + JSON-LD на страницах.

Ничего не удаляет: только заменяет конкретные строки.
"""
import io
import os
import re
import sys

ROOT = r"H:\susa ai 500\argymaq.kg\site\src\pages"


def read(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()


def write(p, t):
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)
    print("  written:", p.replace(ROOT, "src/pages"))


def sub(t, old, new, label):
    if old in t:
        print("  ok:", label)
        return t.replace(old, new, 1)
    print("  MISS:", label)
    return t


# ── 1. uslugi/[slug].astro — удлиняем description ──────────────────
p = os.path.join(ROOT, "uslugi", "[slug].astro")
t = read(p)
t = sub(
    t,
    "const description = service.lead;",
    "const description =\n"
    "  `${service.lead} ${service.includes.length} пунктов работы, от ${fmt} ${service.priceUnit}. ` +\n"
    "  `Что входит, сроки и как заказать — на странице услуги.`;",
    "uslugi/[slug] description",
)
write(p, t)

# ── 2. uslugi/index.astro — description + JSON-LD ──────────────────
p = os.path.join(ROOT, "uslugi", "index.astro")
t = read(p)
t = sub(
    t,
    "const description =\n  'Шесть направлений: SEO, продвижение в нейросетях, карты (Яндекс, 2GIS, Google), SMM, сайты и реклама. Для бизнеса в Кыргызстане.';",
    "const description =\n"
    "  'Шесть направлений для бизнеса в Кыргызстане: SEO и продвижение в поиске, продвижение в нейросетях, ' +\n"
    "  'карты Яндекс и 2GIS, SMM, сайты под ключ и реклама. Цены в сомах, от 15 000 в месяц.';",
    "uslugi/index description",
)
if "const jsonLd" not in t:
    t = sub(
        t,
        "---\n\n<Base",
        "const jsonLd = {\n"
        "  '@context': 'https://schema.org',\n"
        "  '@type': 'ItemList',\n"
        "  name: 'Услуги Digital Growth KG',\n"
        "  itemListElement: services.map((s, i) => ({\n"
        "    '@type': 'ListItem',\n"
        "    position: i + 1,\n"
        "    item: {\n"
        "      '@type': 'Service',\n"
        "      name: s.title,\n"
        "      description: s.lead,\n"
        "      url: `${site.brand.url}/uslugi/${s.slug}/`,\n"
        "    },\n"
        "  })),\n"
        "};\n"
        "---\n\n<Base",
        "uslugi/index jsonLd",
    )
    t = sub(t, "<Base title={title} description={description}>",
            "<Base title={title} description={description} jsonLd={jsonLd}>",
            "uslugi/index jsonLd prop")
t = sub(t,
        "import services from '../../data/services.json';",
        "import services from '../../data/services.json';\nimport site from '../../data/site.json';",
        "uslugi/index site import")
write(p, t)

# ── 3. kak-rabotaem.astro — description + JSON-LD ──────────────────
p = os.path.join(ROOT, "kak-rabotaem.astro")
t = read(p)
t = sub(
    t,
    "const description =\n  'Пять шагов: бриф, аудит, план, работа, отчёт. Вы всегда знаете, что происходит и что дальше. Без воды.';",
    "const description =\n"
    "  'Пять шагов работы: бриф, аудит, план, внедрение и отчёт. Вы всегда знаете, на каком этапе проект, ' +\n"
    "  'что от вас нужно и что будет дальше. Без воды и скрытых доплат.';",
    "kak-rabotaem description",
)
if "const jsonLd" not in t:
    t = sub(
        t,
        "---\n\n<Base",
        "const jsonLd = {\n"
        "  '@context': 'https://schema.org',\n"
        "  '@type': 'HowTo',\n"
        "  name: 'Как мы работаем',\n"
        "  description,\n"
        "  step: process.map((p, i) => ({\n"
        "    '@type': 'HowToStep',\n"
        "    position: i + 1,\n"
        "    name: p.title,\n"
        "    text: p.text,\n"
        "  })),\n"
        "};\n"
        "---\n\n<Base",
        "kak-rabotaem jsonLd",
    )
    t = sub(t, "<Base title={title} description={description}>",
            "<Base title={title} description={description} jsonLd={jsonLd}>",
            "kak-rabotaem jsonLd prop")
write(p, t)

# ── 4. about.astro — JSON-LD ───────────────────────────────────────
p = os.path.join(ROOT, "about.astro")
t = read(p)
if "const jsonLd" not in t:
    t = sub(
        t,
        "---\n\n<Base",
        "const jsonLd = {\n"
        "  '@context': 'https://schema.org',\n"
        "  '@type': 'AboutPage',\n"
        "  name: title,\n"
        "  description,\n"
        "  mainEntity: {\n"
        "    '@type': 'Organization',\n"
        "    name: site.brand.name,\n"
        "    url: site.brand.url,\n"
        "    email: site.contacts.email,\n"
        "    telephone: site.contacts.whatsapp,\n"
        "  },\n"
        "};\n"
        "---\n\n<Base",
        "about jsonLd",
    )
    t = sub(t, "<Base title={title} description={description}>",
            "<Base title={title} description={description} jsonLd={jsonLd}>",
            "about jsonLd prop")
write(p, t)

# ── 5. kase/plan.astro — JSON-LD ───────────────────────────────────
p = os.path.join(ROOT, "kase", "argymaq-kg", "plan.astro")
t = read(p)
if "const jsonLd" not in t:
    t = sub(
        t,
        "---\n\n<Base",
        "const jsonLd = {\n"
        "  '@context': 'https://schema.org',\n"
        "  '@type': 'Article',\n"
        "  headline: title,\n"
        "  description,\n"
        "  about: { '@type': 'Organization', name: 'ARGYMAQ KYRGYZSTAN' },\n"
        "};\n"
        "---\n\n<Base",
        "plan jsonLd",
    )
    t = sub(t, "<Base title={title} description={description}>",
            "<Base title={title} description={description} jsonLd={jsonLd}>",
            "plan jsonLd prop")
write(p, t)

# ── 6. kase/work.astro — JSON-LD ───────────────────────────────────
p = os.path.join(ROOT, "kase", "argymaq-kg", "work.astro")
t = read(p)
if "const jsonLd" not in t:
    t = sub(
        t,
        "---\n\n<Base",
        "const jsonLd = {\n"
        "  '@context': 'https://schema.org',\n"
        "  '@type': 'Article',\n"
        "  headline: title,\n"
        "  description,\n"
        "  about: { '@type': 'Organization', name: 'ARGYMAQ KYRGYZSTAN' },\n"
        "};\n"
        "---\n\n<Base",
        "work jsonLd",
    )
    t = sub(t, "<Base title={title} description={description}>",
            "<Base title={title} description={description} jsonLd={jsonLd}>",
            "work jsonLd prop")
write(p, t)

print("\ndone")