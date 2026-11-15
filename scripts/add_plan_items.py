#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Добавляет пункты по безопасности и доступам в P0-план кейса."""
import io
import json

PATH = r"H:\susa ai 500\argymaq.kg\site\src\data\case\plan.json"

with io.open(PATH, encoding="utf-8") as f:
    plan = json.load(f)

for section in plan:
    if section["level"] != "P0":
        continue
    texts = [t["text"] for t in section["tasks"]]
    additions = [
        {
            "text": "Закрыть утечку логина и версий WordPress (REST users, generator, ?ver=, readme.html)",
            "who": "мы",
            "result": "логин и версии не видны снаружи",
        },
        {
            "text": "Ограничить /wp-login.php: лимит попыток, скрыть адрес входа, 2FA",
            "who": "мы + клиент (2FA)",
            "result": "защита от перебора пароля",
        },
        {
            "text": "Подключить Google Search Console и Яндекс Вебмастер, отправить sitemap",
            "who": "мы + клиент (подтверждение прав)",
            "result": "видно, индексируется ли сайт",
        },
    ]
    for a in additions:
        if a["text"] not in texts:
            section["tasks"].append(a)
            print("added:", a["text"])

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    json.dump(plan, f, ensure_ascii=False, indent=2)

print("P0 tasks:", len([s for s in plan if s["level"] == "P0"][0]["tasks"]))