---
title: 'Liquidity-Volatility Divergence (LVD) Indicator'
description: 'The LVD indicator is a proprietary tool designed to detect early-stage liquidity crises and flash crash conditions by identifying divergence'
pubDate: 2026-05-27
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/LVD_Indicator.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Liquidity-Volatility Divergence (LVD) Indicator
# 流動性-波動率背離 (LVD) 指標

## 🔍 Concept Overview
# 🔍 概念概述
The LVD indicator is a proprietary tool designed to detect early-stage liquidity crises and flash crash conditions by identifying divergence between market volatility and exchange-level liquidity flow.
# LVD 指標是一款專有的工具，旨在透過識別市場波動率與交易所級流動性流向之間的背離，來檢測早期流動性危機和閃崩條件。

## 🛠️ Map-Trigger-Lock Framework
# 🛠️ Map-Trigger-Lock 框架

### 🗺️ Map (Input Components)
# 🗺️ Map (輸入組件)
* **[Macro Volatility Index]**: Tracking systemic volatility (e.g., VIX, MOVE).
  **[宏觀波動率指數]**：追踪系統性波動（如 VIX、MOVE）。
* **[Exchange Order Flow Imbalance]**: Measuring the delta between aggressive buy-side and sell-side hitting of the limit order book.
  **[交易所訂單流不平衡]**：衡量激進買方與賣方對限價訂單簿衝擊之間的差值。

### ⚡ Trigger (Signal Condition)
# ⚡ Trigger (信號條件)
* **[Spread Widening]**: Rapid expansion of Bid-Ask spreads in highly liquid assets.
  **[價差擴大]**：高流動性資產中買賣價差的快速擴張。
* **[Directionless Aggression]**: High volume of aggressive market orders hitting both sides of the book without a sustained price trend.
  **[無方向性的激進行為]**：大量激進的市價單同時衝擊訂單簿兩側，但沒有持續的價格趨勢。

### 🔒 Lock (Actionable Response)
# 🔒 Lock (可操作反應)
* **[Automatic Risk Reduction]**: Upon a confirmed LVD signal, automatically reduce the Risk Budget allocated in VIP reports by 30% to preserve capital.
  **[自動風險降低]**：一旦確認 LVD 信號，自動將 VIP 報告中分配的風險預算降低 30%，以保存資本。

## 🎯 Strategic Value
# 🎯 戰略價值
Provides an early warning system for high-leverage environments, allowing for preemptive de-risking before liquidity-driven price cascades occur.
# 為高槓桿環境提供早期預警系統，允許在流動性驅動的價格連鎖反應發生前進行預防性去風險。
