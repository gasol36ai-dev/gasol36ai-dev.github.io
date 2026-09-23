---
title: 'Hermes Spatial-Wave Indicator (HSWI)'
description: 'The HSWI is the evolved successor to the Hermes Judgment Indicator (HJI). It synthesizes structural wave analysis, spatial liquidity mapping…'
pubDate: 2026-04-25
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/HSWI.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Hermes Spatial-Wave Indicator (HSWI)

The HSWI is the evolved successor to the Hermes Judgment Indicator (HJI). It synthesizes structural wave analysis, spatial liquidity mapping, and macro volatility to create a high-conviction signal.

## The HSWI Framework

$$\text{HSWI} = (\text{S} \times \text{W}) \times \text{HJI}$$

### 1. Spatial Component (S) - "Liquidity Gravity"
Analyzes the proximity of price to "Gravity Wells" (Unmitigated Order Blocks and Iceberg levels identified via MBO data).
- **S = 1.5**: Price is entering a high-conviction Gravity Well.
- **S = 0.5**: Price is in "No Man's Land" (low liquidity).

### 2. Wave Component (W) - "Structural Phase"
Derived from NEoWave structural analysis.
- **W = 1.2 (Motive)**: Price is in a motive wave; trend signals are amplified.
- **W = 1.8 (Corrective)**: Price is in a corrective wave; reversal signals are amplified.

### 3. Base Signal (HJI)
The original Hermes Judgment Indicator (Delta Divergence $\times$ Macro Volatility).

## Logic Gates for Execution

| Phase (W) | Spatial (S) | HJI Signal | Outcome | Action |
| :--- | :--- | :--- | :--- | :--- |
| Motive | Gravity Well | Trend-Following | **High Conviction Trend** | Long/Short with Trend |
| Corrective | Gravity Well | Divergence | **High Conviction Reversal** | Mean Reversion Trade |
| Any | No Man's Land | Any | **Low Conviction** | No Trade / Wait |

## Strategic Advantage
The HSWI eliminates "false divergences" by requiring both a **Structural Reason** (NEoWave) and a **Spatial Reason** (Liquidity Gravity) before triggering a trade.
