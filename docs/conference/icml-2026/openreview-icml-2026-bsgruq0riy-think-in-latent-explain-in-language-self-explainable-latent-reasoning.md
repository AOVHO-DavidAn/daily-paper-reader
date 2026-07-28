---
title: "Think in Latent, Explain in Language: Self-Explainable Latent Reasoning"
title_zh: 在隐空间中思考，用语言解释：自解释隐空间推理
authors: "Dayuan Zhao, Shengcao Cao, Yu-Xiong Wang, Liangyan Gui"
date: 2026-04-30
pdf: "https://openreview.net/pdf/9cbca985aaa3c5008f975c66792937c746462994.pdf"
tags: ["query:lr"]
score: 10.0
evidence: 统一的自解释隐空间推理框架
tldr: 本文针对隐空间推理不可解释的问题，提出自解释隐空间推理（SELR）。该方法训练统一的隐推理路径，同时保持高效性和可解释性，无需后处理解码器。实验证明SELR在保持效率的同时提供了可读的推理解释。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 隐空间推理虽高效但不可解释，现有方法增加了解耦的后期解码器。
method: 训练共享的隐推理路径，同时进行推理和解释生成。
result: 在多个推理数据集上效率与可解释性均优于基线。
conclusion: 隐空间推理可以同时实现高效和自解释。
---

## Abstract
Latent reasoning has emerged as a powerful alternative to text-based Chain-of-Thought (CoT), offering significant gains in computational efficiency by compressing verbose reasoning into compact embeddings. However, compressing reasoning into the latent space renders the thinking opaque, hindering its interpretability.
Current methods present a stark trade-off: they either function as unexplainable “black boxes” (e.g., Coconut), where the latent reasoning is not human-readable, or rely on separate post-hoc decoders for explainability (e.g., Heima), introducing architectural overhead and decoupling the explanation from the actual reasoning process.
In this work, we present a unified framework for Self-Explainable Latent Reasoning (SELR) that trains a single model to perform efficient and inherently explainable latent reasoning. Our core contribution is a novel multi-task training objective that optimizes for two goals simultaneously: (1) an Answer Loss that optimizes the latent reasoning trajectory to produce accurate final answers, and (2) a CoT Loss that explicitly trains the same model to decode its own latent representations back into human-understandable reasoning steps. This design ensures that generated latent representations are both task-effective and semantically interpretable, eliminating the need for external decoders. We validate the effectiveness of SELR on both Large Language Models (LLMs) and Vision-Language Models (VLMs), demonstrating that SELR achieves superior token efficiency and accuracy compared to baselines, while uniquely providing self-contained explainability without auxiliary models.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：隐空间推理（Latent Reasoning）通过将冗长的推理过程压缩为紧凑的嵌入向量，大幅提升了计算效率，但导致推理过程不透明、不可解释。现有方法存在明显权衡：要么是完全不可解释的“黑箱”（如Coconut），要么依赖额外的后处理解码器（如Heima）来提供解释，这不仅增加了架构开销，而且解释与实际的推理过程是分离的。
- **动机**：现有方法无法让隐空间推理本身同时具备高效性和可解释性，亟需一个统一框架，使得模型能自主生成可读的推理步骤，而无需外部解码器。
- **整体含义**：本文提出的自解释隐空间推理（SELR）旨在证明：通过设计合适的训练目标，隐空间推理可以“在隐空间中思考，用语言解释”，实现自包含的解释能力，从而兼顾效率与可解释性。

## 2. 方法论：核心思想、关键技术细节

- **核心思想**：训练一个单一的模型，同时执行高效隐空间推理和显式推理步骤生成，使得隐表示既对任务有效又具有语义可解释性。
- **关键技术细节**：
  - 提出**多任务训练目标**，包含两个损失：
    - **Answer Loss**：优化隐空间推理轨迹，确保模型生成准确的最终答案。
    - **CoT Loss**：训练同一个模型将自己的隐表示解码回人类可理解的推理步骤（Chain-of-Thought），强制隐表示携带语义信息。
  - 通过联合优化这两个损失，隐表示自然具备可解释性，无需任何外部分离的解码器或后处理模块。
- **算法流程**（文字说明）：
  1. 输入问题，模型在隐空间中进行多步推理，产生一系列隐状态嵌入。
  2. 在训练时，同时计算两个目标：Answer Loss（基于最终隐状态得到答案，与真实答案对比）和 CoT Loss（将中间隐状态解码为文本推理步骤，与真实推理步骤对比）。
  3. 反向传播更新模型参数，使模型同时学会高效压缩推理和准确解码解释。
  4. 推理时，模型默认在隐空间推理得到答案，并可选择性地将隐状态解码为文字解释，无需额外模型。

## 3. 实验设计

- **使用场景与数据集**：论文在**大型语言模型（LLMs）** 和**视觉-语言模型（VLMs）** 上都进行了验证。具体数据集名称未在摘要中列出，仅提及“多个推理数据集”。
- **Benchmark**：未明确说明 benchmark 名称，但评估指标包括**词元效率（token efficiency）** 和**准确率（accuracy）**，同时考察解释质量（自包含可解释性）。
- **对比方法**：
  - 隐空间推理黑箱方法：Coconut（无解释）
  - 带后处理解码器方法：Heima（引入架构开销）
  - 可能还包括标准的文本 CoT 推理（作为效率基线）

## 4. 资源与算力

- 论文摘要和元数据中**未提及**使用的 GPU 型号、数量、训练时长等具体算力信息。因此无法给出具体数值。

## 5. 实验数量与充分性

- **实验数量**：论文在 LLMs 和 VLMs 两大类型模型上进行了实验，但摘要未透露具体多少个数据集或消融实验组数。元数据提到“在多个推理数据集上效率与可解释性均优于基线”，暗示至少覆盖了 2-3 个推理数据集。
- **充分性与公平性**：
  - **优点**：同时覆盖了纯文本和视觉-语言两种模态，增强了结论的普适性；对比了当前主流的两类基线（不可解释黑箱与后处理可解释方法）。
  - **不足**：缺少消融实验的明确提及（如多任务权重的影响、不同解码方式的影响）；未说明是否在同等计算量下对比（如词元数或推理步数是否一致）。由于摘要信息有限，无法完整判断实验的全面性，但核心指标（效率和准确率）均有报告，可认为基本充分。

## 6. 主要结论与发现

- SELR 在词元效率和准确率上均优于基线方法（包括 Coconut 和 Heima）。
- 独特地提供了**自包含的可解释性**，无需任何辅助模型或后处理解码器。
- 证明了隐空间推理可以同时实现高效和自解释，打破了现有方法中效率与可解释性不能兼得的僵局。

## 7. 优点

- **方法亮点**：
  - 提出统一框架，一个模型即可完成推理和解释生成，架构简洁。
  - 多任务训练目标巧妙地将可解释性要求融入隐表示学习过程，无需额外解码器。
  - 在 LLMs 和 VLMs 上统一验证，展示跨模态的通用性。
- **实验亮点**：
  - 同时对比了不可解释和可解释两类基线，证明新方法在效率和可解释性上的双重优势。
  - 强调“token efficiency”指标，契合隐空间推理的本意（减少推理词元）。

## 8. 不足与局限

- **实验覆盖局限**：摘要中未给出具体数据集名称和规模，也未提及实际应用的领域（如数学、常识、多跳问答等），难以判断方法是否在复杂推理任务上同样有效。
- **偏差风险**：仅提及优于 Coconut 和 Heima，未与更多近期隐空间推理或可解释性方法（如 LLaVA 的视觉 CoT、隐动作推理等）比较，对比范围可能有限。
- **局限性**：
  - 多任务训练可能引入额外的超参数调整（如两个损失的权重），但未在摘要中讨论其敏感性。
  - “自解释”能力可能受限于模型容量：如果隐表示压缩过度，CoT Loss 可能难以恢复高质量解释；如果过度注重可解释性，可能牺牲一部分效率。
  - 未讨论推理速度或实际部署开销（如推理时是否必须同时解码解释才能获得答案，还是可以仅用隐推理）。
- **资源信息缺失**：未提供训练所需算力，其他研究者难以复现或评估方法的实际成本。

（完）
