---
title: 'Liquidity Geometric Divergence Gate (LGDG)'
description: 'The LGDG is a proprietary Hermes judgment logic designed to identify "Structural Liquidity Traps"—regimes where the market''s relational subs…'
pubDate: 2026-05-24
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/liquidity-geometric-divergence-gate-2026-05-24.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Liquidity Geometric Divergence Gate (LGDG)

## 1. Concept Overview
The LGDG is a proprietary Hermes judgment logic designed to identify **"Structural Liquidity Traps"**—regimes where the market's relational substrate is undergoing intense geometric deformation (**Shear**) without corresponding price discovery (**Drift**). These regimes often precede a catastrophic liquidity collapse or a violent volatility breakout.

It moves beyond traditional volume imbalance metrics by monitoring the *geometric quality* and *structural stability* of the Limit Order Book (LOB) as a projected density.

## 2. The Map-Trigger-Lock Framework

The LGDG utilizes the **Map-Trigger-Lock** framework to ensure deterministic execution and filter out microstructure noise.

### A. Map (Macro): The Volatility-Regime Context
The LGDG is only active when the macro environment provides a "fragility context."
- **Regime Context**: High Macro Uncertainty or Low-Liquidity Environments (e.g., "Stagflationary Bind" or "Policy Paralysis").
- **Variable**: Macro Volatility ($\sigma_{macro}$) or Liquidity-to-GDP indicators.
- **Purpose**: To ensure the logic is applied when "Shear" represents structural weakness rather than healthy, high-volume price discovery.

### B. Trigger (Micro): Shear Acceleration ($\alpha_{shear}$)
The trigger is not the presence of Shear, but its *acceleration*.
- **Metric**: The second derivative of the **Shear-to-Drift Ratio (SDR)**.
- **Signal**: $\frac{d^2}{dt^2} \left( \frac{\text{Shear}}{\text{Drift}} \right) > \Theta_{crit}$.
- **Interpretation**: The liquidity profile is "warping" (changing shape/density) at an accelerating rate without a corresponding translation of the mid-price. This indicates that liquidity is being repositioned (likely being pulled) rather than being consumed.

### C. Lock (Confirmation): Spectral Gap Contraction ($\Delta\lambda$)
To prevent false positives from transient LOB noise, the trigger must be confirmed by a fundamental change in the relational connectivity of the market.
- **Metric**: The **Spectral Gap** ($\lambda_2 - \lambda_1$) of the Liquidity Graph Laplacian.
- **Signal**: A rapid, significant contraction in the spectral gap.
- **Interpretation**: A contraction in the spectral gap signifies that the "connectedness" of the liquidity-providing vertices is breaking down. The market is transitioning from a continuous, stable manifold to a fragmented, disconnected state—a precursor to "price teleportation" (gaps).

## 3. Strategic Utility

| Application | Objective |
| :--- | :--- |
| **Risk Management** | Early warning for "Flash Crash" or "Liquidity Void" scenarios. |
| **Execution Strategy** | Avoidance of high-Shear/low-Lock environments to minimize market impact and slippage. |
| **Alpha Generation** | Identifying "Structural Traps" where price is likely to react violently to the next micro-imbalance. |

---
*Developed by CTO - Pillar 4: Innovation Research (2026-05-24)*
