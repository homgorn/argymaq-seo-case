#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Доступ к локальной базе знаний аудита (data/seo.db).

Примеры:
  python scripts/kb_query.py summary
  python scripts/kb_query.py issues critical
  python scripts/kb_query.py sql "select url, words from pages order by words"
  python scripts/kb_query.py fts "картинк"
"""
import json
import os
import sqlite3
import sys

ROOT = r"H:\susa ai 500\argymaq.kg"
DB = os.path.join(ROOT, "data", "seo.db")


def show(cur, title, cursor=None):
    src = cursor if cursor is not None else cur
    cols = [d[0] for d in src.description]
    rows = src.fetchall()
    print("\n== %s (%d) ==" % (title, len(rows)))
    if not rows:
        return
    print(" | ".join(cols))
    for r in rows:
        print(" | ".join("" if v is None else str(v)[:120] for v in r))


def main():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    args = sys.argv[1:]
    mode = args[0] if args else "summary"

    if mode == "summary":
        for t in ("pages", "issues", "competitors", "images", "keywords", "rankings"):
            n = cur.execute("select count(*) from %s" % t).fetchone()[0]
            print("%-14s %d" % (t, n))
        show(cur, "issues by severity",
             cur.execute("select severity, count(*) c from issues group by severity order by c desc"))
        show(cur, "issues by category",
             cur.execute("select category, count(*) c from issues group by category order by c desc"))
        show(cur, "top-15 issues",
             cur.execute("select severity, category, page, title from issues "
                         "order by priority, severity limit 15"))
    elif mode == "issues":
        sev = args[1] if len(args) > 1 else None
        q = "select severity, category, page, title, fact, fix, priority from issues"
        params = ()
        if sev:
            q += " where severity=?"
            params = (sev,)
        q += " order by priority, severity"
        show(cur, "issues " + (sev or ""), cur.execute(q, params))
    elif mode == "sql":
        show(cur, args[1], cur.execute(args[1]))
    elif mode == "fts":
        q = "select url, title, h1 from pages_fts where pages_fts match ?"
        show(cur, "fts " + args[1], cur.execute(q, (args[1],)))
    else:
        print(__doc__)
    con.close()


if __name__ == "__main__":
    main()