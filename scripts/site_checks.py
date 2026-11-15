#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Точечные проверки уровня сайта для argymaq.kg.

Проверяет: главную HTML (счётчики, hreflang, schema, viewport, og),
HTTP-заголовки главной, редирект сам-на-себя, скорость (TTFB по 5 замерам),
размер HTML/CSS/JS, наличие sitemap-пагинации, robots для UAI bots,
страницы сервисные (404, /sitemap.xml, /wp-sitemap.xml), HSTS, сжатие.

Результат: work/audit/site_checks.json + вывод в stdout.
"""
import json
import os
import re
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
BASE = "https://argymaq.kg"
OUT = r"H:\susa ai 500\argymaq.kg\work\audit\site_checks.json"


def req(url, method="GET", headers=None, timeout=30):
    h = {"User-Agent": UA, "Accept": "*/*", "Accept-Language": "ru,en;q=0.9",
         "Accept-Encoding": "gzip, deflate, br"}
    if headers:
        h.update(headers)
    r = urllib.request.Request(url, method=method, headers=h)
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(r, timeout=timeout) as resp:
            body = resp.read()
            return {"url": url, "status": resp.status, "headers": dict(resp.headers),
                    "len": len(body), "elapsed": round(time.monotonic() - t0, 3),
                    "body": body, "final": resp.geturl()}
    except urllib.error.HTTPError as e:
        body = b""
        try:
            body = e.read()
        except Exception:
            pass
        return {"url": url, "status": e.code, "headers": dict(e.headers or {}),
                "len": len(body), "elapsed": round(time.monotonic() - t0, 3),
                "body": body, "final": url}
    except Exception as e:
        return {"url": url, "status": 0, "headers": {}, "len": 0,
                "elapsed": round(time.monotonic() - t0, 3), "body": b"",
                "error": str(e), "final": url}


def main():
    res = {}
    # 1. TTFB/скорость: 5 замеров главной и тяжёлой страницы
    speed = {}
    for label, u in (("home", BASE + "/"), ("tours", BASE + "/our-tours/")):
        times = []
        for _ in range(5):
            r = req(u, method="GET", headers={"Range": "bytes=0-2048"})
            times.append(r["elapsed"])
            time.sleep(0.3)
        speed[label] = {"runs": times, "min": min(times), "median": sorted(times)[2], "max": max(times)}
    res["speed"] = speed

    # 2. HTTP-заголовки главной + безопасность
    h = req(BASE + "/")
    hdr = {k.lower(): v for k, v in h["headers"].items()}
    res["home_headers"] = hdr
    res["security"] = {
        "hsts": hdr.get("strict-transport-security"),
        "csp": hdr.get("content-security-policy"),
        "x_frame_options": hdr.get("x-frame-options"),
        "x_content_type_options": hdr.get("x-content-type-options"),
        "referrer_policy": hdr.get("referrer-policy"),
        "permissions_policy": hdr.get("permissions-policy"),
        "server": hdr.get("server"),
        "x_powered_by": hdr.get("x-powered-by"),
        "cache_control": hdr.get("cache-control"),
        "content_encoding": hdr.get("content-encoding"),
        "cdn": any(x in (hdr.get("server", "") + str(hdr)).lower()
                   for x in ("cloudflare", "cf-ray", "fastly", "akamai", "sucuri")),
    }

    # 3. Сжатие: сравнить identity и gzip/br
    r_id = req(BASE + "/", headers={"Accept-Encoding": "identity"})
    r_br = req(BASE + "/", headers={"Accept-Encoding": "br, gzip, deflate"})
    res["compression"] = {"identity_len": r_id["len"], "encoded_len": r_br["len"],
                          "encoding_header": r_br["headers"].get("Content-Encoding")}

    # 4. Главная: редирект на себя, дубли
    res["home_self_redirect"] = {"start": BASE + "/", "final": h["final"],
                                 "status": h["status"],
                                 "redirected": h["final"].rstrip("/") != BASE}

    # 5. www / http зеркала
    mirrors = {}
    for v in ("http://argymaq.kg/", "https://www.argymaq.kg/", "http://www.argymaq.kg/"):
        r = req(v)
        mirrors[v] = {"status": r["status"], "final": r["final"], "len": r["len"]}
    res["mirrors"] = mirrors

    # 6. robots: UA-специфичные правила + AI-краулеры
    robots = req(BASE + "/robots.txt")["body"].decode("utf-8", "replace")
    res["robots_raw"] = robots
    uas = re.findall(r"User-agent:\s*(.+)", robots)
    res["robots_ua_blocks"] = uas

    # 7. Сервисные страницы
    svc = {}
    for name, u in (("404", BASE + "/nonexistent-page-seo-audit-12345"),
                    ("sitemap_index", BASE + "/wp-sitemap.xml"),
                    ("sitemap_kml", BASE + "/sitemap_index.xml"),
                    ("feed", BASE + "/feed/"),
                    ("wp_json", BASE + "/wp-json/"),
                    ("favicon", BASE + "/favicon.ico"),
                    ("llms", BASE + "/llms.txt")):
        r = req(u)
        svc[name] = {"status": r["status"], "len": r["len"], "elapsed": r["elapsed"],
                     "ctype": r["headers"].get("Content-Type")}
    res["service_pages"] = svc

    # 8. HTML главной: важные маркеры
    html = h["body"].decode("utf-8", "replace")
    res["home_markers"] = {
        "viewport": bool(re.search(r'name=["\']viewport["\']', html)),
        "yandex_metrika": ("mc.yandex.ru" in html or "ym(" in html),
        "gtm": "googletagmanager.com" in html,
        "ga4": "gtag(" in html or "google-analytics.com" in html,
        "fbq": "fbq(" in html,
        "ld_json_count": len(re.findall(r'application/ld\+json', html)),
        "og_tags": len(re.findall(r'property=["\']og:', html)),
        "twitter_tags": len(re.findall(r'name=["\']twitter:', html)),
        "hreflang": len(re.findall(r'hreflang=', html)),
        "amp": "ampproject" in html,
        "inline_style_blocks": len(re.findall(r"<style", html)),
        "style_block_bytes": sum(len(x) for x in re.findall(r"(?is)<style[^>]*>(.*?)</style>", html)),
        "script_src": re.findall(r'<script[^>]+src=["\']([^"\']+)', html)[:30],
        "css_hrefs": re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]+href=["\']([^"\']+)', html)[:30],
        "total_script_src": len(re.findall(r'<script[^>]+src=', html)),
        "total_css": len(re.findall(r'rel=["\']stylesheet["\']', html)),
        "generator": re.findall(r'name=["\']generator["\'][^>]*content=["\']([^"\']+)', html),
        "wp_version": (re.findall(r'ver=(\d+\.\d+(?:\.\d+)?)', html) or [])[:5],
        "json_ld_blocks": re.findall(r'(?is)<script[^>]+application/ld\+json[^>]*>(.{0,600})', html)[:3],
    }

    # 9. HTML главной: ссылки на соцсети / мессенджеры (для проверки запрещённых)
    res["social_links"] = sorted(set(re.findall(
        r'https?://(?:www\.)?(?:facebook|instagram|linkedin|tiktok|ok\.ru|vk\.com|youtube\.com|t\.me|wa\.me|api\.whatsapp)[^"\'<>\s)]*',
        html)))[:20]

    # 10. Скорость загрузки ресурсов (CSS/JS): проверим размеры топ-файлов
    assets = res["home_markers"]["css_hrefs"] + [s for s in res["home_markers"]["script_src"] if not s.startswith("data:")]
    assets = [urllib.parse.urljoin(BASE + "/", a) for a in assets][:14]
    asset_stats = []
    for a in assets:
        r = req(a, method="GET", headers={"Range": "bytes=0-1"})
        asset_stats.append({"url": a.replace(BASE, ""), "status": r["status"],
                            "len": r["len"], "ms": int(r["elapsed"] * 1000),
                            "ctype": r["headers"].get("Content-Type"),
                            "cache": r["headers"].get("Cache-Control")})
    res["assets"] = asset_stats

    # 11. SSL
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(__import__("socket").create_connection(("argymaq.kg", 443), timeout=10),
                             server_hostname="argymaq.kg") as s:
            cert = s.getpeercert()
        import datetime
        exp = datetime.datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
        res["ssl"] = {"expires": cert["notAfter"], "days_left": (exp - datetime.datetime.utcnow()).days,
                      "issuer": dict(x[0] for x in cert["issuer"])}
    except Exception as e:
        res["ssl"] = {"error": str(e)}

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, default=str)
    print(json.dumps({k: v for k, v in res.items() if k != "home_markers"},
                     ensure_ascii=False, indent=1, default=str)[:6000])
    print("\nMARKERS:", json.dumps(res["home_markers"], ensure_ascii=False, indent=1, default=str)[:3000])
    print("\nsaved", OUT)


if __name__ == "__main__":
    main()