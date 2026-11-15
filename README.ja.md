<!-- 言語：日本語。メイン README は英語です。 -->
<div align="center">

[English](README.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [中文](README.zh.md) · **日本語**

</div>

---

# argymaq-seo-case

**キルギスの観光サイトの完全な SEO 監査を、クライアント向けレポートとポートフォリオ事例にまとめました。**

公開サイト：**https://homgorn.github.io/argymaq-seo-case/**

![監査](https://img.shields.io/badge/監査-54%20件-critical) ![ページ](https://img.shields.io/badge/ページ-17-success) ![構成](https://img.shields.io/badge/Astro-5.18-ff5d01) ![ライセンス](https://img.shields.io/badge/ライセンス-MIT-blue)

---

## これは何か

**argymaq.kg**（キルギス・カラコルで乗馬ツアーを提供する事業者）の完全で再現可能な SEO 監査を、二つの成果物にしました。

1. **静的ウェブサイト**（Astro、17 ページ）。図表と「ビフォー／アフター」比較、段階別プランを交えて、平易な言葉で所見を説明します。SEO の専門知識がない事業主を読者として想定しています。
2. **完全なデータセット**。すべての測定、すべてのスクリプト、すべての出典を収録し、作業を再実行・検証できます。

事例は「**ビフォー → アフター**」として構成されています。何が見つかり、収益にとって何を意味し、何を最初に直すのか。

### 出発点の数値

| 指標 | ビフォー | 出典 |
|---|---|---|
| 1 ツアーページの画像重量 | **150.4 MB** | 実測、54 ファイルへの HEAD リクエスト |
| サーバー応答の中央値 | **4.33 秒** | 実測、5 回実行 |
| meta description | **14 ページ中 0 ページ** | 実測 |
| schema.org ブロック | **15 URL 中 0 件** | 実測 |
| 設置済みの解析ツール | **なし** | 実測 |
| 問い合わせフォーム | **0 件** | 実測 |

## 内容

```
argymaq-seo-case/
|-- site/                   レポートサイト本体（Astro 5 + Tailwind 4）
|   |-- src/pages/          17 ルート
|   |-- src/components/     MetricCard, BeforeAfter, Phase, PriceCard, Steps
|   |-- src/data/           サービス、プラン、事例データ（JSON）
|   `-- dist/               ビルド成果物（Git 管理外）
|-- docs/
|   |-- architecture/       サイト構成とデザインシステム
|   |-- reports/            事業主向けレポート（露 + 英）
|   |-- research/           市場価格、報告書のパターン、GEO、地図
|   `-- wiki/               すべての所見の多層 LLM ウィキ
|-- scripts/                監査を再現する 11 個の Python スクリプト
|-- research/               競合の生データとベンチマーク
`-- data/                   SQLite ナレッジベース + JSONL エクスポート
```

## クイックスタート

```bash
git clone https://github.com/homgorn/argymaq-seo-case.git
cd argymaq-seo-case/site
npm install
npm run dev        # ローカルプレビュー
npm run build      # dist/ へビルド
npm run check      # 型チェック
```

監査を再実行する：

```bash
python scripts/crawl_full.py
python scripts/site_checks.py
python scripts/images_head.py
python scripts/competitors.py
python scripts/benchmark.py
python scripts/build_kb.py
python scripts/verify_site.py
```

## ドキュメント

| 文書 | 内容 |
|---|---|
| [アーキテクチャ](docs/architecture/00-architecture.md) | 17 ページのサイトマップ、デザインシステム、データモデル |
| [スキル計画](docs/architecture/01-skill-plan.md) | どの段階で誰が担当するか |
| [レポート（露）](docs/reports/seo-audit-2026-11-15.md) | クライアントに提出した完全なレポート |
| [レポート（英）](docs/reports/seo-audit-2026-11-15.en.md) | 同じレポートの英語版 |
| [キルギスの価格](docs/research/market-prices-kr/00-prices.md) | ソム建ての市場価格、出典と日付付き |
| [クライアント報告](docs/research/client-reporting/00-reporting.md) | 読まれる報告書をどう書くか |
| [GEO / AI 検索](docs/research/geo-ai-search/00-geo.md) | ChatGPT・Perplexity・Google AI での可視性の測定 |
| [ローカル地図](docs/research/local-maps/00-maps.md) | 2GIS、Yandex マップ、Google ビジネスプロフィール |
| [事例の構成](docs/research/case-studies/00-case-study.md) | ポートフォリオが問い合わせを生む条件 |
| [ウィキ索引](docs/wiki/40-index-portfolio.md) | 全文書の相互リンク集 |

## 出典ラベル

| ラベル | 意味 |
|---|---|
| **[measured]** | 直接リクエストで確認済み。数値は再現可能 |
| **[reported]** | 出典 URL と日付を伴う外部情報 |
| **[inferred]** | 論理的推論であり、直接測定ではない |
| **[panel]** | 監査の権限では取得できなかったデータ |

数値の捏造はありません。データが無い箇所は、推測で埋めずに空白として明記します。

## ライセンス

MIT — [LICENSE](LICENSE) を参照。監査データとレポートは現状有姿で参照用に提供します。

`argymaq.kg` のサイトとブランドは各所有者に帰属します。本リポジトリは測定と提言を含み、そのコンテンツ自体は含みません。