#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сводный разбор work/audit/crawl_full.json в читаемый отчёт."""
import json
import os
import sys

P = r"H:\susa ai 500\argymaq.kg\work\audit\crawl_full.json"
OUT = r"H:\susa ai 500\argymaq.kg\work\audit\pages_overview.md"


def main():
    d = json.load(open(P, encoding="utf-8"))
    lines = []
    for p in d["pages"]:
        lines.append("=" * 100)
        lines.append("%s | status %s | html %s B | text %s chars" % (
            p["url"], p["status"], p.get("html_bytes"), p.get("text_len")))
        lines.append("TITLE(%s): %s" % (p.get("title_len"), p.get("title")))
        lines.append("DESC: %s" % ((p.get("meta_description") or "(EMPTY)")[:250]))
        lines.append("ROBOTS: %s | CANONICAL: %s" % (p.get("meta_robots"), p.get("canonical")))
        lines.append("LANG: %s | VIEWPORT: %s" % (p.get("lang"), p.get("viewport")))
        lines.append("H1(%s): %s" % (p.get("h1_count"), p.get("h1")))
        lines.append("H2(%s): %s" % (len(p.get("h2") or []), (p.get("h2") or [])[:10]))
        lines.append("H3(%s): %s" % (len(p.get("h3") or []), (p.get("h3") or [])[:10]))
        lines.append("IMG: %s | noalt %s | nodims %s | lazy %s" % (
            p.get("img_total"), p.get("img_no_alt"), p.get("img_no_dims"), p.get("img_lazy")))
        lines.append("LDJSON: %s | broken %s | count %s" % (
            p.get("ldjson_types"), p.get("ldjson_broken"), p.get("ldjson_count")))
        lines.append("LINKS: internal %s uniq %s | external %s | nofollow %s" % (
            p.get("internal_links"), p.get("internal_unique"),
            len(p.get("external_links") or []), p.get("nofollow")))
        lines.append("COUNTERS: %s" % p.get("counters"))
        lines.append("WORDS: %s | top: %s" % (
            p.get("words_total"), ", ".join("%s:%s" % (w, c) for w, c in (p.get("top_words") or [])[:14])))
        lines.append("OG: %s" % ", ".join("%s=%s" % (k, (v or "")[:60]) for k, v in (p.get("og") or {}).items()))
        lines.append("TWITTER: %s" % ", ".join((p.get("twitter") or {}).keys()))
        lines.append("SCRIPTS: %s | styles %s | inline_css %s B | iframes %s | forms %s | inputs %s | videos %s | tables %s" % (
            p.get("scripts"), p.get("styles"), p.get("inline_style_bytes"),
            p.get("iframes"), p.get("forms"), p.get("inputs"), p.get("videos"), p.get("tables")))
        lines.append("HEADERS: %s" % json.dumps(p.get("headers") or {}, ensure_ascii=False))
        lines.append("EXTERNAL: %s" % ", ".join((p.get("external_links") or [])[:15]))
        lines.append("HREFLANG: %s" % (p.get("hreflang"),))
        lines.append("BLOCKS: %s" % " | ".join("%s:%s" % (t, x[:60]) for t, x in (p.get("blocks_sample") or [])[:12]))
        lines.append("")
    txt = "\n".join(lines)
    open(OUT, "w", encoding="utf-8").write(txt)
    # краткая сводка в stdout
    for p in d["pages"]:
        print("%-70s T=%-3s D=%-3s H1=%-2s IMG=%-3s ALT_MISS=%-3s WORDS=%-5s LD=%s" % (
            p["url"].replace("https://argymaq.kg", "")[:68],
            p.get("title_len"), len(p.get("meta_description") or ""),
            p.get("h1_count"), p.get("img_total"), p.get("img_no_alt"),
            p.get("words_total"), ",".join(p.get("ldjson_types") or []) or "-"))
    print("\n->", OUT)


if __name__ == "__main__":
    main()