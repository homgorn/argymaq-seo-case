<!-- 语言：中文。主 README 为英文。 -->
<div align="center">

[English](README.md) · [Русский](README.ru.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · **中文** · [日本語](README.ja.md)

</div>

---

# argymaq-seo-case

**吉尔吉斯斯坦旅游网站的完整 SEO 审计，整理为面向客户的报告网站与作品集案例。**

在线站点：**https://homgorn.github.io/argymaq-seo-case/**

![审计](https://img.shields.io/badge/审计-54%20个问题-critical) ![页面](https://img.shields.io/badge/页面-17-success) ![技术栈](https://img.shields.io/badge/Astro-5.18-ff5d01) ![许可证](https://img.shields.io/badge/许可证-MIT-blue)

---

## 这是什么

对 **argymaq.kg** 的完整可复现 SEO 审计。该站是吉尔吉斯斯坦卡拉科尔的骑马旅行运营商。成果分为两部分：

1. **一个静态网站**（Astro，17 页），用通俗语言解释发现，配图表、前后对比和分阶段计划。写给完全不懂 SEO 的站长看。
2. **完整数据集**：每一次测量、每一个脚本、每一个来源，工作可复跑、可验证。

案例以**前 → 后**叙述：发现了什么、对收入意味着什么、先修哪一项。

### 起始数字

| 指标 | 前 | 来源 |
|---|---|---|
| 单个路线页的图片重量 | **150.4 MB** | 实测，对 54 个文件发 HEAD 请求 |
| 服务器响应中位数 | **4.33 秒** | 实测，5 次运行 |
| Meta description | **14 页中 0 页** | 实测 |
| schema.org 区块 | **15 个 URL 中 0 个** | 实测 |
| 已安装的分析工具 | **无** | 实测 |
| 联系表单 | **0 个** | 实测 |

## 目录结构

```
argymaq-seo-case/
|-- site/                   报告网站（Astro 5 + Tailwind 4）
|   |-- src/pages/          17 条路由
|   |-- src/components/     MetricCard, BeforeAfter, Phase, PriceCard, Steps
|   |-- src/data/           服务、套餐、案例数据（JSON）
|   `-- dist/               构建产物（不入库）
|-- docs/
|   |-- architecture/       站点架构与设计系统
|   |-- reports/            给站长的报告（俄语 + 英语）
|   |-- research/           市场价格、报告范式、GEO、地图
|   `-- wiki/               全部发现的多层 wiki
|-- scripts/                11 个复现审计的 Python 脚本
|-- research/               竞品原始数据与基准
`-- data/                   SQLite 知识库 + JSONL 导出
```

## 快速开始

```bash
git clone https://github.com/homgorn/argymaq-seo-case.git
cd argymaq-seo-case/site
npm install
npm run dev        # 本地预览
npm run build      # 构建到 dist/
npm run check      # 类型检查
```

重跑审计：

```bash
python scripts/crawl_full.py
python scripts/site_checks.py
python scripts/images_head.py
python scripts/competitors.py
python scripts/benchmark.py
python scripts/build_kb.py
python scripts/verify_site.py
```

## 文档

| 文档 | 内容 |
|---|---|
| [架构](docs/architecture/00-architecture.md) | 17 页站点地图、设计系统、数据模型 |
| [技能计划](docs/architecture/01-skill-plan.md) | 各阶段由谁执行 |
| [报告（俄语）](docs/reports/seo-audit-2026-11-15.md) | 交付给客户的完整报告 |
| [报告（英语）](docs/reports/seo-audit-2026-11-15.en.md) | 同一报告的英文版 |
| [吉尔吉斯斯坦价格](docs/research/market-prices-kr/00-prices.md) | 索姆计价的市场行情，附来源与日期 |
| [客户报告](docs/research/client-reporting/00-reporting.md) | 机构如何写出会被读完的报告 |
| [GEO / AI 搜索](docs/research/geo-ai-search/00-geo.md) | 在 ChatGPT、Perplexity、Google AI 中衡量可见度 |
| [本地地图](docs/research/local-maps/00-maps.md) | 2GIS、Yandex 地图、Google 商家资料 |
| [案例结构](docs/research/case-studies/00-case-study.md) | 什么样的作品集能带来询盘 |
| [Wiki 索引](docs/wiki/40-index-portfolio.md) | 全部文档及交叉引用 |

## 来源标记

| 标记 | 含义 |
|---|---|
| **[measured]** | 通过直接请求核实，数字可复现 |
| **[reported]** | 来自外部来源，附 URL 与日期 |
| **[inferred]** | 逻辑推断，非直接测量 |
| **[panel]** | 需要审计方没有的后台权限 |

没有编造的数字。数据缺失处直接标明空缺，而非以推测填补。

## 许可证

MIT — 见 [LICENSE](LICENSE)。审计数据与报告按现状提供，仅供参考。

`argymaq.kg` 网站及其品牌归其所有者所有。本仓库包含测量与建议，不包含其内容。