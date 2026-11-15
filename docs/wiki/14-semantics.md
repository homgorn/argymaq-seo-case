# 14 — семантическое ядро

Регион: Каракол. Языки: EN (основной по контенту), RU (домен .kg, локальный спрос).

38 фраз в 5 кластерах. Объёмы частотности **не подтверждены** — нужны Wordstat / Keyword Planner [панель].

## Кластеры

| Кластер | Фраз | Целевая страница |
|---|---|---|
| Коммерческие — общие | 6 | `/` |
| Коммерческие — туры | 12 | `/our-tours/` + страницы туров |
| Коммерческие — размещение | 4 | `/guesthouse-and-yurt-camp/` |
| Коммерческие — трансфер | 3 | `/airport-pickup/` |
| Информационные | 8 | `/blog/` |
| Бренд | 5 | `/` |

## Фразы

### Коммерческие — общие (6)

| Фраза | Язык | Целевая |
|---|---|---|
| horse riding karakol | EN | `/` |
| horseback riding karakol | EN | `/` |
| horseback riding tours kyrgyzstan | EN | `/` |
| конные туры каракол | RU | `/` |
| конные прогулки каракол | RU | `/` |
| верхом на лошади каракол | RU | `/` |

### Коммерческие — туры (12)

| Фраза | Язык | Целевая |
|---|---|---|
| horse riding tour karakol kyrgyzstan | EN | `/our-tours/` |
| kyrgyzstan horseback tour 3 days | EN | `/our-tours/` |
| horse riding tour ala kol lake | EN | `/4-day-…/` |
| horse riding ala kul | EN | `/4-day-…/` |
| horseback riding ala-kul lake tour | EN | `/4-day-…/` |
| horseback riding tour kyrgyzstan price | EN | `/our-tours/` |
| horse riding tour kyrgyzstan price | EN | `/our-tours/` |
| one day horse riding tour karakol gorge | EN | `/1-day-…/` |
| horse riding tour karakol gorge | EN | `/1-day-…/` |
| two day horse riding tour altyn arashan | EN | `/2-day-…/` |
| horse riding tour altyn arashan | EN | `/2-day-…/` |
| five day horse riding tour kyrgyzstan | EN | `/5-day-…/` |

### Коммерческие — размещение (4)

| Фраза | Язык | Целевая |
|---|---|---|
| guesthouse karakol | EN | `/guesthouse-and-yurt-camp/` |
| yurt camp karakol | EN | `/guesthouse-and-yurt-camp/` |
| yurt stay karakol kyrgyzstan | EN | `/guesthouse-and-yurt-camp/` |
| karakol hostel | EN | `/guesthouse-and-yurt-camp/` |

### Коммерческие — трансфер (3)

| Фраза | Язык | Целевая |
|---|---|---|
| airport pickup karakol | EN | `/airport-pickup/` |
| airport transfer karakol from bishkek | EN | `/airport-pickup/` |
| transfer tamchy to karakol | EN | `/airport-pickup/` |

### Информационные (8)

| Фраза | Язык | Целевая |
|---|---|---|
| things to do in karakol | EN | `/blog/` |
| karakol horse riding | EN | `/blog/` |
| altyn arashan hot springs | EN | `/blog/` |
| ala kul lake trek | EN | `/blog/` |
| karakol gorge hike | EN | `/blog/` |
| best time to visit karakol | EN | `/blog/` |
| kyrgyzstan horse riding experience | EN | `/blog/` |
| horseback riding season kyrgyzstan | EN | `/blog/` |

### Бренд (5)

| Фраза | Язык | Целевая |
|---|---|---|
| argymaq | EN | `/` |
| argymaq kyrgyzstan | EN | `/` |
| аргимак каракол | RU | `/` |
| argymaq horseback | EN | `/` |
| argymaq tours | EN | `/` |

## Подсказки поисковых систем

Собраны автоматически (Google suggest API), см. `data/keywords.json`.

Примеры:

| Запрос | Подсказки |
|---|---|
| horse riding karakol | horse riding karakol valley, horse trekking karakol, horse riding tour karakol, one day horse riding karakol |
| horseback riding karakol | karakol horseback riding, horse riding tour karakol, horse riding near karakol, horseback riding experience levels |
| horseback riding tours kyrgyzstan | kyrgyzstan horse riding trips, best horse riding tours kyrgyzstan, 3 day horse riding tour kyrgyzstan |

## Что проверить в панелях [панель]

1. Wordstat: `конные туры`, `конные прогулки Каракол`, `Ак-Суу конные прогулки`, `Ала-Куль конный тур`.
2. Keyword Planner: `horse riding karakol`, `karakol tours`, `ala kul horse riding`, `kyrgyzstan horse riding`.
3. Живая выдача по региону Каракол: кто в ТОПе, какие форматы страниц.

## Структура под семантику

| Страница | Кластер | Что должна закрывать |
|---|---|---|
| `/` | общие + бренд | «конные туры Каракол», «horse riding karakol» |
| `/our-tours/` | туры | «туры из Каракола», «цены» |
| `/1-day-…/` | туры | «однодневный тур в ущелье Каракола» |
| `/2-day-…/` | туры | «тур в Алтын-Арашан» |
| `/4-day-…/` | туры | «тур на Ала-Куль» |
| `/5-day-…/` | туры | «5-дневный тур» |
| `/guesthouse-and-yurt-camp/` | размещение | «гостевой дом Каракол», «юрточный лагерь» |
| `/airport-pickup/` | трансфер | «трансфер из аэропорта в Каракол» |
| `/blog/` | информационные | «что делать в Караколе», «Ала-Куль трек» |
| `/contacts/` (новая) | локальные | «Аргымак контакты Каракол» |

## Чего не хватает в структуре

| Пробел | Что создать |
|---|---|
| Страница цен | `/prices/` или блок на `/our-tours/` |
| Страница «Как забронировать» | `/booking/` |
| Страница «Частые вопросы» | `/faq/` |
| Страницы гидов | `/guides/` |
| Страницы отзывов | `/reviews/` |
| Статьи блога | 8 информационных статей по кластеру |
| Зимние туры | `/winter-tours/` (если сезон круглый год) |
| Китайский рынок | `/zh/` (если нужен) |