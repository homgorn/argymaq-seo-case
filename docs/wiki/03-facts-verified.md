# 03 — измеренные факты

Только то, что подтверждено запросом к сайту. Каждая строка воспроизводима скриптом из `scripts/`.

## 1. Ответ сервера

| Факт | Значение | Как проверено |
|---|---|---|
| Код главной | 200 | GET https://argymaq.kg/ |
| Сервер | nginx/1.30.6 | заголовок Server |
| PHP | 8.4.27 | заголовок X-Powered-By |
| Размер HTML главной | 142 011 байт | Content-Length / фактическое чтение |
| Content-Encoding | отсутствует | заголовки ответа |
| Connection | close | заголовок Connection |
| HTTP-версия | признаков h2/h3 нет | `Connection: close`, отсутствие negotiated h2 |
| CDN | нет | отсутствуют cf-ray / fastly / akamai |

## 2. Замеры времени (5 прогонов, 14–15.11.2026)

| URL | Прогоны, с | Медиана |
|---|---|---|
| `/` | 3,063 / 5,328 / 4,328 / 5,250 / 2,313 | 4,328 |
| `/our-tours/` | 3,922 / 4,578 / 2,812 / 7,469 / 5,297 | 4,578 |

Отдельные замеры отдельных страниц (одиночный GET): `/about-us/` 5,2 с, `/blog/` 2,5 с, `/5-day-…/` 6,2 с, `/author/argymaqkg/` 6,8 с, `/?p=19` 9,1 с.

## 3. Редиректы и зеркала

| Проверка | Результат |
|---|---|
| `http://argymaq.kg/` | 301 → `https://argymaq.kg/` |
| `https://www.argymaq.kg/` | 301 → `https://argymaq.kg/` |
| `http://www.argymaq.kg/` | 301 → `https://argymaq.kg/` |
| `/about-us` | 301 → `/about-us/` |
| `/our-tours` | 301 → `/our-tours/` |
| `/airport-pickup` | 301 → `/airport-pickup/` |
| `/blog` | 301 → `/blog/` |
| `/guesthouse-and-yurt-camp` | 301 → `/guesthouse-and-yurt-camp/` |
| `/1-day-…` (без слэша) | 301 → слэш |
| `/2-day-…` (без слэша) | 301 → слэш |
| `/4-day-…` (без слэша) | 301 → слэш |
| `/5-day-…` (без слэша) | 301 → слэш |

SSL: Let's Encrypt, `notAfter = Dec 27 20:12:14 2026 GMT`, 43 дня до истечения на момент замера.

## 4. robots.txt и sitemap

robots.txt (111 байт), дословно:

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://argymaq.kg/wp-sitemap.xml
```

sitemap-индекс `wp-sitemap.xml` (512 байт) содержит 4 файла:

| Файл | URL | lastmod |
|---|---|---|
| `wp-sitemap-posts-page-1.xml` | 10 страниц | 2026-07-31 … 2026-08-19 |
| `wp-sitemap-posts-post-1.xml` | 1 запись (`/2026/07/30/привет-мир/`) | 2026-07-30 |
| `wp-sitemap-taxonomies-category-1.xml` | `/category/без-рубрики/` | — |
| `wp-sitemap-users-1.xml` | `/author/argymaqkg/` | — |

Всего 13 URL. Устаревших lastmod (> 1 года) — 0.

## 5. Служебные страницы

| URL | Код | Размер |
|---|---|---|
| `/nonexistent-page-seo-audit-12345` | 404 | 85 891 байт |
| `/wp-sitemap.xml` | 200 | 512 байт |
| `/sitemap_index.xml` | 404 | 85 891 байт |
| `/feed/` | 200 | 2 042 байта |
| `/wp-json/` | 200 | 559 660 байт |
| `/favicon.ico` | 200 | 3 241 байт, image/png |
| `/llms.txt` | 404 | 85 891 байт |

## 6. Содержательные страницы (14 URL)

| URL | Title, знаков | Description | H1 | Слов | Картинок | Без alt | JSON-LD | OG | Метрика |
|---|---|---|---|---|---|---|---|---|---|
| `/` | 30 | пусто | 2 | 343 | 21 | 21 | нет | нет | нет |
| `/our-tours/` | 30 | пусто | 1 | 78 | 6 | 6 | нет | нет | нет |
| `/1-day-…-karakol-gorge/` | 65 | пусто | 1 | 85 | 13 | 13 | нет | нет | нет |
| `/2-day-…-altyn-arashan/` | 69 | пусто | 1 | 143 | 4 | 4 | нет | нет | нет |
| `/4-day-…-program/` | 56 | пусто | 1 | 152 | 8 | 8 | нет | нет | нет |
| `/5-day-…-program/` | 56 | пусто | 1 | 105 | 17 | 17 | нет | нет | нет |
| `/guesthouse-and-yurt-camp/` | 44 | пусто | 1 | 112 | 1 | 1 | нет | нет | нет |
| `/airport-pickup/` | 53 | пусто | 1 | 96 | 1 | 1 | нет | нет | нет |
| `/about-us/` | 29 | пусто | 1 | 153 | 1 | 1 | нет | нет | нет |
| `/blog/` | 86 | пусто | 1 | 166 | 11 | 11 | нет | нет | нет |
| `/category/без-рубрики/` | 32 | пусто | 1 | 43 | 1 | 1 | нет | нет | нет |
| `/author/argymaqkg/` | 30 | пусто | 1 | 43 | 1 | 1 | нет | нет | нет |
| `/2026/07/30/привет-мир/` | 33 | пусто | 1 | 93 | 2 | 1 | нет | нет | нет |
| `/?p=19` | 30 | пусто | 2 | 343 | 21 | 21 | нет | нет | нет |

## 7. Изображения (54 уникальных файла)

| Метрика | Значение |
|---|---|
| Суммарный вес | 408,1 МБ |
| Средний вес | 7 739 КБ |
| Тяжелее 300 КБ | 43 |
| Тяжелее 1 МБ | 42 |
| Тяжелее 5 МБ | 37 |
| Тяжелее 10 МБ | 22 |
| PNG | 52 |
| JPG | 1 |
| WebP / AVIF | 0 |
| Без Cache-Control | 53 |

Вес по страницам: `/5-day-…/` 150,4 МБ; `/blog/` 114,3 МБ; `/1-day-…/` 102,1 МБ; `/4-day-…/` 79,4 МБ; `/` 75,4 МБ; `/our-tours/` 51,0 МБ; `/2-day-…/` 36,9 МБ.

Топ-5: `IMG_7365-convert.io_.png` 15,2 МБ; `IMG_5605-convert.io_.png` 15,2 МБ; `IMG_6419-convert.io_.png` 14,6 МБ; `IMG_7333-convert.io_.png` 13,6 МБ; `IMG_6391-convert.io_.png` 13,5 МБ.

## 8. Служебные заголовки (главная)

| Заголовок | Значение |
|---|---|
| `Strict-Transport-Security` | отсутствует |
| `Content-Security-Policy` | отсутствует |
| `X-Frame-Options` | отсутствует |
| `X-Content-Type-Options` | отсутствует |
| `Referrer-Policy` | отсутствует |
| `Permissions-Policy` | отсутствует |
| `Cache-Control` | отсутствует |
| `Expires` | отсутствует |
| `Vary` | отсутствует |

## 9. Внутренняя структура главной

| Элемент | Значение |
|---|---|
| `<html lang>` | `ru-RU` |
| meta viewport | `width=device-width, initial-scale=1` |
| Скриптов внешних | 9 |
| Стилей внешних | 17 |
| Инлайн-стилей | 24 блока, 73 632 байта |
| `<style>` суммарно | 73 632 байта |
| Iframe | 0 |
| Form | 0 |
| Input | 0 |
| Video | 0 |
| Table | 0 |
| Внутренних ссылок | 20 (12 уникальных) |
| Внешних ссылок | 5 |
| nofollow | 0 |

## 10. Внешние ссылки сайта

| URL | Назначение |
|---|---|
| `https://wa.me/996501282030` | WhatsApp |
| `https://api.whatsapp.com/send?phone=+996501282030` | WhatsApp API |
| `https://facebook.com` | соцсеть |
| `https://instagram.com` | соцсеть |
| `https://linkedin.com` | соцсеть |

Все внешние ссылки отдают 200. Ссылок на 2GIS, Яндекс Карты, Google Maps, Tripadvisor, GetYourGuide нет.