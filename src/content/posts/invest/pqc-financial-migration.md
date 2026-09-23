---
title: 'Post-Quantum Cryptography (PQC) & Financial Rail Migration'
description: 'The advent of Cryptographically Relevant Quantum Computers (CRQC) poses an existential threat to the asymmetric encryption (RSA, ECC) that s…'
pubDate: 2026-06-02
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/PQC_Financial_Migration.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Post-Quantum Cryptography (PQC) & Financial Rail Migration

## 1. Executive Summary
The advent of Cryptographically Relevant Quantum Computers (CRQC) poses an existential threat to the asymmetric encryption (RSA, ECC) that secures global financial rails. The industry is transitioning to Post-Quantum Cryptography (PQC)—algorithms resistant to Shor’s algorithm—to prevent systemic collapse and mitigate the "Harvest Now, Decrypt Later" (HNDL) risk.

## 2. The Threat Landscape: HNDL
The "Harvest Now, Decrypt Later" paradigm is the primary driver for immediate migration. Adversaries are currently intercepting and archiving encrypted financial traffic. While they cannot decrypt it today, this data will be retroactively decrypted once a CRQC becomes available, exposing long-term secrets, sovereign debt records, and historical transaction data.

## 3. Standardized Algorithms (NIST)
In August 2024, NIST finalized the first set of PQC standards:
- **ML-KEM (FIPS 203)**: Module-Lattice-Based Key-Encapsulation Mechanism (formerly CRYSTALS-Kyber). Used for secure key exchange.
- **ML-DSA (FIPS 204)**: Module-Lattice-Based Digital Signature Algorithm (formerly CRYSTALS-Dilithium). Used for identity and authentication.
- **SLH-DSA (FIPS 205)**: Stateless Hash-Based Digital Signature Algorithm (formerly SPHINCS+). A fallback option with different mathematical assumptions.

## 4. Global Migration Timelines & Mandates
### 4.1 European Union (EU)
- **Start Date**: Member States are urged to begin transition activities by **end-2026**.
- **Compliance Deadline**: High-risk systems, including critical financial infrastructure, must be PQC-secured by **end-2030**.
- **Regulatory Drivers**: 
    - **DORA (Digital Operational Resilience Act)**: Effective Jan 2025; mandates "crypto-agility"—the ability to rapidly swap algorithms without system overhauls.
    - **NIS2 Directive**: Requires "state-of-the-art" security controls, which increasingly includes quantum-readiness.

### 4.2 United States (US)
- **CNSA 2.0**: The NSA's Commercial National Security Algorithm Suite 2.0 sets milestones for 2030–2035 for all National Security Systems.
- **Federal Mandates**: NSM-10 and EO 14144 require government contractors and agencies to prioritize PQC migration.

## 5. Financial Rail Integration
### 5.1 SWIFT & Cross-Border Rails
SWIFT is coordinating the transition to PQC through pilot programs and the evolution of SwiftNet. The migration is often synchronized with the **ISO 20022** transition, as structured data allows for better cryptographic inventory and agility.

### 5.2 FedWire & CHIPS
US domestic rails are focusing on hybrid key exchange (combining classical ECC with ML-KEM) to ensure backward compatibility while providing quantum protection.

## 6. Implementation Strategy
Financial institutions are adopting a phased approach:
1. **Cryptographic Inventory**: Creating a "Cipher Bill of Materials" (CBOM) to identify every instance of RSA/ECC.
2. **Hybrid Transition**: Implementing "Hybrid Schemes" (Classical + PQC) to maintain current compliance while layering quantum resistance.
3. **Crypto-Agility**: Abstracting the cryptographic layer from the application logic to allow for seamless algorithm updates as standards evolve.
