---
title: 'HPI-4: Geometric-Macro Fragility (GMF)'
description: 'The Geometric-Macro Fragility (GMF) indicator is a high-order synthetic judgment metric. It moves beyond traditional volume/price imbalance …'
pubDate: 2026-05-24
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/HPI-4-Geometric-Macro-Fragility.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# HPI-4: Geometric-Macro Fragility (GMF)

## 1. Overview
The **Geometric-Macro Fragility (GMF)** indicator is a high-order synthetic judgment metric. It moves beyond traditional volume/price imbalance by monitoring the **topological stability** of the market's liquidity manifold, specifically looking for "Structural Traps" where the market's geometry is deforming (Shear) without moving (Drift) in a fragile macro regime.

## 2. The Logic: The "Shear-Regime Trap"
GMF detects the convergence of three critical signals:

### A. The Macro Map (Context)
- **Condition**: The market is in a **Fragmentation Regime** (High Trade Fragmentation + Rising Real Yields/Volatility).
- **Purpose**: In an "Expansion Regime," Shear is often just healthy price discovery. In a "Fragmentation Regime," Shear is a sign of structural decay.

### B. The Micro Trigger (Shear Acceleration)
- **Metric**: The acceleration of the **Shear-to-Drift Ratio (SDR)**.
- **Signal**: $\frac{d^2}{dt^2} \left( \frac{\text{Shear}}{\text{Drift}} \right) > \Theta_{crit}$.
- **Interpretation**: The LOB shape is warping at an increasing rate, but the mid-price is stagnant. This indicates liquidity is being "pulled" rather than "consumed."

### C. The Topological Lock (Spectral Gap Contraction)
- **Metric**: The **Spectral Gap** ($\Delta\lambda$) of the Liquidity Graph Laplacian.
- **Signal**: A rapid contraction in $\Delta\lambda$.
- **Interpretation**: The "connectedness" of market participants is breaking down. The manifold is fragmenting into disconnected clusters, making a "price teleportation" (gap) imminent.

## 3. Indicator Signal & Judgment

| Signal State | Macro Context | Micro Signal | Judgment | Action |
| :--- | :--- | :--- | :--- | :--- |
| **GMF ACTIVE** | **Fragmentation** | **High SDR Accel + $\Delta\lambda$ Contraction** | **"Structural Liquidity Trap"** | **Aggressive De-risking / Volatility Hedge** |
| GMF DORMANT | Expansion | Any | "Healthy Liquidity Provision" | Maintain Normal Execution |
| GMF DORMANT | Fragmentation | Low SDR / Stable $\Delta\lambda$ | "Stable Fragmentation" | Standard Micro-Alpha Strategies |

## 4. Implementation Requirements
- **Data Feed**: Level 3 (MBO) or high-granularity L2 data to reconstruct the relational graph.
- **Compute**: Real-time Graph Laplacian and Spectral Decomposition.
- **Integration**: Feed into the **Hermes-LMM (Large Market Model)** as a "Fragility Constraint" for the Actor and Strategist.

---
*Invented by CTO - Pillar 4: Innovation Research (2026-05-24)*
