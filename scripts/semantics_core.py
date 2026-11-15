#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Семантическое ядро argymaq.kg (Черновик, регион — Каракол).

Источники частотности: поисковые подсказки (Google/Bing suggest API),
Wordstat-подобные данные недоступны без ключей — объём помечен как
NULL и требует подтверждения в панели. Задача скрипта — собрать
структуру спроса, кластеры и целевые страницы.

Результат: data/keywords.json + таблица keywords в data/seo.db
"""
import json
import os
import sqlite3
import time
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
ROOT = r"H:\susa ai 500\argymaq.kg"
DB = os.path.join(ROOT, "data", "seo.db")
OUT = os.path.join(ROOT, "data", "keywords.json")


def suggest(q, lang="en"):
    url = ("https://suggestqueries.google.com/complete/search?client=firefox&hl=%s&q=%s"
           % (lang, urllib.parse.quote(q)))
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode("utf-8", "replace"))
            return data[1] if len(data) > 1 else []
    except Exception:
        return []


# --- ядро: кластеры, намерения, целевые страницы
CORE = [
    # cluster, phrase, intent, target page
    ("коммерческие — общие", "horse riding karakol", "commercial", "/"),
    ("коммерческие — общие", "horseback riding karakol", "commercial", "/"),
    ("коммерческие — общие", "horseback riding tours kyrgyzstan", "commercial", "/"),
    ("коммерческие — общие", "конные туры каракол", "commercial", "/"),
    ("коммерческие — общие", "конные прогулки каракол", "commercial", "/"),
    ("коммерческие — общие", "верхом на лошади каракол", "commercial", "/"),
    ("коммерческие — туры", "horse riding tour karakol kyrgyzstan", "commercial", "/our-tours/"),
    ("коммерческие — туры", "kyrgyzstan horseback tour 3 days", "commercial", "/our-tours/"),
    ("коммерческие — туры", "horse riding tour ala kol lake", "commercial",
     "/4-day-horseback-riding-tour-program/"),
    ("коммерческие — туры", "horse riding ala kul", "commercial",
     "/4-day-horseback-riding-tour-program/"),
    ("коммерческие — туры", " horseback riding ala-kul lake tour", "commercial",
     "/4-day-horseback-riding-tour-program/"),
    ("коммерческие — туры", " horseback riding tour kyrgyzstan price", "commercial", "/our-tours/"),
    ("коммерческие — туры", " horseback riding tour kyrgyzstan price", "commercial", "/our-tours/"),
    ("коммерческие — туры", " horse riding tour kyrgyzstan price", "commercial", "/our-tours/"),
    ("коммерческие — туры", " one day horse riding tour karakol gorge", "commercial",
     "/1-day-horseback-riding-tour-in-karakol-gorge/"),
    ("коммерческие — туры", " horse riding tour karakol gorge", "commercial",
     "/1-day-horseback-riding-tour-in-karakol-gorge/"),
    ("коммерческие — туры", " two day horse riding tour altyn arashan", "commercial",
     "/2-day-horseback-riding-itinerary-altyn-arashan/"),
    ("коммерческие — туры", " horse riding tour altyn arashan", "commercial",
     "/2-day-horseback-riding-itinerary-altyn-arashan/"),
    ("коммерческие — туры", " five day horse riding tour kyrgyzstan", "commercial",
     "/5-day-horseback-riding-tour-program/"),
    ("коммерческие — размещение", " guesthouse karakol", "commercial",
     "/guesthouse-and-yurt-camp/"),
    ("коммерческие — размещение", " yurt camp karakol", "commercial",
     "/guesthouse-and-yurt-camp/"),
    ("коммерческие — размещение", " yurt stay karakol kyrgyzstan", "commercial",
     "/guesthouse-and-yurt-camp/"),
    ("коммерческие — размещение", " karakol hostel", "commercial",
     "/guesthouse-and-yurt-camp/"),
    ("коммерческие — трансфер", " airport pickup karakol", "commercial",
     "/airport-pickup/"),
    ("коммерческие — трансфер", " airport transfer karakol from bishkek", "commercial",
     "/airport-pickup/"),
    ("коммерческие — трансфер", " transfer tamchy to karakol", "commercial",
     "/airport-pickup/"),
    ("информационные", " things to do in karakol", "informational", "/blog/"),
    ("информационные", " karakol horse riding", "informational", "/blog/"),
    ("информационные", " altyn arashan hot springs", "informational", "/blog/"),
    ("информационные", " ala kul lake trek", "informational", "/blog/"),
    ("информационные", " karakol gorge hike", "informational", "/blog/"),
    ("информационные", " best time to visit karakol", "informational", "/blog/"),
    ("информационные", " kyrgyzstan horse riding experience", "informational", "/blog/"),
    ("информационные", " horseback riding season kyrgyzstan", "informational", "/blog/"),
    ("бренд", " argymaq", "brand", "/"),
    ("бренд", " argymaq kyrgyzstan", "brand", "/"),
    ("бренд", " аргимак каракол", "brand", "/"),
    ("бренд", " argymaq horseback", "brand", "/"),
    ("бренд", " argymaq tours", "brand", "/"),
]


def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("select coalesce(max(id),0)+1 from audit_run")
    run_id = cur.execute("select id from audit_run order by id desc limit 1").fetchone()[0]

    rows = []
    seen = set()
    for cluster, phrase, intent, page in CORE:
        p = phrase.strip()
        key = p.lower()
        if not p or key in seen:
            continue
        seen.add(key)
        sug = suggest(p, "en") + suggest(p, "ru")
        rows.append({"cluster": cluster, "phrase": p, "intent": intent,
                     "target": page, "suggest": sug[:8],
                     "volume": None, "note": "объём подтвердить в Wordstat/GKP"})

    cur.execute("delete from keywords where run_id=?", (run_id,))
    for r in rows:
        cur.execute("""insert into keywords(run_id,phrase,intent,volume,source,target_page,cluster,note)
                       values(?,?,?,?,?,?,?,?)""",
                    (run_id, r["phrase"], r["intent"], r["volume"],
                     "suggest: " + "; ".join(r["suggest"]), r["target"],
                     r["cluster"], r["note"]))
    con.commit()
    json.dump({"run_id": run_id, "count": len(rows),
               "fetched": time.strftime("%Y-%m-%d %H:%M"),
               "keywords": rows},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    print("ключей в ядре: %d" % len(rows))
    print("кластеры:")
    cl = {}
    for r in rows:
        cl.setdefault(r["cluster"], []).append(r["phrase"])
    for c, ps in cl.items():
        print("  %-28s %d" % (c, len(ps)))
        for p in ps:
            print("      - %s" % p)
    print("\nподсказки, которые стоит проверить (пример):")
    for r in rows[:6]:
        if r["suggest"]:
            print("  %s -> %s" % (r["phrase"], ", ".join(r["suggest"][:5])))
    print("\nsaved", OUT)
    con.close()


if __name__ == "__main__":
    main()