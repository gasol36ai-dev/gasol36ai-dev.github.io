---
title: 'ML-DSA (Module-Lattice-Based Digital Signature Standard)'
description: 'ML-DSA (formerly Dilithium) is a NIST-standardized (FIPS 204) post-quantum digital signature algorithm. It is designed to replace classical '
pubDate: 2026-07-12
category: 'invest'
topic: 'research'
tags: ['研究筆記']
draft: false
source: 'knowledge/research/concepts/PQC_ML_DSA.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# ML-DSA (Module-Lattice-Based Digital Signature Standard)
**Type:** Algorithm / Standard
**Domain:** Sovereign Identity & Transactional Integrity

## Overview
ML-DSA (formerly Dilithium) is a NIST-standardized (FIPS 204) post-quantum digital signature algorithm. It is designed to replace classical signature schemes like ECDSA and RSA.

## Technical Details
- **Primary Use:** Digital signatures for transaction authentication, identity verification, and software updates.
- **Security Basis:** Based on the hardness of the Module Learning with Errors (MLWE) and Short Integer Solution (SIS) problems in lattices.
- **Performance Profile:** 
    - **Pros:** High computational efficiency for signing and verification.
    - **Cons:** Significantly larger signature and public key sizes compared to ECDSA, which increases network bandwidth requirements and storage overhead for ledgers.

## Implications for Sovereign Data & CBDCs
- **Transaction Authenticity:** ML-DSA is the cornerstone for ensuring that CBDC transfers remain immutable and authentic in the presence of a CRQC.
- **Root of Trust:** Used in the issuance of sovereign digital identities and the signing of policy updates in programmable money rails.
- **Hardware Acceleration:** Due to the polynomial multiplication requirements, deployment in sovereign edge nodes often requires FPGA or ASIC acceleration to maintain throughput.

**Related:** [[Post-Quantum_Cryptography]], [[PQC_ML_KEM]], [[Quantum_Safe_Financial_Rails]]

## Deployment Pipeline
Integrate ML-DSA into the root-of-trust for sovereign sensor nodes.

## Strategic Value
Provides high-security digital signatures for autonomous agent commands.
