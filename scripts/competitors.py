#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка SEO-базы сайтов-конкурентов по нише «конные туры Каракол».

Для каждого конкурента снимает: title/description/H1, наличие JSON-LD и
типы разметки, счётчики аналитики, hreflang, скорость ответа, размер HTML,
число внутренних ссылок и картинок, наличие цен на странице.
Результат: research/raw/competitors.json + таблица в stdout.
"""
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
OUT = r"H:\susa ai 500\argymaq.kg\research\raw\competitors.json"

TARGETS = [
    ("destinationkarakol (RU)", "https://destinationkarakol.com/ru/tury/konnie-tury/"),
    ("destinationkarakol (EN)", "https://destinationkarakol.com/tours/horseback-riding"),
    ("visitkarakol", "https://visitkarakol.com/horse_riding_in_celestrial_mountains"),
    ("hikingkyrgyzstan 1-day", "https://hikingkyrgyzstan.com/one-day-horseback-riding-from-karakol"),
    ("silkwaytrips Karakol gorge", "https://silkwaytrips.com/kyrgyzstan/tours/horseback-riding-in-karakol-gorge-and-hot-springs"),
    ("CBT Karakol Altyn-Arashan", "https://cbtkarakol.com/tours/t/Horseback%20riding/horseback-riding-tour-altyn-arashan"),
    ("horseridingtourchabandes", "https://horseridingtourchabandes.com"),
    ("karakol.kg конный тур", "https://www.karakol.kg/horseback-riding-tour-from-jety-oguz-to-altyn-arashan.html"),
]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._t = False
        self.metas = {}
        self.h1 = []
        self._h1 = False
        self.buf = []
        self.ld = []
        self._ld = None
        self._skip = 0
        self.links = []
        self.img = 0
        self.img_noalt = 0
        self.pcount = 0
        self.text_all = 0
        self.text = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "noscript"):
            self._skip += 1
            if tag == "script" and "ld+json" in (a.get("type") or ""):
                self._ld = []
            return
        if self._skip:
            return
        if tag == "title":
            self._t = True
        elif tag == "meta":
            n = (a.get("name") or a.get("property") or "").lower()
            if n:
                self.metas[n] = a.get("content") or ""
        elif tag == "h1":
            self._h1 = True
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "img":
            self.img += 1
            if not (a.get("alt") or "").strip():
                self.img_noalt += 1
        elif tag == "p":
            self.buf = []
            self._inp = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            if self._skip:
                self._skip -= 1
            if tag == "script" and self._ld is not None:
                self.ld.append("".join(self._ld))
                self._ld = None
            return
        if tag == "title":
            self._t = False
        elif tag == "h1":
            self._h1 = False
        elif tag == "p":
            self.pcount += 1
            t = " ".join("".join(self.buf).split())
            if len(t) > 30:
                self.text.append(t)
            self.text_all += len(t)
            self.buf = []

    def handle_data(self, d):
        if self._ld is not None:
            self._ld.append(d)
            return
        if self._skip:
            return
        if self._t:
            self.title += d
        if self._h1:
            self.buf.append(d)
        if self.buf is not None and self._is_p:
            self.buf.append(d)


P._is_p = False


def ldtypes(buf):
    ts, errs = [], 0
    for b in buf:
        try:
            d = json.loads(b)
        except Exception:
            errs += 1
            continue
        st = [d]
        while st:
            n = st.pop()
            if isinstance(n, dict):
                t = n.get("@type")
                if isinstance(n, str):
                    ts.append(t)
                elif isinstance(n, list):
                    ts.extend(map(str, t))
                st.extend(n.values())
            elif isinstance(n, list):
                st.extend(n)
    return sorted(set(ts)), errs


def grab(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept-Language": "ru,en;q=0.9",
        "Accept": "text/html,*/*;q=0.8", "Accept-Encoding": "identity"})
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=35) as r:
            body = r.read(3 * 1024 * 1024)
            el = round(time.monotonic() - t0, 3)
            h = r.read(0)
            return {"status": r.status, "headers": dict(r.headers), "body": body, "elapsed": el}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "headers": dict(e.headers or {}), "body": b"",
                "elapsed": round(time.monotonic() - t0, 3)}
    except Exception as e:
        return {"status": 0, "headers": {}, "body": b"", "elapsed": 0, "error": str(e)}


def main():
    out = []
    for name, url in TARGETS:
        r = grab(url)
        if not r["body"]:
            out.append({"name": name, "url": url, "status": r["status"],
                        "error": r.get("error", "no body")})
            print("%-32s FAIL %s" % (name, r["status"]))
            continue
        html = r["body"].decode("utf-8", "replace")
        p = P()
        try:
            p.feed(html)
            p.close()
        except Exception:
            pass
        types, errs = ldtypes(p.ld)
        host = urllib.parse.urlsplit(url).netloc
        internal = [l for l in p.links if host.replace("www.", "") in l or l.startswith("/")]
        rec = {
            "name": name, "url": url, "status": r["status"], "elapsed": r["elapsed"],
            "html_bytes": len(r["body"]),
            "title": " ".join(p.title.split())[:160],
            "title_len": len(" ".join(p.title.split())),
            "description": (p.metas.get("description") or "")[:250],
            "desc_len": len(p.metas.get("description") or ""),
            "h1": [x for x in p.h1][:3],
            "h1_count": len(p.h1),
            "lang": "",
            "ldjson": types, "ldjson_broken": errs,
            "metrika": "mc.yandex.ru" in html,
            "gtm": "googletagmanager.com" in html or "gtag(" in html,
            "hreflang": len(re.findall(r'hreflang=', html)),
            "og": len(re.findall(r'property=["\']og:', html)),
            "viewport": bool(re.search(r'name=["\']viewport["\']', html)),
            "img": p.img, "img_noalt": p.img_noalt,
            "internal_links": len(internal),
            "currency_mention": bool(re.search(r"( сом|KGS|USD|\$|€|руб)", html)),
            "prices_found": re.findall(r"(?:от\s*)?\$?\d[\d\s,.]{1,8}\s?(?: сом|KGS|USD|usd|\$|€)", html)[:8],
            "text_blocks": p.pcount,
            "text_chars": p.text_all,
        }
        m = re.search(r'(?is)<html[^>]+lang=["\']([^"\']+)', html)
        rec["lang"] = m.group(1) if m else ""
        out.append(rec)
        print("%-32s %3s %6sms %7sB  T=%-3s D=%-3s H1=%-2s LD=%-28s prices=%s" % (
            name[:32], rec["status"], int(rec["elapsed"] * 1000), rec["html_bytes"],
            rec["title_len"], rec["desc_len"], rec["h1_count"],
            ",".join(types)[:28] or "-",
            "Y" if rec["currency_mention"] else "N"))
        time.sleep(0.5)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"fetched": time.strftime("%Y-%m-%d %H:%M"), "targets": out},
                  f, ensure_ascii=False, indent=1)
    print("\nsaved", OUT)


if __name__ == "__main__":
    main()