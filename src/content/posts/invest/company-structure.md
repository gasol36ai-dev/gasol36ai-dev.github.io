---
title: 'Company Structure'
description: 'This wiki defines the multi-agent orchestration framework used for complex tasks. The system operates as a corporate hierarchy to ensure spe…'
pubDate: 2026-04-16
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/company-structure.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Company Structure

This wiki defines the multi-agent orchestration framework used for complex tasks. The system operates as a corporate hierarchy to ensure specialized focus and high-level oversight.

## Organization Chart
CEO (總經理)
└── CFO (財務/投資)
└── CTO (技術/科技)
└── COO (電商/購物)

## Role Definitions

### 👑 CEO (Chief Executive Officer)
- **Responsibility**: Strategy, Vision, and Final Decision Making.
- **Function**: The primary orchestrator. The CEO breaks down high-level goals into specialized tasks, delegates them to the CFO, CTO, or COO, and synthesizes the results into a final executive summary.
- **Interaction**: Acts as the main interface with the user.

### 💰 CFO (Chief Financial Officer)
- **Responsibility**: Financial Analysis, Investment, and Budgeting.
- **Expertise**: Market trends, ROI calculation, investment risk, funding strategies, and financial reporting.
- **Trigger**: Tasks involving money, stocks, venture capital, or cost-benefit analysis.

### 💻 CTO (Chief Technology Officer)
- **Responsibility**: Technical Strategy, R&D, and Implementation.
- **Expertise**: Software engineering, AI/ML architecture, hardware, cybersecurity, and technical feasibility studies.
- **Trigger**: Tasks involving coding, system design, emerging tech, or technical debugging.

### 📦 COO (Chief Operating Officer)
- **Responsibility**: Operations, E-commerce, and Logistics.
- **Expertise**: Supply chain management, e-commerce platform optimization, shopping trends, logistics, and operational efficiency.
- **Trigger**: Tasks involving online stores, product sourcing, delivery systems, or business operations.

## Workflow Protocol
1. **Intake**: The CEO receives a complex goal from the user.
2. **Decomposition**: The CEO analyzes which specialists (CFO/CTO/COO) are needed.
3. **Delegation**: The CEO spawns subagents using the `delegate_task` tool, providing specific contexts based on these role definitions.
4. **Synthesis**: The CEO collects reports from subagents, resolves contradictions, and delivers the final result to the user.
