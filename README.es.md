<!-- Language: Español. El README principal es el inglés. -->
<div align="center">

[English](README.md) · [Русский](README.ru.md) · **Español** · [Deutsch](README.de.md) · [Français](README.fr.md) · [中文](README.zh.md) · [日本語](README.ja.md)

</div>

---

# argymaq-seo-case

**Auditoría SEO completa de un sitio turístico kirguís, presentada como informe para el cliente y como caso de portafolio.**

Sitio en vivo: **https://homgorn.github.io/argymaq-seo-case/**

![Auditoría](https://img.shields.io/badge/auditoría-54%20problemas-critical) ![Páginas](https://img.shields.io/badge/páginas-17-success) ![Stack](https://img.shields.io/badge/Astro-5.18-ff5d01) ![Licencia](https://img.shields.io/badge/licencia-MIT-blue)

---

## Qué es

Una auditoría SEO completa y reproducible de **argymaq.kg**, un operador de excursiones a caballo en Karakol, Kirguistán, convertida en dos entregables:

1. **Un sitio web estático** (Astro, 17 páginas) que explica los hallazgos en lenguaje sencillo, con gráficos, comparativas «antes / después» y un plan por fases. Escrito para un propietario que no trabaja en SEO.
2. **El conjunto completo de datos**: cada medición, cada script y cada fuente, para que el trabajo pueda repetirse y verificarse.

El caso se presenta como **antes → después**: qué se encontró, qué significa para los ingresos y qué se corrige primero.

### Los números iniciales

| Métrica | Antes | Fuente |
|---|---|---|
| Peso de imágenes en una página de tour | **150,4 MB** | medido, peticiones HEAD a 54 archivos |
| Tiempo de respuesta mediano | **4,33 s** | medido, 5 ejecuciones |
| Meta descriptions | **0 de 14 páginas** | medido |
| Bloques schema.org | **0 en 15 URLs** | medido |
| Analítica instalada | **ninguna** | medido |
| Formularios de contacto | **0** | medido |

## Contenido

```
argymaq-seo-case/
|-- site/                   sitio de informe (Astro 5 + Tailwind 4)
|   |-- src/pages/          17 rutas
|   |-- src/components/     MetricCard, BeforeAfter, Phase, PriceCard, Steps
|   |-- src/data/           servicios, paquetes, datos del caso en JSON
|   `-- dist/               salida de compilación (fuera de git)
|-- docs/
|   |-- architecture/       arquitectura del sitio y sistema de diseño
|   |-- reports/            informe para el propietario (RU + EN)
|   |-- research/           precios de mercado, patrones de informes, GEO, mapas
|   `-- wiki/               wiki multinivel de todos los hallazgos
|-- scripts/                11 scripts de Python que reproducen la auditoría
|-- research/               datos crudos de competidores y benchmark
`-- data/                   base de conocimiento SQLite + export JSONL
```

## Inicio rápido

```bash
git clone https://github.com/homgorn/argymaq-seo-case.git
cd argymaq-seo-case/site
npm install
npm run dev        # vista previa local
npm run build      # compilación en dist/
npm run check      # verificación de tipos
```

Repetir la auditoría:

```bash
python scripts/crawl_full.py
python scripts/site_checks.py
python scripts/images_head.py
python scripts/competitors.py
python scripts/benchmark.py
python scripts/build_kb.py
python scripts/verify_site.py
```

## Documentación

| Documento | Contenido |
|---|---|
| [Arquitectura](docs/architecture/00-architecture.md) | mapa de 17 páginas, sistema de diseño, modelo de datos |
| [Plan por especialidades](docs/architecture/01-skill-plan.md) | quién se aplica en cada etapa |
| [Informe (RU)](docs/reports/seo-audit-2026-11-15.md) | informe completo entregado al cliente |
| [Informe (EN)](docs/reports/seo-audit-2026-11-15.en.md) | edición en inglés del mismo informe |
| [Precios, Kirguistán](docs/research/market-prices-kr/00-prices.md) | tarifas de mercado en som, con fuentes y fechas |
| [Informes al cliente](docs/research/client-reporting/00-reporting.md) | cómo las agencias presentan informes que se leen |
| [GEO / búsqueda IA](docs/research/geo-ai-search/00-geo.md) | medir visibilidad en ChatGPT, Perplexity, Google AI |
| [Mapas locales](docs/research/local-maps/00-maps.md) | Yandex Maps, 2GIS, Google Business Profile |
| [Estructura del caso](docs/research/case-studies/00-case-study.md) | qué hace que un portafolio convierta |
| [Índice del wiki](docs/wiki/40-index-portfolio.md) | todos los documentos con enlaces |

## Etiquetas de fuente

| Etiqueta | Significado |
|---|---|
| **[measured]** | verificado con una petición directa; la cifra es reproducible |
| **[reported]** | tomado de una fuente externa con URL y fecha |
| **[inferred]** | conclusión lógica, no una medición directa |
| **[panel]** | requiere acceso del que la auditoría no disponía |

Ninguna cifra es inventada. Donde no había datos, se indica el vacío, no una suposición.

## Licencia

MIT — ver [LICENSE](LICENSE). Los datos y los informes se ofrecen tal cual, como referencia.

El sitio `argymaq.kg` y su marca pertenecen a su propietario. Este repositorio contiene mediciones y recomendaciones, no su contenido.