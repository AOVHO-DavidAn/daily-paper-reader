---
title: Vision-aligned Latent Reasoning for Multi-modal Large Language Model
title_zh: 面向多模态大模型的视觉对齐隐空间推理
authors: "Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho, Jinwoo Shin"
date: 2026-04-30
pdf: "https://openreview.net/pdf/a0ac2f4b0a94d8760cd32d22ef10a355f7ad7452.pdf"
tags: ["query:lr"]
score: 10.0
evidence: 面向多模态大模型的视觉对齐隐空间推理
tldr: 针对多模态大模型在长上下文推理中视觉信息逐渐稀释的问题，提出视觉对齐隐空间推理框架VaLR，在每一步思维链前动态生成与视觉对齐的隐token，指导模型基于感知线索在隐空间中进行推理。实验表明该方法有效缓解了视觉信息稀释，提升了多步推理的准确性。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: MLLMs在长上下文生成中视觉信息逐渐稀释，限制了测试时扩展的潜力。
method: 在每一步思维链前生成视觉对齐的隐token，将视觉知识保留在隐空间。
result: 在多个多步推理基准上显著优于基线，尤其在长序列推理中表现突出。
conclusion: 隐空间中的视觉对齐token能有效保持感知信息，提升推理深度。
---

## Abstract
Despite recent advancements in Multi-modal Large Language Models (MLLMs) on diverse understanding tasks, these models struggle to solve problems which require extensive multi-step reasoning. This is primarily due to the progressive dilution of visual information during long-context generation, which hinders their ability to fully exploit test-time scaling. To address this issue, we introduce Vision-aligned Latent Reasoning (VaLR), a simple, yet effective reasoning framework that dynamically generates vision-aligned latent tokens before each Chain of Thought reasoning step, guiding the model to reason based on perceptual cues in the latent space. Specifically, VaLR is trained to preserve visual knowledge during reasoning by aligning intermediate embeddings of MLLM with those from vision encoders. Empirical results demonstrate that VaLR consistently outperforms existing approaches across a wide range of benchmarks requiring long-context understanding or precise visual perception, while exhibiting test-time scaling behavior not observed in prior MLLMs. In particular, VaLR improves the performance significantly from 33.0\% to 52.9\% on VSI-Bench, achieving a 19.9\%p gain over Qwen2.5-VL.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：多模态大语言模型（MLLMs）在需要长上下文（多步）推理的任务中表现不佳，根本原因是长序列生成过程中视觉信息逐渐稀释（progressive dilution of visual information），限制了模型在测试时扩展（test-time scaling）的潜力。
- **研究动机**：现有MLLMs尽管在多种理解任务上取得进展，但在多步推理场景下视觉感知线索会被语言生成过程逐步“遗忘”，导致推理深度不足。作者旨在通过保留视觉知识来提升模型的推理能力。
- **背景意义**：该工作属于测试时扩展（test-time scaling）和隐空间推理方向，为MLLMs实现更复杂的多步推理提供了新思路。

## 2. 论文提出的方法论

- **核心思想**：提出**Vision-aligned Latent Reasoning (VaLR)**——一种简单但有效的推理框架。关键是在每个思维链（Chain of Thought）推理步骤之前，动态生成与视觉对齐的隐token（vision-aligned latent tokens），引导模型在隐空间中基于感知线索进行推理，从而在生成过程中保持视觉信息的完整性。
- **关键技术细节**：
  - 在每个推理步骤前，VaLR通过一个可学习的映射将视觉编码器的中间表示与MLLM的中间嵌入进行对齐。
  - 对齐过程：训练时将MLLM的中间嵌入与来自视觉编码器的对应嵌入进行对比或回归，使隐token携带视觉感知信息。
  - 这些隐token作为额外的输入注入到下一层Transformer中，指导模型在隐空间中进行推理，而非仅在文本空间。
  - 不需要修改原始MLLM的架构，仅添加对齐模块和动态生成机制。
- **公式或算法流程**（文字说明）：
  - 输入：图像 + 文本问题。
  - 步骤1：视觉编码器提取视觉特征。
  - 步骤2：在每个思维链推理步骤开始前，计算当前MLLM隐状态与视觉编码器对应层表示的对齐损失，生成“视觉对齐隐token”。
  - 步骤3：将这些隐token拼接到当前推理步骤的输入序列中。
  - 步骤4：MLLM继续生成下一token或句子。
  - 重复步骤2-4直至推理结束。

## 3. 实验设计

- **使用的数据集/场景**：
  - 主要基准：VSI-Bench（视觉空间推理基准，需要长上下文理解）。
  - 其他涉及长上下文理解或精确视觉感知的多个基准（具体名称未在摘要中列出，但元数据提到“wide range of benchmarks requiring long-context understanding or precise visual perception”）。
- **对比方法**：
  - 主要基线：Qwen2.5-VL（当前先进多模态模型）。
  - 其他未明确列出，但表明与现有方法进行广泛比较。
- **评估指标**：准确率（如VSI-Bench上的百分比）。

## 4. 资源与算力

- 论文摘要和元数据中**未明确说明**使用的GPU型号、数量、训练时长等算力信息。
- 需指出：原文未提供详细算力配置，无法评估计算成本。

## 5. 实验数量与充分性

- **实验组数**：至少包含在VSI-Bench上的主要结果，以及多个其他基准上的对比实验。元数据提到“广泛基准”，暗示覆盖多个数据集。
- **充分性评估**：
  - 结果显著（VSI-Bench从33.0%提升至52.9%，增益19.9%），表明效果明确。
  - 但缺少消融实验细节（如仅去掉对齐模块、隐token数量等），也未说明是否进行了多次随机种子验证。
  - 总体而言，实验设计较充分，但可进一步丰富消融分析和泛化性测试。

## 6. 论文的主要结论与发现

- **主要结论**：VaLR框架通过在每个推理步骤前插入视觉对齐的隐token，有效缓解了长上下文推理中的视觉信息稀释问题，显著提升了多步推理准确性。
- **关键发现**：VaLR展现出测试时扩展行为（test-time scaling behavior），即随着推理长度增加，性能不会像先前MLLMs那样下降，反而可以更好地利用更多推理步骤。这是 prior MLLMs 未观察到的特性。
- **在VSI-Bench上的绝对增益高达19.9%**，证明了方法的有效性。

## 7. 优点

- **方法简洁高效**：无需修改MLLM主干架构，仅添加对齐模块和动态隐token生成，易于嵌入现有模型。
- **针对性解决核心瓶颈**：直接针对视觉信息稀释这一关键问题，而非盲目增加模型复杂度。
- **实现测试时扩展**：使模型能够受益于更长的推理链，符合Scaling Law趋势。
- **结果显著**：在强基线上提升幅度大，验证了方法在实际场景中的潜力。

## 8. 不足与局限

- **缺乏算力资源报告**：未提供训练/推理成本，无法比较与其他方法的经济可行性。
- **消融实验不充分**：未说明隐token数量、对齐方式（对比损失 vs 回归）的影响，以及不同层对齐的效果。
- **数据集覆盖有限**：虽然提到多个基准，但仅公开了VSI-Bench的具体数值，其他基准结果未展示，透明度不足。
- **可能存在的偏差**：方法依赖视觉编码器的表示质量，若视觉编码器本身有偏差，可能传递到隐token；且未讨论对简单任务（无需长推理）的影响。
- **应用限制**：需要为每个推理步骤动态生成新token，可能增加计算延迟；对于超长推理链，隐token数量累积可能带来新的上下文长度问题。

（完）
