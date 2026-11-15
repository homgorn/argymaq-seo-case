#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Расширенный паук argymaq.kg: полный набор SEO-полей + schema.org в tidy-JSON.

Пишет work/audit/crawl_full.json, work/audit/crawl_index.csv и
research/raw/<slug>.meta.json для каждого URL.
"""
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from html.parser import HTMLParser

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
TIMEOUT = 30
OUT = r"H:\susa ai 500\argymaq.kg\work\audit"
RAW = r"H:\susa ai 500\argymaq.kg\research\raw"
STOP = set("""
и в во не что он на я с со как а то все она так его но да ты к у же вы за бы по только
её ее мне было вот от меня еще нет о из ему теперь когда даже ну вдруг ли если уже или ни
быть был него до вас нибудь опять уж вам сказал ведь там потом себя ничего ей может они тут
где есть надо ней для мы тебя их чем была сам чтоб без будто человек чего раз тоже себе под
жизнь будет ж тогда кто этот говорил того потому этого какой совсем ним здесь этом один почти
мой тем чтобы нее the and for are but not you all any can had her was one our out day get has
him his how man new now old see two way who boy did its let put say she too use với это эта
эти этот также более мыти тур
""".split())


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._t = False
        self.metas = {}
        self.links = []
        self.canonical = None
        self.hreflang = []
        self.h1, self.h2, self.h3 = [], [], []
        self._h = None
        self._buf = []
        self.img = []
        self.ld = []
        self._ld = None
        self._skip = 0
        self.words = Counter()
        self.text_len = 0
        self.scripts = 0
        self.iframes = 0
        self.forms = 0
        self.inp = 0
        self.ext_links = []
        self.nofollow = 0
        self.lang = ""
        self.html_tag_attrs = {}
        self.videos = 0
        self.tables = 0
        self.blocks = []          # (tag, text) для оценки структуры
        self._block = None
        self._bbuf = []
        self.styles = 0
        self.inline_style_bytes = 0
        self._in_style = False
        self._sbuf = []

    # -- helpers
    def _txt(self, s):
        return " ".join(s.split())

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang", "")
            self.html_tag_attrs = a
        if tag in ("script", "style", "noscript"):
            self._skip += 1
            if tag == "script":
                self.scripts += 1
            if tag == "style":
                self.styles += 1
                self._in_style = True
                self._sbuf = []
        if self._skip:
            if tag == "script" and "ld+json" in (a.get("type") or ""):
                self._ld = []
            return
        if tag == "title":
            self._t = True
        elif tag == "meta":
            n = (a.get("name") or a.get("property") or
                 a.get("http-equiv") or "").lower()
            if n:
                self.metas[n] = a.get("content") or ""
        elif tag == "link":
            rel = (a.get("rel") or "").lower()
            if "canonical" in rel:
                self.canonical = a.get("href")
            if "alternate" in rel and a.get("hreflang"):
                self.hreflang.append((a.get("hreflang"), a.get("href")))
            self.links.append({"rel": rel, "href": a.get("href") or "",
                               "type": a.get("type") or ""})
        elif tag in ("h1", "h2", "h3"):
            self._h = tag
            self._buf = []
        elif tag == "a":
            href = a.get("href") or ""
            if href:
                rec = {"href": href, "rel": a.get("rel") or "",
                       "text": ""}
                self.links.append(rec)
                if "nofollow" in (a.get("rel") or "").lower():
                    self.nofollow += 1
                self._a = rec
        elif tag == "img":
            self.img.append({"src": a.get("src") or a.get("data-src") or "",
                             "alt": a.get("alt"),
                             "title": a.get("title") or "",
                             "w": a.get("width") or "",
                             "h": a.get("height") or "",
                             "loading": a.get("loading") or ""})
        elif tag == "iframe":
            self.iframes += 1
        elif tag == "form":
            self.forms += 1
        elif tag == "input":
            self.inp += 1
        elif tag == "video":
            self.videos += 1
        elif tag == "table":
            self.tables += 1
        elif tag in ("p", "li", "section", "article", "div", "blockquote"):
            self._block = tag
            self._bbuf = []

    def handle_startendtag(self, tag, attrs):
        if tag == "img":
            a = dict(attrs)
            self.img.append({"src": a.get("src") or a.get("data-src") or "",
                             "alt": a.get("alt"), "title": a.get("title") or "",
                             "w": a.get("width") or "", "h": a.get("height") or "",
                             "loading": a.get("loading") or ""})
        if tag == "link":
            a = dict(attrs)
            rel = (a.get("rel") or "").lower()
            if "canonical" in rel:
                self.canonical = a.get("href")
            if "alternate" in rel and a.get("hreflang"):
                self.hreflang.append((a.get("hreflang"), a.get("href")))

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            if tag == "style" and self._in_style:
                self.inline_style_bytes += len("".join(self._sbuf))
                self._in_style = False
            if self._skip:
                self._skip -= 1
            if tag == "script" and self._ld is not None:
                self.ld.append("".join(self._ld))
                self._ld = None
            return
        if tag == "title":
            self._t = False
        elif tag in ("h1", "h2", "h3") and self._h == tag:
            t = self._txt("".join(self._buf))
            if t:
                {"h1": self.h1, "h2": self.h2, "h3": self.h3}[tag].append(t)
            self._h = None
        elif tag in ("p", "li", "section", "article", "div", "blockquote") and self._block == tag:
            t = self._txt("".join(self._bbuf))
            if len(t) > 40:
                self.blocks.append((tag, t[:200]))
            self._block = None

    def handle_data(self, data):
        if self._in_style:
            self._sbuf.append(data)
            return
        if self._ld is not None:
            self._ld.append(data)
            return
        if self._t:
            self.title += data
        if self._h:
            self._buf.append(data)
        if self._skip:
            return
        if self._block:
            self._bbuf.append(data)
        clean = data.strip()
        if clean and len(clean) > 1:
            self.text_len += len(clean)
            for w in re.findall(r"[а-яёa-z0-9\-]{3,}", data.lower()):
                if w not in STOP:
                    self.words[w] += 1


def fetch(url, method="GET"):
    req = urllib.request.Request(url, method=method, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8,ky;q=0.7",
        "Accept-Encoding": "identity",
    })
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read(4 * 1024 * 1024)
            return {"status": r.status, "headers": dict(r.headers), "body": body,
                    "elapsed": round(time.monotonic() - t0, 3), "url": r.geturl()}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "headers": dict(e.headers or {}), "body": b"",
                "elapsed": round(time.monotonic() - t0, 3), "url": url}
    except Exception as e:
        return {"status": 0, "headers": {}, "body": b"",
                "elapsed": round(time.monotonic() - t0, 3), "url": url,
                "error": str(e)}


def ld_types(buf):
    types, raw_blocks, errs = [], [], 0
    for b in buf:
        try:
            data = json.loads(b)
        except Exception:
            errs += 1
            continue
        raw_blocks.append(data)
        stack = [data]
        while stack:
            n = stack.pop()
            if isinstance(n, dict):
                t = n.get("@type")
                if isinstance(n, str):
                    types.append(t)
                elif isinstance(n, list):
                    types.extend(map(str, t))
                stack.extend(n.values())
            elif isinstance(n, list):
                stack.extend(n)
    return types, raw_blocks, errs


def audit_url(url):
    r = fetch(url)
    ctype = (r["headers"].get("Content-Type") or "")
    if "html" not in ctype.lower() or not r["body"]:
        return {"url": url, "status": r["status"], "error": r.get("error", "not html"),
                "elapsed": r["elapsed"], "html": None}
    h = r["body"].decode("utf-8", errors="replace")
    p = P()
    try:
        p.feed(h)
        p.close()
    except Exception as e:
        pass
    types, raw_ld, errs = ld_types(p.ld)
    internal, external, anchors = [], [], []
    for l in p.links:
        href = l.get("href") if isinstance(l, dict) else l
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        full = urllib.parse.urljoin(url, href)
        host = urllib.parse.urlsplit(full).hostname or ""
        if "argymaq.kg" in host:
            internal.append(full)
            if isinstance(l, dict):
                anchors.append({"to": full, "text": " ".join((l.get("text") or "").split()),
                                "rel": l.get("rel", "")})
        else:
            external.append(full)
    top = p.words.most_common(20)
    return {
        "url": url, "final_url": r["url"], "status": r["status"],
        "elapsed": r["elapsed"], "ttfb": r["elapsed"],
        "html_bytes": len(r["body"]), "text_len": p.text_len,
        "lang": p.lang, "title": " ".join(p.title.split()),
        "title_len": len(" ".join(p.title.split())),
        "meta_description": p.metas.get("description", "").strip(),
        "meta_keywords": p.metas.get("keywords", ""),
        "meta_robots": p.metas.get("robots", ""),
        "canonical": p.canonical,
        "hreflang": p.hreflang,
        "og": {k.split(":", 1)[1]: v for k, v in p.metas.items() if k.startswith("og:")},
        "twitter": {k.split(":", 1)[1]: v for k, v in p.metas.items() if k.startswith("twitter:")},
        "viewport": p.metas.get("viewport", ""),
        "h1": p.h1, "h2": p.h2, "h3": p.h3,
        "h1_count": len(p.h1),
        "img_total": len(p.img),
        "img_no_alt": sum(1 for i in p.img if not (i["alt"] or "").strip()),
        "img_no_dims": sum(1 for i in p.img if not (i["w"] and i["h"])),
        "img_lazy": sum(1 for i in p.img if i["loading"] == "lazy"),
        "images": p.img[:60],
        "ldjson_types": sorted(set(types)),
        "ldjson_count": len(p.ld),
        "ldjson_broken": errs,
        "ldjson_raw": raw_ld[:3],
        "internal_links": len(internal),
        "internal_unique": len(set(internal)),
        "external_links": sorted(set(external)),
        "nofollow": p.nofollow,
        "scripts": p.scripts, "styles": p.styles,
        "inline_style_bytes": p.inline_style_bytes,
        "iframes": p.iframes, "forms": p.forms, "inputs": p.inp,
        "videos": p.videos, "tables": p.tables,
        "words_total": sum(p.words.values()),
        "top_words": top,
        "counters": {
            "metrika": ("mc.yandex.ru" in h or "ym(" in h),
            "gtm_ga": ("googletagmanager.com" in h or "gtag(" in h or "google-analytics.com" in h),
            "fb_pixel": ("connect.facebook.net" in h or "fbq(" in h),
            "clarity": "clarity.ms" in h,
            "hotjar": "hotjar" in h,
        },
        "head_links": [l for l in p.links if isinstance(l, dict)][:40],
        "blocks_sample": p.blocks[:25],
        "anchors_sample": anchors[:40],
        "headers": {k: v for k, v in r["headers"].items()
                    if k.lower() in ("server", "cache-control", "content-encoding",
                                     "x-robots-tag", "link", "content-type",
                                     "strict-transport-security", "cf-cache-status",
                                     "x-cache", "vary", "expires", "x-powered-by")},
    }


def main():
    urls = [
        "https://argymaq.kg/",
        "https://argymaq.kg/our-tours/",
        "https://argymaq.kg/1-day-horseback-riding-tour-in-karakol-gorge/",
        "https://argymaq.kg/2-day-horseback-riding-itinerary-altyn-arashan/",
        "https://argymaq.kg/4-day-horseback-riding-tour-program/",
        "https://argymaq.kg/5-day-horseback-riding-tour-program/",
        "https://argymaq.kg/guesthouse-and-yurt-camp/",
        "https://argymaq.kg/airport-pickup/",
        "https://argymaq.kg/about-us/",
        "https://argymaq.kg/blog/",
        "https://argymaq.kg/2026/07/30/%d0%bf%d1%80%d0%b8%d0%b2%d0%b5%d1%82-%d0%bc%d0%b8%d1%80/",
        "https://argymaq.kg/category/%d0%b1%d0%b5%d0%b7-%d1%80%d1%83%d0%b1%d1%80%d0%b8%d0%ba%d0%b8/",
        "https://argymaq.kg/author/argymaqkg/",
        "https://argymaq.kg/?p=19",
        "https://argymaq.kg/wp-json/",
    ]
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(RAW, exist_ok=True)
    out = []
    for u in urls:
        d = audit_url(u)
        out.append(d)
        print("%-4s %6dms  %-70s  %s" % (d["status"], int(d["elapsed"] * 1000),
                                         u[:70],
                                         ",".join(d.get("ldjson_types") or [])[:60]))
        time.sleep(0.4)
    with open(os.path.join(OUT, "crawl_full.json"), "w", encoding="utf-8") as f:
        json.dump({"fetched_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
                   "pages": out}, f, ensure_ascii=False, indent=1)
    # tidy per-URL meta
    for d in out:
        slug = re.sub(r"[^a-zA-Z0-9]+", "-", d["url"].split("://", 1)[1])[:80]
        slim = {k: v for k, v in d.items() if k not in ("images", "ldjson_raw", "blocks_sample", "anchors_sample")}
        with open(os.path.join(RAW, slug + ".meta.json"), "w", encoding="utf-8") as f:
            json.dump(slim, f, ensure_ascii=False, indent=1)
    print("saved", len(out))


if __name__ == "__main__":
    main()