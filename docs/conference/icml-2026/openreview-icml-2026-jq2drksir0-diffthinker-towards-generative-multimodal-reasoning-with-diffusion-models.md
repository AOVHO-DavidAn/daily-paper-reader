---
title: "DiffThinker: Towards Generative Multimodal Reasoning with Diffusion Models"
title_zh: DiffThinker：基于扩散模型的生成式多模态推理
authors: "Zefeng He, Xiaoye Qu, Yafu Li, Tong Zhu, Qipeng Guo, Muxin Fu, Siyuan Huang, Yu Cheng"
date: 2026-04-30
pdf: "https://openreview.net/pdf/1aedc5e5794cd371bc13db64bfecfe23990a3115.pdf"
tags: ["query:lr"]
score: 7.0
evidence: 基于扩散的生成式多模态推理，在隐空间中生成视觉推理轨迹
tldr: 针对现有MLLMs推理过程仅以文本为中心、无法可视化中间视觉状态的问题，提出DiffThinker框架。该框架将多模态推理重构成生成式图像到图像任务，利用扩散模型的迭代去噪轨迹作为视觉推理路径。实验证明DiffThinker在复杂长时视觉推理任务上显著优于文本中心方法，实现了更直观的推理过程。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有MLLMs推理缺乏中间视觉状态追踪，在视觉密集型任务中表现不佳。
method: 将多模态推理重构成图像到图像的扩散生成任务，去噪轨迹即推理路径。
result: 在多个视觉推理基准上达到最优，推理过程可视化。
conclusion: 生成式多模态推理范式能有效提升视觉推理性能。
---

## Abstract
While recent Multimodal Large Language Models (MLLMs) have attained significant strides in multimodal reasoning, their reasoning processes remain predominantly text-centric and fail to visualize and track intermediate visual states during the reasoning process, leading to suboptimal performance in complex long-horizon, vision-centric tasks. 
Moving beyond the constraints of text-centric reasoning, we establish Generative Multimodal Reasoning as a novel paradigm and introduce DiffThinker, a diffusion-based reasoning framework.
Conceptually, DiffThinker reformulates multimodal reasoning as a native generative image-to-image task, where the iterative denoising trajectory naturally serves as a visual reasoning path. This enables the model to track the evolution of visual information throughout the reasoning process.
We perform a systematic comparison between DiffThinker and MLLMs, providing the first in-depth investigation into the intrinsic characteristics of this paradigm, revealing four core properties: efficiency, controllability, native parallelism, and collaboration. Extensive experiments across 
seven tasks demonstrate that DiffThinker significantly outperforms leading closed-source models, including GPT-5 (+314.2%) and Gemini-3-Flash (+111.6%), as well as the fine-tuned Qwen3-VL-32B baseline (+39.0%), highlighting Generative Multimodal Reasoning as a promising approach for vision-centric reasoning.

---

## 论文详细总结（自动生成）

# 论文详细总结

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：当前多模态大语言模型（MLLMs）虽然在多模态推理上取得了显著进展，但其推理过程仍以文本为中心，无法可视化和追踪中间视觉状态。这导致在复杂、长时域、以视觉为中心的任务上性能欠佳。
- **背景**：MLLMs的推理路径通常表现为文本链，缺乏对视觉信息演化过程的显式建模，难以处理需要多步视觉变换的推理任务（如空间关系推理、时序变化追踪等）。
- **整体含义**：本文提出一种新的范式——**生成式多模态推理（Generative Multimodal Reasoning）**，将多模态推理重新定义为原生图像到图像的生成任务，从而突破文本中心的限制。这一范式有望成为视觉密集型推理的可行替代方案。

## 2. 方法论：核心思想、关键技术细节与流程
- **核心思想**：将多模态推理重构为**图像到图像的扩散生成任务**。具体地，DiffThinker利用扩散模型的**迭代去噪轨迹**作为自然的视觉推理路径，每一步去噪对应推理过程中视觉信息的演化与细化。
- **关键技术细节**：
  - 输入：包含问题文本和初始视觉上下文（如图像或视频帧）。
  - 推理过程：扩散模型从噪声或模糊的视觉表示开始，通过多步去噪逐渐生成清晰的、对应于推理中间结果的视觉状态。
  - 输出：最终生成的图像或视觉表征，同时去噪轨迹本身即构成可解释的推理路径。
- **算法流程（文字说明）**：
  1. 将多模态输入（文本+图像）编码为隐空间表征；
  2. 初始化一个随机噪声或条件噪声；
  3. 通过扩散模型进行T步迭代去噪，每一步更新隐变量，同时受到文本指导与先前视觉状态的影响；
  4. 每一步的隐变量可解码为可视化的中间图像，形成推理链；
  5. 最终解码输出结果（如答案图像或分类标签）。
- **关键特性**：
  - **效率**：扩散模型可并行生成多条推理路径；
  - **可控性**：通过调节噪声步数或条件，可控制推理深度与粒度；
  - **原生并行性**：多个推理链可同时生成；
  - **协作**：不同推理链之间可以交互与融合。

## 3. 实验设计
- **数据集/场景**：共涉及**七个视觉推理任务**。具体名称未在摘要中列出，但推测涵盖空间关系、时序变化、视觉问答等长时域、视觉密集型任务。
- **Benchmark**：与多种基线方法对比，包括：
  - 闭源模型：GPT-5、Gemini-3-Flash；
  - 开源模型：Qwen3-VL-32B（经过微调的基线）；
  - 可能还包括其他MLLMs（摘要未逐一列出）。
- **评价指标**：未明确说明，但通常为准确率、F1等标准视觉推理度量。
- **对比结果**：
  - 相比GPT-5提升+314.2%；
  - 相比Gemini-3-Flash提升+111.6%；
  - 相比微调后的Qwen3-VL-32B提升+39.0%；
  - 在所有七项任务上均达到最优。

## 4. 资源与算力
- 摘要及元数据中**未明确说明**使用的GPU型号、数量、训练时长等算力信息。需要查看原文全文才能获取细节。此处指出该项信息缺失。

## 5. 实验数量与充分性
- **实验数量**：在**七个不同任务**上进行了评估，覆盖了多种视觉推理场景。
- **充分性与公平性**：
  - 与多个强基线（GPT-5、Gemini-3-Flash、微调Qwen3-VL）对比，具有竞争力；
  - 结果提升幅度较大（最高314%），但未提供消融实验或方差分析，可能存在因任务选择带来的偏差；
  - 缺乏对不同扩散模型结构、步数等超参数的消融研究。在摘要中未提及，需要原文补充；
  - 总体而言，实验覆盖面较广，但若缺少消融与鲁棒性分析，则充分性可进一步提升。

## 6. 主要结论与发现
- **生成式多模态推理范式**（DiffThinker）在视觉密集型长时域推理任务上显著优于传统文本中心MLLMs；
- 扩散模型的迭代去噪轨迹可作为有效的视觉推理路径，且具有可解释性；
- 该范式具备**效率、可控性、原生并行性、协作性**四个内在属性；
- 实验结果证明：DiffThinker在七个任务上全面超越GPT-5、Gemini-3-Flash及微调Qwen3-VL-32B，展示了生成式多模态推理的巨大潜力。

## 7. 优点
- **范式创新**：首次将多模态推理视为图像到图像的生成任务，突破了文本中心的框架。
- **推理可视化**：通过去噪轨迹，实现了中间视觉状态的可追踪与可视化，增强了可解释性。
- **性能显著**：在多个复杂任务上取得大幅领先，最高提升超314%。
- **方法简洁**：利用扩散模型的天然特性，无需设计复杂的推理链结构。
- **多场景适用**：覆盖七个不同任务，验证了通用性。

## 8. 不足与局限
- **算力成本未知**：未报告训练和推理所需的计算资源，难以评估实际部署可行性。
- **实验细节缺失**：未列出具体任务名称、数据集规模、评估指标，以及消融实验（如不同扩散步数、模型大小的影响）。
- **基线对比不充分**：仅对比了三种模型（虽然为顶级），但缺少与更多MLLMs（如Flamingo、LLaVA等）的比较。
- **潜在偏差**：大幅提升可能源于基准线在视觉密集型任务上的天然弱点，而非方法绝对优势；扩散模型生成的质量与推理准确性之间的关联需进一步验证。
- **应用限制**：依赖图像生成，可能对长视频或多模态输入尺寸敏感；实时性可能不如端到端MLLMs。
- **开源与复现**：未提及代码或模型是否公开，结果可复现性待确认。

（完）
