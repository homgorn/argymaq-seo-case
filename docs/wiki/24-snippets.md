# 24 — готовые тексты для внедрения

Шаблоны, которые можно вставлять в SEO-плагин и на страницы.

## Meta description (12 страниц)

| Страница | Description (156–160 знаков) |
|---|---|
| `/` | Horseback riding tours in Karakol, Kyrgyzstan. 1–5 day routes to Altyn Arashan, Ala-Kul lake and Karakol gorge. Guesthouse, yurt camp, transfers. Book now! |
| `/our-tours/` | Horse riding tours from Karakol: 1, 2, 3, 4 and 5 day routes. Prices, program, what is included. Small groups, local guides. Book your tour online. |
| `/1-day-…-karakol-gorge/` | 1-day horseback riding tour in Karakol gorge from Karakol. Mountain views, forests, rivers. Lunch included. Price, program, booking. Season: May–October. |
| `/2-day-…-altyn-arashan/` | 2-day horse riding tour to Altyn Arashan: Ak-Suu valley, hot springs, overnight in a yurt camp. All meals included. Price, program, booking online. |
| `/4-day-…-program/` | 4-day horseback tour from Karakol to Ala-Kul lake via Altyn Arashan. Hot springs, glacier views, yurt stays. Price, detailed program, booking. |
| `/5-day-…-program/` | 5-day horseback riding tour: Karakol gorge, Ala-Kul lake, Altyn Arashan. Tents and yurts, full board, local guide. Price, itinerary, booking online. |
| `/guesthouse-and-yurt-camp/` | Guesthouse and yurt camp in Karakol, Kyrgyzstan. Cozy rooms, traditional yurts, mountain views, hospitality. Prices, photos, booking. Open all year. |
| `/airport-pickup/` | Airport pickup and transfer to Karakol: comfortable car, scenic stops, photo breaks. From Tamchy or Bishkek. Price, booking online, 24/7 support. |
| `/about-us/` | About ARGYMAQ — horse riding tours in Karakol since 2024. Local guides, trained horses, small groups. Our story, team, approach to horseback travel. |
| `/blog/` | Travel blog about horseback riding in Kyrgyzstan: Karakol, Altyn Arashan, Ala-Kul lake, seasons, gear, routes. Guides, tips and stories from our team. |
| `/contacts/` | Contacts of ARGYMAQ in Karakol: address, phone +996 501 282 030, WhatsApp, email, map. We are here to plan your horse riding tour in Kyrgyzstan. |
| `/reviews/` | Reviews of ARGYMAQ horse riding tours in Karakol. Real feedback from our guests: 1 to 5 day routes, yurt stays, guides, horses. Read and book your tour. |

## Title (12 страниц)

| Страница | Title (до 60 знаков) |
|---|---|
| `/` | Horseback Riding Tours in Karakol, Kyrgyzstan |
| `/our-tours/` | Horse Riding Tours from Karakol — 1 to 5 Days |
| `/1-day-…-karakol-gorge/` | 1-Day Horseback Riding Tour in Karakol Gorge |
| `/2-day-…-altyn-arashan/` | 2-Day Horse Riding Tour to Altyn Arashan |
| `/4-day-…-program/` | 4-Day Horseback Tour to Ala-Kul Lake from Karakol |
| `/5-day-…-program/` | 5-Day Horseback Riding Tour: Karakol to Ala-Kul |
| `/guesthouse-and-yurt-camp/` | Guesthouse and Yurt Camp in Karakol — Rooms & Prices |
| `/airport-pickup/` | Airport Pickup and Transfer to Karakol — Price |
| `/about-us/` | About ARGYMAQ — Horse Riding Tours in Karakol |
| `/blog/` | Karakol Travel Blog — Horse Riding, Altyn Arashan, Ala-Kul |
| `/contacts/` | Contacts — ARGYMAQ Horse Riding Tours in Karakol |
| `/reviews/` | Reviews — ARGYMAQ Horse Riding Tours in Karakol |

## H1 (12 страниц)

| Страница | H1 |
|---|---|
| `/` | Horseback Riding Tours in Karakol, Kyrgyzstan |
| `/our-tours/` | Horse Riding Tours from Karakol |
| `/1-day-…-karakol-gorge/` | 1-Day Horseback Riding Tour in Karakol Gorge |
| `/2-day-…-altyn-arashan/` | 2-Day Horse Riding Tour to Altyn Arashan |
| `/4-day-…-program/` | 4-Day Horseback Tour to Ala-Kul Lake |
| `/5-day-…-program/` | 5-Day Horseback Riding Tour: Karakol to Ala-Kul |
| `/guesthouse-and-yurt-camp/` | Guesthouse and Yurt Camp in Karakol |
| `/airport-pickup/` | Airport Pickup and Transfer to Karakol |
| `/about-us/` | About ARGYMAQ |
| `/blog/` | Karakol Travel Blog |
| `/contacts/` | Contacts |
| `/reviews/` | Guest Reviews |

## Alt для изображений (шаблон)

| Фото | Alt |
|---|---|
| Hero главной | Horseback rider on a mountain trail near Karakol, Kyrgyzstan |
| Иконка трансфера | Airport transfer from Tamchy to Karakol, Kyrgyzstan |
| Гостевой дом | Guesthouse room in Karakol, Kyrgyzstan |
| Юрточный лагерь | Yurt camp in Altyn Arashan valley, Kyrgyzstan |
| Лошади | Horses ready for a riding tour near Karakol |
| Ущелье Каракола | Karakol gorge: forest trail and mountain river |
| Алтын-Арашан | Altyn Arashan valley with hot springs, Kyrgyzstan |
| Ала-Куль | Ala-Kul lake at 3500 m, Tian Shan mountains |
| Перевал | Mountain pass on the Ala-Kul horse riding route |
| Лагерь | Campsite with tents in the mountains near Karakol |

Правило: `{объект} + {действие/место} + {локация}`.

## JSON-LD: Organization + LocalBusiness

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://argymaq.kg/#org",
      "name": "ARGYMAQ KYRGYZSTAN",
      "url": "https://argymaq.kg/",
      "logo": "https://argymaq.kg/wp-content/uploads/2026/07/logo.png",
      "sameAs": ["https://www.instagram.com/argymaq", "https://www.facebook.com/argymaq"]
    },
    {
      "@type": "TouristBusiness",
      "@id": "https://argymaq.kg/#business",
      "name": "ARGYMAQ KYRGYZSTAN",
      "image": "https://argymaq.kg/wp-content/uploads/2026/08/IMG_4185-_2_.png",
      "url": "https://argymaq.kg/",
      "telephone": "+996 501 282 030",
      "priceRange": "$$",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "6/1 Masaliev St",
        "addressLocality": "Karakol",
        "addressRegion": "Issyk-Kul",
        "postalCode": "722200",
        "addressCountry": "KG"
      },
      "geo": { "@type": "GeoCoordinates", "latitude": 42.4907, "longitude": 78.3936 },
      "openingHours": "Mo-Su 08:00-20:00",
      "areaServed": ["Karakol", "Issyk-Kul", "Altyn Arashan", "Ala-Kul"],
      "sameAs": ["https://argymaq.kg/#org"]
    }
  ]
}
```

## JSON-LD: TouristTrip (страница тура)

```json
{
  "@context": "https://schema.org",
  "@type": "TouristTrip",
  "name": "1-Day Horseback Riding Tour in Karakol Gorge",
  "description": "One day horseback riding in Karakol gorge from Karakol. Mountain views, spruce forests, alpine meadows, lunch included.",
  "url": "https://argymaq.kg/1-day-horseback-riding-tour-in-karakol-gorge/",
  "image": "https://argymaq.kg/wp-content/uploads/2026/08/IMG_6508.png",
  "touristType": ["Families", "Couples", "Solo travelers"],
  "itinerary": {
    "@type": "ItemList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "09:00 — Meeting in Karakol" },
      { "@type": "ListItem", "position": 2, "name": "10:00 — Start riding in Karakol gorge" },
      { "@type": "ListItem", "position": 3, "name": "13:00 — Lunch on the trail" },
      { "@type": "ListItem", "position": 4, "name": "16:00 — Return to Karakol" }
    ]
  },
  "provider": { "@id": "https://argymaq.kg/#business" },
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://argymaq.kg/1-day-horseback-riding-tour-in-karakol-gorge/"
  }
}
```

## JSON-LD: FAQPage

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need horse riding experience?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. Our horses are calm and trained. A guide leads the group and gives a safety briefing before the ride." }
    },
    {
      "@type": "Question",
      "name": "What is the minimum age?",
      "acceptedAnswer": { "@type": "Answer", "text": "Children from 7 years can ride with an adult. For longer routes the recommended age is 12+." }
    },
    {
      "@type": "Question",
      "name": "What should I bring?",
      "acceptedAnswer": { "@type": "Answer", "text": "Long trousers, closed shoes with a small heel, a warm jacket, rain protection, sunglasses, sunscreen and a water bottle." }
    },
    {
      "@type": "Question",
      "name": "What is the best season?",
      "acceptedAnswer": { "@type": "Answer", "text": "May to October. Winter routes are also possible for experienced riders." }
    },
    {
      "@type": "Question",
      "name": "Is insurance included?",
      "acceptedAnswer": { "@type": "Answer", "text": "Basic insurance is included for multi-day tours. We recommend additional travel insurance for all guests." }
    }
  ]
}
```

## robots.txt (улучшенный)

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /?s=
Disallow: /search/
Disallow: /*?replytocom=
Disallow: /tag/
Crawl-delay: 1

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

Sitemap: https://argymaq.kg/wp-sitemap.xml
```

## nginx: gzip + кэш + безопасность

```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/rss+xml image/svg+xml;

brotli on;
brotli_comp_level 5;
brotli_types text/plain text/css application/json application/javascript text/xml application/xml image/svg+xml;

server_tokens off;

add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "SAMEORIGIN" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;

location ~* ^/wp-content/uploads/.*\.(jpg|jpeg|png|gif|webp|svg|ico|css|js|woff2?)$ {
    expires 365d;
    add_header Cache-Control "public, immutable";
}

location ~* \.(css|js)$ {
    expires 30d;
    add_header Cache-Control "public";
}

location ~* \.(jpg|jpeg|png|gif|webp|svg|ico)$ {
    expires 180d;
    add_header Cache-Control "public";
}
```

## .htaccess (если Apache)

```apache
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/plain text/html text/css application/javascript application/json image/svg+xml
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
</IfModule>

<IfModule mod_headers.c>
  Header set Strict-Transport-Security "max-age=31536000; includeSubDomains"
  Header set X-Content-Type-Options "nosniff"
  Header set X-Frame-Options "SAMEORIGIN"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>