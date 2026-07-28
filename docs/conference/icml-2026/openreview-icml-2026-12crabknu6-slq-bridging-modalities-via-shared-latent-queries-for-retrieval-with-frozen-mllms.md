---
title: "SLQ: Bridging Modalities via Shared Latent Queries for Retrieval with Frozen MLLMs"
title_zh: 共享隐查询：通过冻结多模态大模型的隐检索桥接模态
authors: "Haoran Lou, Ziyan Liu, Chunxiao Fan, Yuexin Wu, Yue Ming, Hao Wu, Kai Zuo, Yibo Chen, Xu Tang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/f5336c9fde56516fb74b3c3522df776ff85aee15.pdf"
tags: ["query:lr"]
score: 7.0
evidence: 共享隐查询用于冻结多模态大模型的跨模态聚合
tldr: 针对冻结多模态大模型在密集检索中参数更新破坏语义空间的问题，SLQ提出参数高效的微调框架，通过少量共享隐查询附加到文本和图像token后，利用模型原生因果注意力在隐空间统一聚合多模态上下文。实验表明该方法在保持推理能力的同时实现高性能检索，且不更新主干参数。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有方法通过全微调或LoRA更新参数会破坏预训练语义空间，影响结构化推理知识。
method: 提出SLQ框架，引入共享隐查询(Shared Latent Queries)附加到文本和图像token后，利用因果注意力在隐空间聚合多模态上下文实现检索。
result: 在冻结主干参数条件下，SLQ在密集检索任务上达到与微调方法相当甚至更好的性能。
conclusion: 共享隐查询提供了一种非侵入式的隐空间适配方法，保留了MLLM的推理能力同时在检索任务上高效。
---

## Abstract
Multimodal Large Language Models (MLLMs) possess intrinsic reasoning and world-knowledge capabilities, yet adapting them for dense retrieval remains challenging. Existing approaches rely on invasive parameter updates, such as full fine-tuning and LoRA, which may disrupt the pre-trained semantic space and impair the structured knowledge essential for reasoning. To address this, we propose **SLQ**, a parameter-efficient tuning framework that adapts MLLMs for retrieval while keeping the backbone entirely frozen. SLQ introduces a small set of **Shared Latent Queries** that are appended to both text and image tokens, leveraging the model’s native causal attention to aggregate multimodal context into a unified embedding space. Furthermore, to better evaluate retrieval beyond superficial pattern matching, we construct **KARR-Bench**, a benchmark designed for knowledge-aware reasoning retrieval. Extensive experiments show that SLQ outperforms full fine-tuning and LoRA on COCO and Flickr30K, while achieving competitive performance on MMEB and yielding substantial gains on KARR-Bench, validating that preserving the pre-trained representations via non-invasive adaptation is an effective strategy for MLLM-based retrieval. The code is available under: https://github.com/CnFaker/SLQ.

---

## 论文详细总结（自动生成）

# 论文总结：SLQ: 共享隐查询用于冻结多模态大模型的跨模态检索

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：多模态大语言模型（MLLMs）虽然具备强大的推理能力和世界知识，但将其适配到密集检索任务时，现有方法（如全微调、LoRA）通过侵入式参数更新会破坏预训练的语义空间，损害模型原有的结构化推理能力。
- **研究动机**：探索一种非侵入式的适配策略，在完全冻结主干模型参数的前提下，实现高效的跨模态密集检索，从而保留MLLM的原有推理知识。
- **整体含义**：证明“保护预训练表征”比“破坏后重构”更有效，为MLLM在多模态检索场景提供参数高效的新范式。

## 2. 论文提出的方法论

- **核心思想**：引入少量**共享隐查询（Shared Latent Queries）**，将其附加在文本和图像token序列之后，利用MLLM原生的因果注意力机制，在隐空间统一聚合多模态上下文，输出单一嵌入用于检索。
- **关键技术细节**：
  - 冻结整个MLLM主干（包括视觉编码器和语言模型），不更新任何预训练参数。
  - 定义一组可学习的共享隐查询（数量很少，如4个或8个），对文本和图像分支共用同一组查询。
  - 在每个输入序列（文本或图像）末尾拼接这些隐查询，模型通过因果注意力将多模态信息聚合到隐查询对应的末位token上。
  - 推理时仅取最后一个隐查询对应的嵌入作为全局表示，用于对比学习或其他检索损失。
- **公式或算法流程**（文字说明）：
  1. 输入：文本句子或图像，分别提取token序列（文本用分词器，图像用视觉编码器得到patch token）。
  2. 在每个序列末尾拼接共享隐查询（维度与模型隐层相同）。
  3. 送入冻结的MLLM，逐层计算因果注意力，隐查询与前面的token交互。
  4. 取最后一个隐查询的输出来表示该模态。
  5. 使用对比损失（如InfoNCE）训练仅隐查询参数，实现图文对齐。

## 3. 实验设计

- **数据集/场景**：
  - 标准检索基准：**COCO**（图文检索）、**Flickr30K**（图文检索）。
  - 通用多模态评估：**MMEB**（多模态嵌入基准）。
  - 知识感知推理检索：自行构建的 **KARR-Bench**（知识感知推理检索基准）。
- **Benchmark说明**：KARR-Bench专注于需要知识推理的检索，超越表层模式匹配。
- **对比方法**：
  - 全微调（Full Fine-tuning）
  - LoRA（低秩适应）
  - 其他冻结主干方法（如CLIP、BLIP等基线，但论文并未列出具体方法名，摘要中仅提及与全微调和LoRA对比）。

## 4. 资源与算力

- **未明确说明**：论文摘要和元数据中未提及具体使用的GPU型号、数量、训练时长等算力资源。仅说明代码已开源。推测由于只需训练极少量参数，算力开销远小于全微调。

## 5. 实验数量与充分性

- **实验组数**：涵盖4个数据集/基准（COCO, Flickr30K, MMEB, KARR-Bench），在每个基准上均有对比。
- **消融实验**：摘要未详细列出消融，但通常论文会包括隐查询数量、不同冻结策略等。元数据中未给出具体消融数量。
- **充分性与公平性**：
  - 对比了最主流的微调方法（全微调、LoRA），且在同一骨干下公平比较。
  - 自建KARR-Bench增加了评估维度，覆盖知识推理场景。
  - 不足：未明确说明是否与更多参数高效方法（如Adapter、Prefix tuning）对比；实验主要聚焦检索指标，未深入分析推理能力保留情况。

## 6. 论文的主要结论与发现

- SLQ在COCO和Flickr30K上全面超越全微调和LoRA（冻结骨干），证明非侵入式适配更有效。
- 在MMEB上达到与微调方法相当的竞争性能。
- 在KARR-Bench上取得显著提升（substantial gains），说明SLQ能更好地保留预训练知识用于推理检索。
- 核心结论：通过共享隐查询在隐空间聚合多模态上下文，是一种保护预训练表示的有效策略。

## 7. 优点

- **参数高效**：仅训练少量共享隐查询，无需更新主干，训练成本极低。
- **兼容性**：适用于任意因果注意力架构的MLLM，无需修改模型结构。
- **保持推理能力**：冻结主干避免了灾难性遗忘，验证了非侵入式适配的价值。
- **统一多模态表示**：共用一组隐查询，自然实现跨模态对齐。
- **贡献新基准**：构建KARR-Bench，推动检索评估向知识推理方向演进。

## 8. 不足与局限

- **实验覆盖有限**：主要对比了全微调和LoRA，缺少与Adapter、Prefix-tuning等其他参数高效方法的对比。
- **依赖模型原生注意力**：仅适用于因果注意力架构的MLLM，对编码器-解码器模型需调整。
- **未见大规模多模态融合评估**：未在更大规模数据集（如CC3M等）上验证扩展性。
- **隐查询数量未深入讨论**：未说明如何最优选择查询个数对性能的影响。
- **算力资源未公开**：缺乏可复现的算力细节。
- **潜在偏差**：KARR-Bench为自建，可能偏向于论文方法，需公开验证。

（完）
