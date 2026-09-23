---
title: 'Quantum-Safe Finance: Sustaining & Security (2026)'
description: 'The financial sector faces an existential threat from Cryptographically Relevant Quantum Computers (CRQC). The transition to Post-Quantum Cr'
pubDate: 2026-07-10
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/reports/quantum_safe_finance_2026-07-10.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Quantum-Safe Finance: Sustaining & Security (2026)

## Executive Summary
The financial sector faces an existential threat from Cryptographically Relevant Quantum Computers (CRQC). The transition to Post-Quantum Cryptography (PQC) is not merely a software update but a fundamental re-architecting of the global financial rails. The focus has shifted from theoretical risk to the implementation of NIST FIPS standards (ML-KEM, ML-DSA, SLH-DSA) across sovereign data rails and ledger systems.

## Transmission Mapping: [Event] -> [Mechanism] -> [Reaction]

### 1. Foundational Cryptographic Collapse
- **[Event]** Deployment of Shor's Algorithm on scale $\ge 20$ million qubits.
- **[Mechanism]** Polynomial-time factorization of large integers and solution of discrete logarithms, rendering RSA, Diffie-Hellman, and ECC obsolete.
- **[Reaction]** Immediate migration to Lattice-based Cryptography (LBC) for asymmetric encryption and digital signatures.

### 2. Financial Ledger Vulnerability
- **[Event]** "Harvest Now, Decrypt Later" (HNDL) attacks on encrypted financial archives.
- **[Mechanism]** Interception of current TLS/SSL traffic for retrospective decryption once CRQC is available.
- **[Reaction]** Deployment of Hybrid Key Exchange (e.g., X25519 + ML-KEM) to ensure that data remains secure unless both classical and quantum-safe algorithms are broken.

### 3. Ledger Integrity & Transactional Trust
- **[Event]** Quantum-enabled signature forgery on legacy blockchain/DLT ledgers.
- **[Mechanism]** Derivation of private keys from public keys stored on-chain using quantum search/factorization.
- **[Reaction]** Transition to ML-DSA (Module-Lattice-Based Digital Signature Standard) and the implementation of "Quantum-Agile" ledger wrappers that allow for seamless signature algorithm rotation.

### 4. Sovereign Data Rail Evolution
- **[Event]** Launch of Quantum-Safe Sovereign Data Rails (National CBDC infrastructures).
- **[Mechanism]** Integration of PQC at the network layer (Layer 0) combined with Quantum Key Distribution (QKD) for backbone inter-bank connectivity.
- **[Reaction]** Creation of "Sovereign Trust Zones" where data transit is guarded by physically secure QKD links and logically secure PQC encapsulations.

### 5. Cross-Border Settlement (SWIFT/ISO 20022)
- **[Event]** Quantum-attack vector on inter-bank messaging protocols.
- **[Mechanism]** Compromise of the Public Key Infrastructure (PKI) used for authenticating high-value cross-border transfers.
- **[Reaction]** Global mandate for "Cryptographic Agility" in ISO 20022 messages, enabling the transport of multiple signature types (Classical + PQC) during the transition window.

## Technical Specifications: NIST PQC Standards (2024-2026)

| Standard | Name | Primary Use Case | Mathematical Basis |
| :--- | :--- | :--- | :--- |
| **FIPS 203** | **ML-KEM** | Key Encapsulation (KEM) | Module-Lattice (LWE) |
| **FIPS 204** | **ML-DSA** | General Digital Signatures | Module-Lattice (LWE) |
| **FIPS 205** | **SLH-DSA** | High-Security/Backup Signatures | Stateless Hash-Based |

## Transition Timeline & Implementation Strategy

### Phase I: Inventory & Assessment (2024 - 2026)
- **Focus:** Identification of all quantum-vulnerable assets (CVE-Q).
- **Action:** Mapping the "Cryptographic Bill of Materials" (CBOM) for all financial middleware.

### Phase II: Hybrid Integration (2026 - 2030)
- **Focus:** Co-existence of classical and quantum-safe algorithms.
- **Action:** Implementing "Double-Wrapping" where transactions are signed by both ECDSA and ML-DSA.

### Phase III: Full PQC Sovereignty (2030 - 2035)
- **Focus:** Deprecation of legacy primitives.
- **Action:** Final removal of RSA/ECC from sovereign rails by 2035 (per NIST IR 8547).

## Critical Risks & Pitfalls
- **Performance Overhead:** ML-KEM/ML-DSA have larger key sizes and signature lengths than ECC, potentially increasing latency in high-frequency trading (HFT) environments.
- **Implementation Bugs:** The complexity of lattice-based math increases the risk of side-channel attacks during early deployment.
- **Sovereign Fragmentation:** Divergence between NIST (US) and other national standards (e.g., China's SM series) could create "cryptographic silos" in global finance.

## Conclusion
Quantum-Safe Finance is not a destination but a state of continuous agility. The ability to rotate cryptographic primitives without interrupting the flow of capital is the new benchmark for systemic stability.
