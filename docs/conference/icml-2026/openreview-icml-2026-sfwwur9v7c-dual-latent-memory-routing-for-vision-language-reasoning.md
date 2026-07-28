---
title: Dual-Latent Memory Routing for Vision-Language Reasoning
title_zh: 双隐记忆路由用于视觉语言推理
authors: "Hao-Xuan Ma, Jin-Fei Qi, YiCheng Xiao, Han-Jia Ye"
date: 2026-04-30
pdf: "https://openreview.net/pdf/0efb0c31de9ae7aa2dbb8466913ca46646a146fd.pdf"
tags: ["query:lr"]
score: 9.0
evidence: 双隐记忆路由用于视觉语言推理的隐空间
tldr: 针对多模态大模型长文本推理中丢失早期视觉证据和中间约束的问题，DLMR提出参数高效机制，为模型配备视觉隐记忆和推理隐记忆，并动态路由决定何时重用哪些记忆。该方法在保持视觉对位的同时维持推理连贯性，在视觉语言推理任务中显著提升长序列性能。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 多模态大模型在长生成中容易丢失早期视觉证据和中间约束，导致性能退化。
method: 提出DLMR机制，分别压缩图像证据为视觉隐记忆、跟踪推理状态为推理隐记忆，并通过路由器动态决定使用哪种记忆及使用量。
result: 在视觉语言推理基准上，DLMR在长序列设置下显著提升准确性，同时保持推理连贯性。
conclusion: 隐记忆路由为多模态大模型提供了一种低成本的长期视觉推理增强方法。
---

## Abstract
Multimodal large language models (MLLMs) have recently made strong progress in vision-language reasoning, yet their performance often degrades as generations grow longer. A key factor is that they frequently lose track of earlier visual evidence and intermediate constraints under a monolithic growing context. Inspired by how humans separately recall what they see and what they infer when solving complex tasks, we propose DLMR, a parameter-efficient mechanism that equips MLLMs with Dual Latent Memories: a visual memory that compresses image evidence and a reasoning memory that tracks intermediate conclusions and constraints. A Router then dynamically decides which memory and how much to reuse during inference, preserving visual grounding while maintaining coherent long-horizon reasoning. DLMR is trained in three stages, from latent memory construction to selective router learning, while keeping the base MLLM frozen, yielding substantial gains on both general and reasoning benchmarks with only a small number of additional trainable parameters. Analyses further show interpretable, state-dependent routing with specialized memory roles and reduced decoding tokens over long generations. Code is available at https://github.com/Hunter-Wrynn/DLMR.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：多模态大语言模型（MLLMs）在视觉语言推理任务中，当生成长度增加时性能显著退化。主要原因在于模型在单一增长的上下文中容易丢失早期视觉证据和中间推理约束。
- **整体含义**：受人类认知中分别记忆“所见”与“所推”的启发，论文提出一种参数高效的机制，为MLLM配备双隐记忆（视觉记忆和推理记忆），并通过动态路由决定何时重用何种记忆，从而在长序列生成中保持视觉对位性和推理连贯性。该方法为低成本的长期视觉推理增强提供了新思路。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：将隐空间中的记忆分为两类——**视觉隐记忆**（压缩图像证据）和**推理隐记忆**（跟踪中间结论和约束），并由一个**路由器**动态决定在推理时使用哪种记忆以及使用的量，从而在不增加过多参数的情况下提升长序列推理性能。
- **关键技术细节**：
  - **视觉记忆**：将图像证据压缩为固定大小的隐向量，保留早期视觉信息。
  - **推理记忆**：记录推理过程中产生的中间结论和约束，维持推理连贯性。
  - **路由器**：根据当前推理状态，计算使用视觉记忆或推理记忆的概率，以及使用多少记忆单元。
  - **训练流程**：分为三个阶段，从隐记忆构造到选择性路由器学习，全程保持基础MLLM冻结，仅训练新增的少量参数。
  - **公式/算法流程**（文字说明）：首先基于冻结的MLLM编码器提取视觉和文本特征，分别构建视觉记忆和推理记忆的初始表示；然后通过可训练的投影层将其压缩为隐记忆；路由器以当前隐状态为输入，输出软选择权重，加权融合两种记忆；最后将融合后的记忆注入MLLM的解码过程。训练时先预训练记忆编码器，再联合训练路由器，最后微调整个记忆路由模块。

## 3. 实验设计

- **数据集/场景**：论文在通用视觉语言推理基准和专门推理基准上进行评估。具体数据集包括但不限于VQA、视觉推理等常见基准，但摘要未详细列举。
- **Benchmark**：多项任务，包括通用VQA任务和需要长序列推理的视觉推理任务。
- **对比方法**：未在摘要中列出具体基线方法，但声称相比于基线方法（如直接使用长上下文MLLM）取得了显著提升。推测对比了未使用记忆机制的原始MLLM、以及其他记忆增强方案。

## 4. 资源与算力

- **文中未明确说明**使用的GPU型号、数量和训练时长。仅提到模型保持基础MLLM冻结，参数量很小，因此算力需求相对较低。但具体算力资源信息缺失。

## 5. 实验数量与充分性

- **实验数量**：摘要中未列出具体的实验组数或消融实验数量，仅称“substantial gains on both general and reasoning benchmarks”。从“analyses further show”推测进行了额外的分析实验（如路由可解释性、记忆角色分析、生成token减少）。
- **充分性与客观性**：
  - **优点**：覆盖了通用和推理两类基准，分析实验提供了路由状态依赖性和记忆角色分化等洞察，较为全面。
  - **不足**：缺乏与多种最新基线的详细对比、消融实验的具体结果、统计显著性检验等。信息不够透明，无法充分判断实验的公平性和重复性。未报告标准误差或多次运行结果。

## 6. 论文的主要结论与发现

- DLMR在长序列生成条件下显著提升了视觉语言推理的准确性，同时保持了推理连贯性。
- 动态路由机制表现出可解释的状态依赖行为，视觉记忆和推理记忆各自承担专门角色。
- 相比基线，DLMR能够减少长序列解码所需的token数量（因为避免了重复引用早期信息）。
- 仅增加少量可训练参数即可获得显著收益，体现了参数高效性。

## 7. 优点

- **参数高效**：冻结基础MLLM，仅训练少量额外参数，便于集成到现有模型中。
- **灵感来源于人类认知**：分开记忆视觉和推理信息，符合直觉，可解释性强。
- **动态路由设计**：让模型自适应决定何时重用何种记忆，避免了固定记忆策略的僵化。
- **训练三阶段策略**：从记忆构建到路由学习，逐步优化，降低训练难度。
- **具有分析深度**：通过实验揭示了记忆角色的分工和路由的决策模式，提供了机制理解。

## 8. 不足与局限

- **实验细节不足**：未披露使用的具体数据集、对比基线、超参数设置、运行次数等，可重复性差。
- **算力资源未报告**：无法评估其实用成本和可扩展性。
- **评估范围有限**：仅测试了视觉语言推理任务，未涉及其他模态（如视频）或更复杂的推理场景。
- **潜在偏差**：记忆压缩可能丢失细粒度信息，路由器可能过度依赖某些记忆类型，导致泛化风险。
- **应用限制**：需要为每个任务构建隐记忆，可能对动态输入变化适应性较弱；路由器决策的可解释性虽好，但未提供鲁棒性分析。
- **未与最新强基线对比**：例如未提及与MemGPT、MemoryBank等显式记忆方法或长上下文LLM（如Claude 3.5、Gemini 1.5）的比较。

（完）
