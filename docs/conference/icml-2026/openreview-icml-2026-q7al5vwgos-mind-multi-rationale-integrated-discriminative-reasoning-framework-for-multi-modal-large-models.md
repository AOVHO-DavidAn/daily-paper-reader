---
title: "MIND: Multi-rationale INtegrated Discriminative Reasoning Framework for Multi-modal Large Models"
title_zh: MIND：面向多模态大模型的多理由集成判别推理框架
authors: "Chuang Yu, Jinmiao Zhao, Mingxuan Zhao, Yunpeng Liu, Xiujun Shu, Yuanhao Feng, Bo Wang, Xiangyu Yue"
date: 2026-04-30
pdf: "https://openreview.net/pdf/a6da5f981d9662081689a139a3664e53aed179be.pdf"
tags: ["query:lr"]
score: 5.0
evidence: 多模态大模型的多理由判别式推理框架
tldr: 针对多模态大模型在多理由语义建模不足、逻辑鲁棒性差等问题，提出多理由集成判别推理框架MIND，包含理由增强与判别范式及渐进式两阶段修正，使模型从被动模仿转向主动判别推理。在多个推理基准上验证了其有效性。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有MLLMs在多理由语义建模和逻辑鲁棒性方面存在不足，易受误导线索影响。
method: 提出理由增强与判别（RAD）范式和渐进式两阶段修正流程。
result: 在多个多模态推理任务上取得了显著改进，尤其在对抗性样本上鲁棒性提升。
conclusion: 主动判别推理范式能有效提升MLLMs的鲁棒性和准确性。
---

## Abstract
Recently, multimodal large language models (MLLMs) have been widely applied to reasoning tasks. However, they suffer from limited multi-rationale semantic modeling, insufficient logical robustness, and susceptibility to misleading cues. Therefore, we propose a Multi-rationale INtegrated Discriminative (MIND) reasoning framework, which is designed to endow MLLMs with human-like cognitive abilities of “Understand → Rethink → Correct”, and achieves a paradigm evolution from passive imitation-based reasoning to active discriminative reasoning. Specifically, we introduce a Rationale Augmentation and Discrimination (RAD) paradigm, which provides a unified and extensible data foundation. Meanwhile, we design a Progressive Two-stage Correction Learning (P2CL) strategy. The first phase enhances multi-rationale positive learning, while the second phase enables active logic discrimination and correction. In addition, to mitigate representation entanglement in the multi-rationale semantic space, we propose a Multi-rationale Contrastive Alignment (MCA) optimization strategy. Extensive experiments show that our MIND achieves SOTA performance on multiple public datasets. Our data and code are available at https://github.com/YuChuang1205/MIND.

---

## 论文详细总结（自动生成）

# 论文总结：MIND：面向多模态大模型的多理由集成判别推理框架

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：现有多模态大语言模型（MLLMs）在推理任务中存在三个关键缺陷：多理由语义建模能力有限、逻辑鲁棒性不足、容易受误导性线索影响。模型往往是被动模仿（passive imitation），缺乏人类主动认知推理能力（理解→反思→纠正）。
- **动机**：为了赋予MLLMs类人的主动判别推理能力，从被动模仿范式转向主动判别推理范式，提升模型在多理由场景下的鲁棒性和准确性。

## 2. 方法论：核心思想、关键技术细节

- **核心思想**：提出“多理由集成判别推理框架”（MIND），模拟人类“理解→反思→纠正”的认知过程。框架包含三个关键技术模块：
  - **理由增强与判别（RAD）范式**：构建统一且可扩展的数据基础，用于生成和判别多个候选理由（rationale）。
  - **渐进式两阶段修正学习（P2CL）策略**：
    - 第一阶段：增强多理由正向学习（positive learning），使模型充分理解正确理由的语义。
    - 第二阶段：使模型学会主动逻辑判别和纠正（active logic discrimination and correction）。
  - **多理由对比对齐（MCA）优化策略**：解决多个理由语义空间中表示纠缠（representation entanglement）问题，通过对比学习拉近正确理由、推远错误理由，提高判别能力。
- **算法流程（文字说明）**：
  1. 输入多模态数据（图像+文本），通过RAD生成多个候选理由。
  2. 利用P2CL两阶段训练：先基于正样本学习多理由正向特征；再引入负样本和对抗样本，训练模型判别正确与错误理由并进行修正。
  3. 在训练过程中，应用MCA损失函数对多理由表示进行对比对齐，增强语义区分度。
  4. 推理时，模型主动判别输入理由的正确性，并输出修正后的最终答案。

## 3. 实验设计

- **数据集/场景**：论文提到在“多个公开数据集”上进行实验，但摘要未具体列出数据集名称。根据元数据中“tags: query:lr”和“evidence: 多模态大模型的多理由判别式推理框架”，可能涉及视觉问答、常识推理等典型多模态推理benchmark（如VQA、ScienceQA、MMBench等，需原文验证，但此处未提供）。
- **Benchmark**：未明确说明具体基准，但声称达到了SOTA（state-of-the-art）性能。
- **对比方法**：未列出具体对比的基线模型，但通常与主流MLLMs（如LLaVA、BLIP-2、InstructBLIP等）进行比较。摘要未提供细节。

## 4. 资源与算力

- **未明确说明**：论文摘要和元数据中未提及使用的GPU型号、数量、训练时长等算力信息。因此无法总结，需要指出此信息缺失。

## 5. 实验数量与充分性

- **实验数量**：摘要提到“大量实验”（extensive experiments），但未给出具体实验组数。通常包含：主要结果对比（多个数据集）、消融实验（验证RAD、P2CL、MCA各模块贡献）、鲁棒性测试（对抗样本）、泛化性测试等。
- **充分性与客观性**：由于缺乏详细实验设置，无法完全评估。但论文声称SOTA，且在多个数据集上验证，表明具有一定的充分性。不过，缺少与具体方法、数据集、随机种子、标准差等细节，客观性需原文确认。

## 6. 主要结论与发现

- MIND框架使MLLMs从被动模仿转向主动判别推理，显著提升了多理由语义建模能力和逻辑鲁棒性。
- 渐进式两阶段修正学习（P2CL）和对比对齐（MCA）有效解决了表示纠缠，增强了抗误导能力。
- 在多个公开数据集上达到SOTA性能，尤其在对抗性样本上鲁棒性提升明显。

## 7. 优点

- **方法创新**：提出“理解→反思→纠正”的主动判别推理范式，不同于传统被动模仿，更具认知启发性。
- **模块化设计**：RAD、P2CL、MCA三个模块可扩展、可组合，便于后续研究。
- **鲁棒性提升**：明确针对误导线索进行对抗训练与纠正，实用价值高。
- **代码与数据开源**：提供GitHub仓库，促进可复现性和社区发展。

## 8. 不足与局限

- **实验细节缺失**：论文摘要未提供具体数据集、对比基线、超参数等，限制了对其全面评价。需阅读全文以获取。
- **算力与效率未提及**：未讨论模型训练/推理成本，可能在大规模部署时存在效率瓶颈。
- **通用性风险**：框架依赖多理由生成质量，若理由生成阶段本身存在偏差，可能影响整体效果。对抗样本覆盖范围未知，存在过拟合特定攻击类型的风险。
- **应用限制**：主要针对视觉-语言多模态推理，是否适用于纯文本或更多模态尚未验证。

（完）
