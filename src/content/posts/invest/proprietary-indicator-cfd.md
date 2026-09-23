---
title: 'Proprietary Indicator: Consensus Fidelity Divergence (CFD)'
description: 'The indicator monitors the interplay between three fundamental dimensions of agentic intelligence:'
pubDate: 2026-05-27
category: 'invest'
topic: 'ai-robotics'
tags: ['AI與機器人']
draft: false
source: 'knowledge/research/Proprietary_Indicator_CFD.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Proprietary Indicator: Consensus Fidelity Divergence (CFD)

**Date**: 2026-05-27
**Status**: Formalized
**Framework**: Map-Trigger-Lock

## Overview
**Consensus Fidelity Divergence (CFD)** is a meta-reasoning indicator designed to monitor the health and decision-quality of multi-agent autonomous systems. It identifies "Reasoning Loops" or "Information Deadlocks" where the system expends increasing computational effort (higher complexity) without achieving a stable, high-confidence consensus, often due to a lack of novel information (low entropy).

## Framework (Map-Trigger-Lock)

### 1. Map (Structural/Strategic Context)
The indicator monitors the interplay between three fundamental dimensions of agentic intelligence:
- **$\text{Consensus Strength} (C)$**: The mathematical degree of agreement among participating agents (e.g., via semantic similarity of outputs or overlap in decision vectors).
- **$\text{Reasoning Complexity} (R)$**: The depth and density of the reasoning traces produced (e.g., average number of steps in the Chain-of-Thought or total tokens used in the deliberation phase).
- **$\text{Information Entropy} (H)$**: The diversity and novelty of the data sources and perspectives currently held within the agent collective.

### 2. Trigger (Operational/Micro-Signal)
A **CFD Signal** is triggered when the system enters a state of **"Computational Friction"**:
$$\text{CFD Signal} \iff [\text{Low } C] + [\text{High } R] + [\text{Low } H]$$

*In plain terms: The agents are arguing intensely (High $R$), but they cannot agree (Low $C$), and they are doing so because they are trapped in a narrow, repetitive information loop (Low $H$).*

### 3. Lock (Risk Management & Response)
Upon detection of a CFD signal, the system automatically executes the following **"Resilience Protocols"**:
- **Protocol A: Information Injection (Break the Loop)**: Immediately suspend internal debate and trigger a high-priority external research task (e.g., via `web_search` or `browser_navigate`) to fetch high-fidelity, non-redundant data.
- **Protocol B: Diversity Expansion (Re-introduce Entropy)**: Deploy new "Outlier Agents" with specialized tools, different personas (e.g., "Devil's Advocate"), or different retrieval capabilities to introduce new perspectives into the consensus pool.

## Strategic Value
- **Preventing "Agentic Groupthink"**: Ensures that consensus is driven by truth/evidence rather than mere agreement.
- **Resource Efficiency**: Identifies and breaks expensive, unproductive reasoning loops before they consume excessive compute/token budgets.
- **System Reliability**: Provides a deterministic mechanism for self-correction in complex, multi-step autonomous workflows.

---
**Formalized**: 2026-05-27
