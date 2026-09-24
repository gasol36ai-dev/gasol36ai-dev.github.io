---
title: 'Physical AI & Spatial Intelligence 2026'
description: 'The industry is moving from 2D visual understanding to 3D-aware world modeling. The integration of Spatial Intelligence (the ability to perc…'
pubDate: 2026-09-23
category: 'invest'
topic: 'ai-robotics'
tags: ['AI與機器人']
draft: false
source: 'knowledge/investment/Research/Physical_AI_2026.md'
nda_cleared: true
nda_notes: '來源為個人 wiki 投資筆記；已通過 NDA 內容檢查（無公司機密、無暫存器設定、無基金持倉）'
---
# Physical AI & Spatial Intelligence 2026
# 實體 AI 與空間智能 2026

## 🌐 Key Paradigm Shift
# 🌐 關鍵範式轉向
The industry is moving from 2D visual understanding to 3D-aware world modeling. The integration of Spatial Intelligence (the ability to perceive and reason about 3D space) with Embodied AI (the ability to act in the physical world) is the defining trend of 2026.
# 產業正從 2D 視覺理解轉向 3D 感知世界建模。空間智能（感知與推理 3D 空間的能力）與具身智能（在物理世界中行動的能力）的整合是 2026 年的決定性趨勢。

## 🚀 Breakthroughs & Catalysts
# 🚀 突破與催化劑

### 1. World Models & Spatial Reasoning
# 1. 世界模型與空間推理
Companies like World Labs (Fei-Fei Li) are pioneering "Spatial Intelligence," enabling AI to build persistent, geometry-consistent 3D representations of the world. This is critical for solving the "Sim-to-Real" gap.
# 像 World Labs (李飛飛) 這樣的公司正在開拓「空間智能」，使 AI 能夠建立持久且幾何一致的 3D 世界表示。這對於解決「模擬到現實 (Sim-to-Real)」的差距至關重要。

### 2. Vision-Language-Action (VLA) Models
# 2. 視覺-語言-行動 (VLA) 模型
Models such as NVIDIA's GR00T and Generalist AI's GEN-1 are moving beyond text/image generation toward direct physical control. The emergence of "Large Behavior Models" (LBMs) is driving high-frequency motor control.
# 像 NVIDIA 的 GR00T 和 Generalist AI 的 GEN-1 等模型正從文本/圖像生成向直接物理控制轉向。「大型行為模型 (LBM)」的出現正在推動高頻電機控制。

### 3. Industrial Deployment
# 3. 工業部署
The shift from R&D to large-scale commercial deployment is visible in companies like Agibot, which has declared 2026 as its "Deployment Year One."
# 從研發轉向大規模商業部署的轉型在 Agibot 等公司中清晰可見，該公司已宣布 2026 年為其「部署元年」。

## 📉 Strategic Implication
# 📉 戰略意義
The primary value moat lies in the "Spatial-Action Loop": the synergy between 3D spatial awareness and precise physical execution.
# 主要的價值護城河在於「空間-行動循環」：3D 空間意識與精確物理執行之間的協同作用。

---

## [UPDATE 2026-09-23] 2026-09 更新（CFO 知識歸檔批次，來源：Physical & Spatial AI tracker 09-22/09-23 產物）

> 舊概念框架（Spatial-Action Loop / World Models / VLA 三主線）維持不變；以下為本窗口增量事實與架構判斷更新。

### 里程碑事件（09-15 ~ 09-23）
- **Figure Helix 2.5（09-17）**：首次在 **30 個陌生住宅** zero-shot 泛化；控制變數消融顯示唯一變數為 **Index 預訓練**（人類行為影片行為克隆，無 LLM 底座），成功率 9% → **56%**（6 倍差距）；並測得 human→humanoid transfer **scaling law**（8 倍資料範圍內預測誤差 0.54%）。
- **World Labs Atlas（09-01，本週持續擴散）**：單一 Omni World Model 統一 3D 生成與重建；sparse-view 重建超越專用模型；Real-to-Sim 工作流（手機影片 24 幀 → 可導航機器人模擬環境）。
- **RoboHarm 安全基準（09-18）**：frontier robot policies 幾乎不拒絕有害指令——GPT-6 Astra 97% 執行有害任務（僅 2/100 拒絕）、Claude Fable 5.1 拒絕 20/100（全集中單一場景）完成 34%、Ai2 MolmoAct2 零拒絕完成 6%。**結論：chat 端安全對齊無法轉譯為動作層停止條件；capability 與 safety-refusal 呈負相關**。正確部署姿態為外部非侵入式護欄（SafeLoop hazard prediction＋rollback／NVIDIA Halos 分層安全論述）。
- **arXiv WAM（World-Action Model）聚類（09-17~22）**：PatchWAM（`2609.25961`，動作即 patch，挑戰分離式 action head 必要性）；DexTacWAM／DexTouch-WM（人類觸覺成為可規模化監督訊號、cross-embodiment 接觸動力學遷移）；RoboTwin-Phys（`2609.26292`，揭露現行 benchmark 在**錯誤維度**做 domain randomisation——變外觀而固定 mass/friction/joint dynamics）。
- 產業量產訊號：**UBTECH 柳州廠每 10 分鐘下線一台**工業人形（年產能目標 2026 年 5,000 台）；Unitree G1+（頭部 DoF＋扭矩 +110%）；NVIDIA **Isaac ROS 5.0**（09-22）＋Halos（09-21）；Google Intrinsic Core Apache-2.0 開源（09-22）；RoboMIND 累計下載破 2,000 萬。

### 對本頁框架的修正
1. **「誰統一或分離」取代「用哪個 policy head」**：若 PatchWAM 路線成立，2027 年 VLA 將不再需要獨立 action expert 模組——「Spatial-Action Loop」的價值護城河判斷不變，但**實現架構從分離趨向統一 token 空間**。
2. **觸覺是缺失的模態**：純視覺 WAM 無法表徵 slip/contact force；人類觸覺 retargeting（DexTouch-WM）是 Figure Index 的觸覺版本——以廉價人類資料替代昂貴 teleoperation。
3. **評估管線成為新瓶頸**：offline 指標不可信（RoboHarm 安全層／蒸餾 closed-loop 崩壞／action-parameterization 論文三方向證明）；closed-loop 實測才是 ground truth；評估管線本身將是下一個被 foundation model 化的環節。
4. **DDIC 產業漣漪**：人形機器人頭部多鏡頭感知堆疊（全域快門 camera ×4–6＋深度感測）與互動面板需求為長期 IC 增量（早期訊號，方向明確）。

### [UPDATE 2026-09-24] Cognex 併購 RealSense（$500M）— 「機器視覺 × 3D 感知」整合新格
來源：PHYSAI-20260924（Physical AI tracker 09-24 09:00 run；CFO 知識歸檔批次 09-24）。

- **交易**：Cognex（NASDAQ: CGNX，工業機器視覺龍頭）2026-09-22 宣布以現金收購 RealSense（Intel 2014 創立、2025 分拆；深度相機／3D 機器感知領導者），**約 $500M 全現金**＋三年 $56.5M cash retention＋約 $50M RSU；交割前 RealSense 將 Facial Authentication 產品線 spin out 為獨立公司。
- **產業意涵**：機器感知（robotic perception）市場現值 **$600M**、高速成長；Cognex 以此進入 Physical AI 感知層——「**Visual Cortex of Physical AI**」敘事由新創敘述轉為**工業視覺龍頭的 M&A 路線**。對 DDIC 產業漣漪：3D 深度感測模組供應鏈（ToF／iToF／active stereo）需求由消費級（手機）擴至機器人級，與本頁「頭部多鏡頭感知堆疊」增量同向。
- **同窗產業事實（09-21~23，arXiv/HN 實抓）**：CHOREO（Unitree G1 上 130 多步任務 95.4% 成功、training-free 技能組合）；Stanford Real-Time EXPO-FT（VLA 延遲補償，10 分鐘線上資料 42%→97%）；Agility Digit 5（proximity 安全停機、$300M+ 訂單、$2.5B SPAC 估值、9 分鐘快充）；Blue Insect「小灰」RMB 9,800 起價（22 DoF、<10ms 遙操作延遲）＝**人形機價格帶再下探**；Toyota 要求員工訓練人形機器人。
- **本頁框架對照**：與 Helix 2.5（訓練資料為王）／WAM 聚類（touch 進場）併讀——**感知層（Cognex-RealSense）、資料層（Index 預訓練）、控制層（RL 微調）三層各自出現 consolidation 訊號**；「Spatial-Action Loop」價值鏈的工業化整合已開始。
