#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Убирает продающие блоки внизу страниц кейса: оставляет нейтральную навигацию по отчёту."""
import io
import re

ROOT = r"H:\susa ai 500\argymaq.kg\site\src\pages"

REPLACE_BAND = {
    "plan.astro": (
        """      <div class="band mt-12">
        <h2>Хотите такой же план для себя?</h2>
        <p>Сделаем аудит и разложим по приоритетам. Бесплатно.</p>
        <div class="flex flex-wrap justify-center gap-2.5">
          <a href="/kontakty/" class="btn btn-primary">Оставить заявку →</a>
          <a href="/work/" class="btn">Что уже сделали</a>
        </div>
      </div>""",
        """      <div class="band mt-12">
        <h2>Что дальше</h2>
        <p>Следующий раздел — что уже исправлено и где виден результат.</p>
        <div class="flex flex-wrap justify-center gap-2.5">
          <a href="/work/" class="btn btn-primary">Что сделано →</a>
          <a href="/audit/" class="btn">Вернуться к аудиту</a>
        </div>
      </div>"""
    ),
    "work.astro": (
        """      <div class="band mt-11">
        <h2>Хотите так же?</h2>
        <p>Покажем, что можно исправить на вашем сайте.</p>
        <div class="flex flex-wrap justify-center gap-2.5">
          <a href="/kontakty/" class="btn btn-primary">Оставить заявку →</a>
          <a href="/result/" class="btn">Смотреть цифры</a>
        </div>
      </div>""",
        """      <div class="band mt-11">
        <h2>Что дальше</h2>
        <p>Следующий раздел — цифры «до» и то, что появится после внедрения.</p>
        <div class="flex flex-wrap justify-center gap-2.5">
          <a href="/result/" class="btn btn-primary">Смотреть результат →</a>
          <a href="/plan/" class="btn">Вернуться к плану</a>
        </div>
      </div>"""
    ),
    "result.astro": (
        """      <div class="mt-11 flex flex-wrap gap-2.5">
        <a href="/kontakty/" class="btn btn-primary">Хочу так же →</a>
        <a href="/audit/" class="btn">Что нашли</a>
      </div>""",
        """      <div class="mt-11 flex flex-wrap gap-2.5">
        <a href="/" class="btn btn-primary">К оглавлению отчёта →</a>
        <a href="/audit/" class="btn">Что нашли</a>
      </div>"""
    ),
    "audit.astro": (
        """      <div class="mt-11 flex flex-wrap gap-2.5">
        <a href="/plan/" class="btn btn-primary">Что с этим делаем →</a>
        <a href="/" class="btn">К началу кейса</a>
      </div>""",
        """      <div class="mt-11 flex flex-wrap gap-2.5">
        <a href="/plan/" class="btn btn-primary">План исправлений →</a>
        <a href="/" class="btn">К оглавлению отчёта</a>
      </div>"""
    ),
}

for name, (old, new) in REPLACE_BAND.items():
    p = ROOT + "\\" + name
    t = io.open(p, encoding="utf-8").read()
    if old in t:
        t = t.replace(old, new, 1)
        with io.open(p, "w", encoding="utf-8", newline="") as f:
            f.write(t)
        print("fixed", name)
    else:
        print("MISS", name)