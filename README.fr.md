<!-- Langue : français. Le README principal est l'anglais. -->
<div align="center">

[English](README.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · **Français** · [中文](README.zh.md) · [日本語](README.ja.md)

</div>

---

# argymaq-seo-case

**Audit SEO complet d'un site touristique kirghize, présenté comme rapport client et étude de cas de portfolio.**

Site en ligne : **https://homgorn.github.io/argymaq-seo-case/**

![Audit](https://img.shields.io/badge/audit-54%20problèmes-critical) ![Pages](https://img.shields.io/badge/pages-17-success) ![Stack](https://img.shields.io/badge/Astro-5.18-ff5d01) ![Licence](https://img.shields.io/badge/licence-MIT-blue)

---

## De quoi il s'agit

Un audit SEO complet et reproductible de **argymaq.kg** — un opérateur de randonnées équestres à Karakol, au Kirghizistan — décliné en deux livrables :

1. **Un site web statique** (Astro, 17 pages) qui explique les résultats en langage simple, avec des graphiques, des comparaisons « avant / après » et un plan par phases. Écrit pour un propriétaire qui ne travaille pas dans le SEO.
2. **Le jeu de données complet** : chaque mesure, chaque script et chaque source, pour que le travail soit vérifiable.

Le cas est présenté comme **avant → après** : ce qui a été trouvé, ce que cela signifie pour le chiffre d'affaires et ce qui est corrigé en premier.

### Les chiffres de départ

| Indicateur | Avant | Source |
|---|---|---|
| Poids des images sur une page de tour | **150,4 Mo** | mesuré, requêtes HEAD sur 54 fichiers |
| Temps de réponse médian | **4,33 s** | mesuré, 5 exécutions |
| Meta descriptions | **0 sur 14 pages** | mesuré |
| Blocs schema.org | **0 sur 15 URL** | mesuré |
| Analytics installé | **aucun** | mesuré |
| Formulaires de contact | **0** | mesuré |

## Contenu

```
argymaq-seo-case/
|-- site/                   site de rapport statique (Astro 5 + Tailwind 4)
|   |-- src/pages/          17 routes
|   |-- src/components/     MetricCard, BeforeAfter, Phase, PriceCard, Steps
|   |-- src/data/           services, forfaits, données du cas en JSON
|   `-- dist/               sortie de build (hors git)
|-- docs/
|   |-- architecture/       architecture du site et système de design
|   |-- reports/            rapport destiné au propriétaire (RU + EN)
|   |-- research/           prix du marché, modèles de rapports, GEO, cartes
|   `-- wiki/               wiki multiniveau de toutes les conclusions
|-- scripts/                11 scripts Python qui reproduisent l'audit
|-- research/               données brutes des concurrents et benchmark
`-- data/                   base de connaissances SQLite + export JSONL
```

## Démarrage rapide

```bash
git clone https://github.com/homgorn/argymaq-seo-case.git
cd argymaq-seo-case/site
npm install
npm run dev        # aperçu local
npm run build      # build dans dist/
npm run check      # vérification des types
```

Relancer l'audit :

```bash
python scripts/crawl_full.py
python scripts/site_checks.py
python scripts/images_head.py
python scripts/competitors.py
python scripts/benchmark.py
python scripts/build_kb.py
python scripts/verify_site.py
```

## Documentation

| Document | Contenu |
|---|---|
| [Architecture](docs/architecture/00-architecture.md) | plan de 17 pages, système de design, modèle de données |
| [Plan de compétences](docs/architecture/01-skill-plan.md) | qui intervient à quelle étape |
| [Rapport (RU)](docs/reports/seo-audit-2026-11-15.md) | rapport complet remis au client |
| [Rapport (EN)](docs/reports/seo-audit-2026-11-15.en.md) | édition anglaise du même rapport |
| [Prix, Kirghizistan](docs/research/market-prices-kr/00-prices.md) | tarifs du marché en som, avec sources et dates |
| [Rapports clients](docs/research/client-reporting/00-reporting.md) | comment les agences présentent des rapports lus |
| [GEO / recherche IA](docs/research/geo-ai-search/00-geo.md) | mesurer la visibilité dans ChatGPT, Perplexity, Google AI |
| [Cartes locales](docs/research/local-maps/00-maps.md) | Yandex Maps, 2GIS, Google Business Profile |
| [Structure du cas](docs/research/case-studies/00-case-study.md) | ce qui rend un portfolio convertissant |
| [Index du wiki](docs/wiki/40-index-portfolio.md) | tous les documents avec liens |

## Marqueurs de source

| Marqueur | Signification |
|---|---|
| **[measured]** | vérifié par une requête directe ; le chiffre est reproductible |
| **[reported]** | issu d'une source externe avec URL et date |
| **[inferred]** | conclusion logique, pas une mesure directe |
| **[panel]** | nécessite un accès dont l'audit ne disposait pas |

Aucun chiffre n'est inventé. Là où les données manquaient, l'écart est indiqué, pas comblé.

## Licence

MIT — voir [LICENSE](LICENSE). Les données et les rapports sont fournis en l'état, pour référence.

Le site `argymaq.kg` et sa marque appartiennent à leur propriétaire. Ce dépôt contient des mesures et des recommandations, pas leur contenu.