---
title: 'Hermes Liquidity World Model (HLWM)'
description: 'The HLWM is a proprietary Hermes framework that treats market liquidity as a spatial topology rather than a static number. It applies the pr'
pubDate: 2026-04-29
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/hermes-liquidity-world-model.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Liquidity World Model (HLWM)

The HLWM is a proprietary Hermes framework that treats market liquidity as a spatial topology rather than a static number. It applies the principles of **World Models** (causal simulation and physics) to the **Order Book**.

## The Hypothesis
Market liquidity acts as a physical environment with its own "physics":
- **Liquidity Wells**: High-density zones that exert "gravitational pull" on price.
- **Liquidity Vacuums**: Low-density gaps that cause "price acceleration".
- **Absorption Walls**: High-density areas that create "friction" and reverse trends.

## Proprietary Indicator: Liquidity Curvature ($\kappa_L$)
We define **Liquidity Curvature** to measure the acceleration of price through the liquidity space:

$$\kappa_L = \frac{\Delta \text{OFI} / \Delta t}{\text{Liquidity Density at } P_{current}}$$

### Logic Gates
- **Positive Curvature ($\kappa_L \gg 0$)**: Signal of a "Liquidity Vacuum". Price is likely to accelerate rapidly in the direction of the imbalance.
- **Negative Curvature ($\kappa_L \ll 0$)**: Signal of "Absorption/Friction". Price is likely to stall or reverse despite aggressive order flow.

## Execution Strategy
**High Confidence Entry** $\rightarrow$ `(Curvature $\kappa_L$ High) AND (Macro Trend Aligned) AND (Order Flow Imbalance $\text{OFI} > \text{Threshold}$)`.

## Related Concepts
- [[order-flow-imbalance]]
- [[world-models]]
