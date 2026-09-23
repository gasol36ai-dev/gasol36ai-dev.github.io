---
title: 'Physical AI & Spatial Intelligence (2026 Update)'
description: 'Physical AI represents the transition from symbolic/digital intelligence to embodied intelligence. The core objective is the ability to perc'
pubDate: 2026-05-13
category: 'invest'
topic: 'ai-robotics'
tags: ['AI與機器人']
draft: false
source: 'knowledge/investment/Technical_Analysis/Physical_AI.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Physical AI & Spatial Intelligence (2026 Update)

## Overview
Physical AI represents the transition from symbolic/digital intelligence to embodied intelligence. The core objective is the ability to perceive 3D structure, reason about object relationships, and act under physical constraints in real-time.

## Key Breakthroughs (May 2026)

### 1. Embodied Reasoning & Spatial Intelligence
- **Gemini Robotics-ER 1.6**: Focuses on "reasoning-first" robotics. Key capabilities include:
    - **Instrument Reading**: Ability to interpret circular gauges and vertical level indicators via agentic vision (zoom -> point -> code execution -> interpretation).
    - **Relational Logic**: Defining "from-to" relationships and constraint compliance (e.g., "objects small enough to fit in a blue cup").
    - **Multi-view Reasoning**: Integrating multiple camera streams to understand dynamic or occluded environments.
- **SpatialEvo**: A self-evolving framework for 3D spatial reasoning. It uses **Deterministic Geometric Environments (DGE)** where ground truth is computable from point clouds and camera poses, eliminating the need for expensive human annotation.

### 2. World Models for Physical Manipulation
- **Dexterity's 'Foresight'**: A physics-consistent world model designed for production-scale manipulation (e.g., 4D box packing for truck loading).
    - **4D Reasoning**: Reasons across 3 spatial dimensions + time.
    - **Combinatorial Optimization**: Optimizes density, stability, and reachability in <400ms.
- **RAYNOVA**: A scale-temporal autoregressive world model using **Plücker-ray positional encoding**. It avoids strong 3D geometric priors, allowing it to generalize across diverse camera setups and ego-motions without explicit 3D scene representations.

## Strategic Implications
- **From Perception to Agency**: The gap is being closed by moving from "symbolic grounding" (image-to-text) to "spatial grounding" (metric understanding of geometry/physics).
- **The Role of World Models**: Essential for safe deployment across micro-to-macro scales, allowing agents to simulate the result of an action before executing it in the physical world.
