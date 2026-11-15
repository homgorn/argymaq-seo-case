# 20 — план P0 (неделя 1)

Критично, до любого продвижения. Каждый пункт проверяем.

## 1. Установить аналитику

| Что | Как |
|---|---|
| Яндекс Метрика | создать счётчик на metrika.yandex.ru → вставить код в `<head>` через плагин или тему |
| Цели | «Отправка формы», «Клик по WhatsApp», «Клик по телефону» |
| Вебвизор | включить запись сессий |
| GA4 | создать поток → GTM → тег |
| GTM | контейнер → тег GA4 |

Проверка: в HTML главной есть `mc.yandex.ru` и `googletagmanager.com`; цели срабатывают при тестовой отправке.

## 2. Пережать изображения

| Шаг | Действие |
|---|---|
| 1 | Скачать 54 файла из `wp-content/uploads/` |
| 2 | Конвертировать в WebP (quality 80), размеры 640 / 1024 / 1600 |
| 3 | Залить обратно |
| 4 | Заменить ссылки в записях и Elementor |
| 5 | Удалить исходники после замены |

Проверка: вес главной ≤ 5 МБ, вес страницы 5-дневного тура ≤ 8 МБ.

## 3. Заменить http:// на https://

| Где | Как |
|---|---|
| WP-опции | `siteurl` и `home` в `wp_options` |
| Elementor CSS | перегенерировать CSS после смены |
| Медиатека | Better Search Replace по `wp-content/uploads` |

Проверка: 0 ссылок `http://argymaq.kg` в HTML.

## 4. Прописать meta description

12 страниц. Готовые тексты — в [24-snippets.md](24-snippets.md).

Проверка: 12 из 12 страниц имеют description 140–160 знаков.

## 5. Внедрить JSON-LD

| Тип | Где |
|---|---|
| `Organization` | на всех страницах |
| `TouristBusiness` / `LocalBusiness` | на главной и контактах |
| `WebSite` + `SearchAction` | на главной |
| `BreadcrumbList` | на всех внутренних |
| `TouristTrip` | на страницах туров |
| `Product` + `Offer` | на страницах туров (цена) |
| `FAQPage` | где есть FAQ |
| `Review` / `AggregateRating` | на странице отзывов |

Проверка: validator.schema.org без ошибок.

## 6. Добавить alt

102 изображения без alt. Шаблон:

```
{что на фото} — {маршрут}, {локация}
```

Примеры: «Всадник на горной тропе в ущелье Каракола», «Юрточный лагерь в Алтын-Арашане», «Лошади на перевале к озеру Ала-Куль».

Проверка: 0 изображений без alt.

## 7. Включить gzip/brotli

```nginx
gzip on;
gzip_types text/plain text/css application/json application/javascript text/xml application/xml image/svg+xml;
gzip_min_length 1024;
brotli on;
brotli_types text/plain text/css application/json application/javascript text/xml application/xml image/svg+xml;
```

Проверка: `Content-Encoding: br` в ответе.

## 8. Удалить демо-запись

| Действие | Где |
|---|---|
| Удалить «Привет, мир» | Записи → Удалить в корзину → Очистить |
| Удалить дефолтный комментарий | Комментарии → Удалить |
| Удалить пустую рубрику «Без рубрики» | Записи → Рубрики (если пустая) |

Проверка: 404 на `/2026/07/30/привет-мир/`, нет в sitemap.

## 9. Закрыть дубли ?p=N

```nginx
if ($arg_p) { return 301 $scheme://$host$request_uri; }
```

Или плагин, который 301-редиректит `/?p=N` на канонический URL.

Проверка: `/?p=19` → 301 на `/`.

## 10. Исправить lang

В теме: `<html lang="en">` вместо `ru-RU`.

Проверка: `<html lang="en">`.

## Чек-лист недели 1

- [ ] Метрика + GA4 + цели
- [ ] Изображения пережаты
- [ ] http → https
- [ ] 12 description
- [ ] JSON-LD: Organization, LocalBusiness, WebSite, Breadcrumb
- [ ] 102 alt
- [ ] gzip/brotli
- [ ] Демо-запись удалена
- [ ] `?p=N` → 301
- [ ] `lang="en"`