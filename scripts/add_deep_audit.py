#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Добавляет новые находки глубокого аудита в site/src/data/case/audit.json."""
import json
import io

PATH = r"H:\susa ai 500\argymaq.kg\site\src\data\case\audit.json"

with io.open(PATH, encoding="utf-8") as f:
    data = json.load(f)

ids = {item["id"] for item in data}

NEW = [
    {
        "id": "wp-user-enumeration",
        "severity": "critical",
        "category": "Безопасность",
        "title": "Логин администратора виден всем",
        "plain": "Сайт отдаёт список пользователей: имя и логин администратора — ARGYMAQKG. Также по адресу /?author=1 поисковик вычисляет логин. Это готовая цель для подбора пароля.",
        "fact": "/wp-json/wp/v2/users отдаёт 200 и раскрывает имя (ARGYMAQKG), логин (argymaqkg) и Gravatar-хэш; /?author=1 редиректит на /author/argymaqkg/.",
        "fix": "Закрыть REST API users для неавторизованных (фильтр rest_user_query / плагин), сменить логин, убрать публичный Gravatar-профиль",
        "priority": 1,
        "impact": "high",
        "status": "pending",
    },
    {
        "id": "wp-version-disclosure",
        "severity": "critical",
        "category": "Безопасность",
        "title": "Разглашена точная версия WordPress и плагинов",
        "plain": "По коду страницы видно версии: WordPress 7.1.4, Elementor 4.2.1, jQuery 3.7.1 и другие. Злоумышленник сопоставляет версии с известными уязвимостями.",
        "fact": "meta generator «WordPress 7.1.4» и «Elementor 4.2.1»; RSS отдаёт https://wordpress.org/?v=7.1.4; все ассеты с параметром ?ver=; /readme.html и /license.txt доступны (200).",
        "fix": "Удалить readme.html и license.txt, убрать generator и ?ver= параметры, обновить все плагины до последних версий",
        "priority": 1,
        "impact": "high",
        "status": "pending",
    },
    {
        "id": "wp-login-exposed",
        "severity": "warning",
        "category": "Безопасность",
        "title": "Форма входа в админку открыта всем",
        "plain": "Любой может открыть страницу входа и перебирать пароль. Форма не скрыта, ограничений попыток нет.",
        "fact": "/wp-login.php отдаёт 200, публично доступен; /xmlrpc.php закрыт (403) — это хорошо.",
        "fix": "Включить ограничение попыток, скрыть адрес входа, добавить 2FA, ограничить доступ по IP при возможности",
        "priority": 2,
        "impact": "medium",
        "status": "pending",
    },
    {
        "id": "wp-install-exposed",
        "severity": "warning",
        "category": "Безопасность",
        "title": "Страница установки WordPress открыта",
        "plain": "Страница /wp-admin/install.php показывает, что сайт уже установлен. Она не позволяет переустановить, но раскрывает состояние.",
        "fact": "/wp-admin/install.php отдаёт 200 с сообщением, что WordPress уже установлен.",
        "fix": "Закрыть /wp-admin/install.php внешним запросам (403) на уровне nginx",
        "priority": 2,
        "impact": "low",
        "status": "pending",
    },
    {
        "id": "wp-opml-exposed",
        "severity": "notice",
        "category": "Безопасность",
        "title": "OPML-экспорт блога доступен",
        "plain": "Файл /wp-links-opml.php отдаёт список закладок и заголовок сайта. Мелочь, но лишняя точка входа.",
        "fact": "/wp-links-opml.php отдаёт 200 (251 байт).",
        "fix": "Отключить или закрыть /wp-links-opml.php",
        "priority": 3,
        "impact": "low",
        "status": "pending",
    },
    {
        "id": "serp-unknown",
        "severity": "notice",
        "category": "Поиск",
        "title": "Неизвестно, индексируется ли сайт вообще",
        "plain": "Мы не смогли проверить, видит ли сайт Google и Яндекс: Google отдал страницу согласия, Яндекс — CAPTCHA. Возможно, сайт вообще не попал в поиск.",
        "fact": "Проверка «site:argymaq.kg» в Google и Яндекс заблокирована. Нужны выгрузки из Google Search Console и Яндекс Вебмастера.",
        "fix": "Добавить сайт в панели, отправить sitemap, проверить покрытие индекса",
        "priority": 1,
        "impact": "high",
        "status": "pending",
    },
]

merged = list(data)
for item in NEW:
    if item["id"] not in ids:
        merged.append(item)
        print("added:", item["id"])
    else:
        print("skip (exists):", item["id"])

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print("\ntotal issues:", len(merged))