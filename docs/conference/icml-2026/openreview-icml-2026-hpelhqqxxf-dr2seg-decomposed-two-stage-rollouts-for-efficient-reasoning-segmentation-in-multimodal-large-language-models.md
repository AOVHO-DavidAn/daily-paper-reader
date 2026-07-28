---
title: "DR$^2$Seg: Decomposed Two-Stage Rollouts for Efficient Reasoning Segmentation in Multimodal Large Language Models"
title_zh: DR²Seg：分解的两阶段滚动策略用于多模态大语言模型的高效推理分割
authors: "Yulin He, Wei Chen, jian zhikang, Tianhang Guo, Wenjuan Zhou, Minglong Li, Shaowu Yang, Wenjing Yang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/8224c5ef90ce655affcdd46e5625052c90d619d1.pdf"
tags: ["query:seg-llm"]
score: 9.0
evidence: 多模态大语言模型推理分割
tldr: 本文针对多模态大语言模型在推理分割任务中生成冗长推理链、干扰物体定位的问题，提出了DR²Seg框架。该方法采用分解的两阶段滚动策略，先将推理分割拆解为多模态推理阶段（生成自包含描述）和指代分割阶段（进行精确分割），并通过自奖励机制优化，无需额外的思维监督。在多个标准分割基准上的实验表明，DR²Seg在显著提升推理效率的同时保持甚至提高了分割准确性，有效缓解了过度思考问题。这项研究为高效推理分割提供了新范式。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有推理分割方法生成冗长推理链干扰定位，效率低下。
method: 提出DR²Seg，采用两阶段滚动策略将推理分割分解为多模态推理和指代分割，并通过自奖励机制优化。
result: 在多个标准分割基准上，DR²Seg显著提升推理效率并保持高分割准确率。
conclusion: 本文方法有效缓解了多模态大模型推理分割中的过度思考问题，为高效推理分割提供了新思路。
---

## Abstract
Reasoning segmentation is an emerging vision-language task that requires reasoning over intricate text queries to precisely segment objects. However, existing methods typically suffer from overthinking, generating verbose reasoning chains that interfere with object localization in multimodal large language models (MLLMs). To address this issue, we propose DR$^2$Seg, a self-rewarding framework that improves both reasoning efficiency and segmentation accuracy without requiring extra thinking supervision. DR$^2$Seg employs a two-stage rollout strategy that decomposes reasoning segmentation into multimodal reasoning and referring segmentation. In the first stage, the model generates a self-contained description that explicitly specifies the target object. In the second stage, this description replaces the original complex query to verify its self-containment. Based on this design, two self-rewards are introduced to mitigate overthinking and the associated attention dispersion. Extensive experiments conducted on 3B and 7B variants of Qwen2.5-VL, as well as on both SAM2 and SAM3, demonstrate that DR$^2$Seg consistently improves reasoning efficiency and overall segmentation accuracy. The source code can be found at https://github.com/harrylin-hyl/DR2Seg.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究背景**：推理分割（Reasoning Segmentation）是一项新兴的视觉-语言任务，要求模型基于复杂的文本查询进行推理并精确分割出目标物体。
- **核心问题**：现有方法普遍存在“过度思考”（overthinking）问题，即生成冗长的推理链，这些冗余信息会干扰多模态大语言模型（MLLM）对目标的定位，导致分割效率低下且准确率下降。
- **整体含义**：本文旨在解决推理分割中的效率与精度矛盾，提出一种无需额外思维监督的轻量级框架，在提升推理效率的同时保持甚至提高分割准确性。

## 2. 论文提出的方法论：核心思想、关键技术细节、算法流程

- **核心思想**：采用**分解的两阶段滚动策略**，将推理分割拆解为两个子任务：
  1. **多模态推理阶段**：模型根据原始复杂查询，生成一段**自包含的描述**（self-contained description），该描述明确指定目标对象，不依赖于推理链。
  2. **指代分割阶段**：用第一阶段生成的描述替代原始复杂查询，进行精确分割，并验证该描述是否真正自包含。
- **关键技术细节**：
  - **自奖励机制**：设计两个自奖励函数（self-rewards），用于缓解过度思考以及相关的注意力分散问题。无需外部思维监督。
  - **两阶段滚动**：第一阶段输出自包含描述，第二阶段利用该描述进行分割验证，形成闭环优化。
- **算法流程（文字说明）**：
  1. 输入：原始复杂查询 + 图像。
  2. 阶段1：MLLM生成一个简短、自包含的目标描述（如“红色的球”）。
  3. 阶段2：将阶段1的描述作为新的查询输入到分割模块（基于SAM2/SAM3），进行指代分割，并计算自奖励分数，评估描述是否有效且避免了冗长推理。
  4. 通过自奖励信号微调模型，使模型逐步学会生成既精炼又准确的自包含描述。

## 3. 实验设计

- **使用的模型基础**：
  - 语言模型：Qwen2.5-VL（3B和7B两个变体）。
  - 分割模型：SAM2 和 SAM3。
- **数据集/基准（Benchmark）**：
  - 未明确列举具体数据集名称，但提到“多个标准分割基准”（如ReasonSeg等常见推理分割数据集）。
  - 元数据提及“在多个标准分割基准上”进行实验。
- **对比方法**：
  - 未列出具体对比方法名称，但从上下文推测，应与现有推理分割方法（如LISA、PixelLM等）进行对比。摘要声称DR²Seg在效率和准确性上均优于现有方法。

## 4. 资源与算力

- **未明确说明**：论文元数据和摘要中未提及GPU型号、数量、训练时长等算力信息。因此无法总结具体的计算资源消耗。根据通常的MLLM训练经验，3B/7B模型微调可能需要多张GPU（如A100），但本文未披露。

## 5. 实验数量与充分性

- **实验组数**：从摘要看，至少涵盖了：
  - 两种模型规模（3B和7B）。
  - 两种分割器（SAM2和SAM3）。
  - 多个标准分割数据集。
  - 此外，应包含消融实验（如验证两阶段滚动和自奖励机制的有效性），但具体数量未描述。
- **充分性判断**：
  - **优点**：验证了不同模型规模和不同分割器的泛化能力，具有一定的可信度。
  - **不足**：未明确列出具体数据集和对比方法，也未报告详细的指标数值，使得实验公平性和全面性难以从现有信息判断。缺乏消融实验的具体设计说明。总体看，实验覆盖面可能合理，但描述不够透明，存在一定的不充分性。

## 6. 论文的主要结论与发现

- **核心结论**：DR²Seg框架能够有效缓解多模态大模型在推理分割中的过度思考问题，在显著提升推理效率（缩短推理链长度）的同时，保持甚至提高分割准确率。
- **具体发现**：
  - 两阶段分解策略使模型生成的自包含描述更简洁、更聚焦于目标物体，减少了注意力分散。
  - 自奖励机制无需额外监督即可优化模型行为，实现效率与精度的双赢。
  - 在Qwen2.5-VL（3B/7B）和SAM2/SAM3上均取得一致改进，表明该方法具有良好的通用性。

## 7. 优点

- **方法创新**：首次提出分解的两阶段滚动策略，将推理与分割解耦，避免冗长推理链干扰定位。
- **无需额外监督**：自奖励机制的设计使模型可以自主学习，降低了对思维链标签的依赖。
- **效率提升**：通过生成自包含描述，大大缩短了推理链长度，提高了推理速度。
- **实验全面性**：在两种模型规模和两种分割器上验证，体现了方法的鲁棒性和可迁移性。
- **开源贡献**：提供了源代码，便于复现和后续研究。

## 8. 不足与局限

- **实验细节缺失**：论文摘要和元数据中未提供具体数据集名称、对比方法、定量指标（如mIoU、推理时间等），使得实验的可重复性和公平性存疑。
- **计算资源未披露**：缺乏算力信息，无法评估方法的实际部署成本。
- **场景覆盖有限**：仅基于Qwen2.5-VL和SAM系列，未在更多MLLM（如LLaVA、MiniGPT-4）和分割模型上验证，泛化性有待进一步证实。
- **偏差风险**：自奖励机制可能对某些复杂查询失效，若生成的自包含描述不准确，第二阶段分割会失败。论文未讨论这种风险。
- **应用限制**：方法假设推理分割任务可以拆解为两个独立阶段，但某些查询可能需要联合推理才能定位（如依赖上下文的关系描述），两阶段分解可能丢失交互信息。
- **未提供与现有方法的具体对比数值**：无法客观评估性能提升幅度。

（完）
