# 22 — план P2 (недели 4–8)

Скорость и качество.

## 24. Кэш страниц

| Вариант | Когда |
|---|---|
| LiteSpeed Cache | если сервер на LiteSpeed |
| WP Super Cache | shared-хостинг |
| W3 Total Cache | VPS с Memcached |
| WP Rocket | платный, самый простой |

Настройки: кэш страниц, кэш браузера, минификация, ленивая загрузка, preload.

## 25. OPcache + объектный кэш

```ini
opcache.enable=1
opcache.memory_consumption=256
opcache.max_accelerated_files=20000
opcache.validate_timestamps=0
```

Redis: `wp-redis` плагин + `redis-server`.

## 26. CDN

| Вариант | Стоимость |
|---|---|
| Cloudflare Free | 0 |
| bunny.net | ~$1/мес |
| jsDelivr | только для статики |

Настроить: проксирование, кэш статики, HTTP/2, Brotli.

## 27. Ленивая загрузка и приоритет

```html
<img loading="lazy" decoding="async" ...>
<img fetchpriority="high" ...>  <!-- для LCP -->
```

## 28. Убрать лишние плагины

Проверить:

| Плагин | Нужен? |
|---|---|
| elementor | да, конструктор |
| superb-blocks | проверить, какие блоки используются |
| animated-floating-chat-button | да (WhatsApp) |
| wpfront-scroll-top | под вопросом |
| jquery-migrate | можно отключить, если тема не требует |

## 29. Объединить CSS и JS

Плагин Asset CleanUp или Autoptimize. Убрать неиспользуемые стили Elementor.

## 30. Локальные шрифты

Скачать Roboto и Roboto Slab, положить на сервер, отключить Google Fonts.

## 31. HTTP/2 или HTTP/3

```nginx
listen 443 ssl http2;
```

Проверить: `curl -I --http2 https://argymaq.kg/`.

## 32. Cache-Control на uploads

```nginx
location ~* ^/wp-content/uploads/.*\.(jpg|jpeg|png|gif|webp|svg|ico|css|js|woff2?)$ {
    expires 365d;
    add_header Cache-Control "public, immutable";
}
```

## 33. Заголовки безопасности

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "SAMEORIGIN" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
```

## 34. Скрыть версию PHP

```ini
expose_php = Off
```

И в nginx: `server_tokens off;`

## Ожидаемый результат

| Метрика | Сейчас | После P2 |
|---|---|---|
| TTFB | 4,33 с | 0,5–1,0 с |
| Полная загрузка HTML | 5,1 с | 1,5–2,5 с |
| Вес страницы | 75–150 МБ | 2–5 МБ |
| Кэш статики | нет | 365 дней |
| HTTP | 1.1 | 2 или 3 |
| Заголовки безопасности | 0 | 4+ |

## Чек-лист P2

- [ ] Кэш страниц
- [ ] OPcache
- [ ] Redis
- [ ] CDN
- [ ] Lazy + fetchpriority
- [ ] Плагины вычищены
- [ ] CSS/JS объединены
- [ ] Локальные шрифты
- [ ] HTTP/2
- [ ] Cache-Control на uploads
- [ ] Заголовки безопасности
- [ ] Версии скрыты