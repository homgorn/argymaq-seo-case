<!-- Language: Русский. Основной README — английский. -->
<div align="center">

[English](README.md) · **Русский** · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [中文](README.zh.md) · [日本語](README.ja.md)

</div>

---

# argymaq-seo-case

**Полный SEO-аудит сайта кыргызского туроператора в виде клиентского отчёта и портфолио-кейса.**

Живой сайт: **https://homgorn.github.io/argymaq-seo-case/**

![Аудит](https://img.shields.io/badge/аудит-54%20проблемы-critical) ![Страниц](https://img.shields.io/badge/страниц-17-success) ![Стек](https://img.shields.io/badge/Astro-5.18-ff5d01) ![Лицензия](https://img.shields.io/badge/license-MIT-blue)

---

## Что это

Полный воспроизводимый SEO-аудит сайта **argymaq.kg** — оператора конных туров в Караколе, Кыргызстан — превращённый в два результата:

1. **Статический сайт-отчёт** (Astro, 17 страниц), который объясняет находки простым языком: с графиками, сравнением «было / стало» и поэтапным планом. Написан для владельца, который не работает в SEO.
2. **Полный набор данных** — каждый замер, каждый скрипт и каждый источник, чтобы работу можно было перепроверить.

Кейс подан как «**было → стало**»: что нашли, что это значит для денег и что исправляем первым.

### С чего начали

| Показатель | Было | Источник |
|---|---|---|
| Вес изображений на странице тура | **150,4 МБ** | измерено, HEAD-запросы по 54 файлам |
| Медианное время ответа | **4,33 с** | измерено, 5 прогонов |
| Meta description | **0 из 14 страниц** | измерено |
| Блоков schema.org | **0 на 15 URL** | измерено |
| Установленной аналитики | **нет** | измерено |
| Форм обратной связи | **0** | измерено |

## Что внутри

```
argymaq-seo-case/
├── site/                   сам сайт-отчёт (Astro 5 + Tailwind 4)
│   ├── src/pages/          17 маршрутов
│   ├── src/components/     MetricCard, BeforeAfter, Phase, PriceCard, Steps…
│   ├── src/data/           услуги, пакеты, данные кейса в JSON
│   └── dist/               собранный результат (не в гите)
├── docs/
│   ├── architecture/       архитектура сайта и дизайн-система
│   ├── reports/            отчёт для владельца (RU + EN)
│   ├── research/           цены рынка, паттерны отчётов, GEO, карты
│   └── wiki/               многоуровневая вики всех находок
├── scripts/                11 скриптов на Python, воспроизводящих аудит
├── research/               сырые данные по конкурентам и бенчмарк
└── data/                   SQLite-база знаний и JSONL-выгрузка
```

## Быстрый старт

```bash
git clone https://github.com/homgorn/argymaq-seo-case.git
cd argymaq-seo-case/site
npm install
npm run dev        # локальный предпросмотр
npm run build      # сборка в dist/
npm run check      # проверка типов
```

Перезапустить аудит:

```bash
python scripts/crawl_full.py
python scripts/site_checks.py
python scripts/images_head.py
python scripts/competitors.py
python scripts/benchmark.py
python scripts/build_kb.py
python scripts/verify_site.py
```

## Документация

| Документ | О чём |
|---|---|
| [Архитектура](docs/architecture/00-architecture.md) | карта из 17 страниц, дизайн-система, модель данных |
| [План по специалистам](docs/architecture/01-skill-plan.md) | кто и на каком этапе применяется |
| [Отчёт (RU)](docs/reports/seo-audit-2026-11-15.md) | полный отчёт, отданный клиенту |
| [Отчёт (EN)](docs/reports/seo-audit-2026-11-15.en.md) | английская версия того же отчёта |
| [Цены, Кыргызстан](docs/research/market-prices-kr/00-prices.md) | рыночные ставки в сомах, с источниками и датами |
| [Клиентские отчёты](docs/research/client-reporting/00-reporting.md) | как агентства подают отчёты, которые читают |
| [GEO / ИИ-поиск](docs/research/geo-ai-search/00-geo.md) | измерение видимости в ChatGPT, Perplexity, Google AI |
| [Локальные карты](docs/research/local-maps/00-maps.md) | Яндекс Карты, 2GIS, Google Business Profile |
| [Структура кейса](docs/research/case-studies/00-case-study.md) | что делает портфолио конверсионным |
| [Индекс вики](docs/wiki/40-index-portfolio.md) | все документы со связями |

## Как читать метки источников

Каждое утверждение в документах несёт метку:

| Метка | Значение |
|---|---|
| **[измерено]** | проверено прямым запросом, цифра воспроизводима |
| **[сообщено]** | взято из внешнего источника с URL и датой |
| **[выведено]** | логический вывод, не прямое измерение |
| **[панель]** | нужны данные, к которым у аудита не было доступа |

Ни одна цифра не выдумана. Где данных не было — указан пробел, а не предположение.

## Лицензия

MIT — см. [LICENSE](LICENSE). Данные аудита и отчёты предоставлены как есть, для справки.

Сайт `argymaq.kg` и его бренд принадлежат их владельцу. В этом репозитории — измерения и рекомендации, а не их контент.