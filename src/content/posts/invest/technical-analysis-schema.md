---
title: 'Wiki Schema: Investment Technical Analysis'
description: 'Frontier Technical Analysis (TA) and Quantitative Trading strategies, focusing on Order Flow, Market Profile, and Wave Theory.'
pubDate: 2026-05-04
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/investment/Technical_Analysis/SCHEMA.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Wiki Schema: Investment Technical Analysis

## Domain
Frontier Technical Analysis (TA) and Quantitative Trading strategies, focusing on Order Flow, Market Profile, and Wave Theory.

## Conventions
- File names: lowercase, hyphens, no spaces.
- Every wiki page starts with YAML frontmatter.
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page).
- When updating a page, always bump the `updated` date.
- Every new page must be added to `index.md` under the correct section.
- Every action must be appended to `log.md`.

## Frontmatter
```yaml
---
title: Page Title
created: 2026-05-04
updated: 2026-05-04
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
---
```

## Tag Taxonomy
- Analysis: order-flow, market-profile, neowave, wave-theory, quant, quant-strat
- Regime: volatility, trend, range, absorption, trap
- Asset: equity, crypto, fx, commodity
- Meta: breakdown, synthesis, strategy, prediction

## Page Thresholds
- Create a page when a concept appears in 2+ sources or is central to one source.
- Don't create a page for passing mentions.

## Update Policy
Newer sources supersede older ones. Contradictions are marked as `contested: true`.
