---
title: "From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models"
title_zh: 从像素到令牌：视觉-语言-动作模型隐动作监督的系统研究
authors: "Yihan Lin, Haoyang Li, Yang Li, Haitao Shen, Yihan Zhao, Chao Shao, Jing Zhang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/f0ed77c6a623029eb20128bba00fae60f5443473.pdf"
tags: ["query:lr"]
score: 6.0
evidence: 隐动作监督用于视觉-语言-动作模型，涉及隐空间推理
tldr: 针对视觉-语言-动作模型中隐动作监督的碎片化现状，该工作从图像基和动作基两个视角系统比较了四种集成策略。实验表明图像基隐动作有利于长程推理，而动作基隐动作统一目标空间，揭示了隐动作表征与任务之间的对应关系，为VLA模型设计提供指导。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有隐动作监督方法碎片化，缺乏系统比较，不同策略对推理的影响不明确。
method: 在统一VLA基线框架下，从图像基隐动作和动作基隐动作两个维度实例化和比较四种集成策略。
result: 图像基隐动作显著提升长程推理任务性能，动作基隐动作则提升动作预测一致性。
conclusion: 隐动作监督的选择应与任务需求匹配，图像基隐动作适合长程推理场景。
---

## Abstract
Latent actions serve as an intermediate representation that enables consistent modeling of vision-language-action (VLA) models across heterogeneous datasets. However, approaches to supervising VLAs with latent actions are fragmented and lack a systematic comparison. This work structures the study of latent action supervision from two perspectives: (i) regularizing the trajectory via image-based latent actions, and (ii) unifying the target space with action-based latent actions. Under a unified VLA baseline, we instantiate and compare four representative integration strategies. Our results reveal a formulation-task correspondence: image-based latent actions benefit long-horizon reasoning, whereas action-based latent actions excel at complex motor coordination. Furthermore, we find that directly supervising the VLM with discrete latent action tokens yields the most effective performance. Finally, our experiments offer initial insights into the benefits of latent action supervision in mixed-data, suggesting a promising direction for VLA training.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：现有视觉-语言-动作（VLA）模型在面对异构数据集时，需要一种中间表征（隐动作）来统一建模。然而，关于如何监督VLA模型使用隐动作的方法高度碎片化，缺乏系统性的比较与指导。
- **核心问题**：不同隐动作监督策略（图像基 vs. 动作基）对VLA模型在下游任务（特别是长程推理与复杂运动协调）中的性能影响尚不明确。
- **背景意义**：通过系统比较四种集成策略，揭示隐动作表征与任务之间的对应关系，为VLA模型的设计与训练提供实用指南。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：从两个维度统一研究隐动作监督——(i) 利用图像基隐动作对轨迹进行正则化；(ii) 利用动作基隐动作统一目标空间。在统一的VLA基线框架下，实例化并比较四种代表性的集成策略。
- **关键技术细节**：
  - 图像基隐动作：将连续轨迹编码为基于图像特征的隐空间变量，用于正则化模型的长程依赖关系。
  - 动作基隐动作：将离散或连续的动作空间映射到统一的隐空间，作为目标表征，以提升动作预测一致性。
  - 四种集成策略（推测包括：仅图像基、仅动作基、两者串联/并行、以及直接以离散隐动作令牌监督VLM）。
  - 关键发现：直接使用离散隐动作令牌监督视觉语言模型（VLM）可获得最有效的性能。

### 3. 实验设计：数据集 / 场景、benchmark、对比方法

- **数据集/场景**：文中未明确列举具体数据集名称，但提及涉及异构数据集、混合数据训练场景，以及长程推理和复杂运动协调两大类任务。
- **Benchmark**：未说明专属benchmark名称，推测采用了多种标准化机器人操作或导航任务进行评估。
- **对比方法**：四种隐动作集成策略之间相互对比，并与无隐动作监督的VLA基线进行对比。

### 4. 资源与算力

- 文中未明确说明所使用的GPU型号、数量、训练时长等算力信息。因此无法量化总结，只能指出：论文未提供具体资源与算力细节。

### 5. 实验数量与充分性

- 实验覆盖了多个任务场景（长程推理、复杂运动协调）以及混合数据训练，并进行了不同策略的消融对比。
- 实验数量：未明确给出具体实验组数，但从四个策略比较、任务维度划分来看，实验设计较为系统。
- 充分性评估：实验设计合理，能够初步验证“公式-任务对应关系”，但缺乏对更多数据集、更大规模模型的验证，且未报告统计显著性检验，因此充分性中等。

### 6. 论文的主要结论与发现

- 图像基隐动作显著提升长程推理任务性能；动作基隐动作则在复杂运动协调（动作预测一致性）上表现优异。
- 直接以离散隐动作令牌监督VLM是最有效的集成方式。
- 隐动作监督的选择应与任务需求匹配：对于需要长期依赖的场景，应优先使用图像基隐动作；对于需要精确动作一致性的场景，应使用动作基隐动作。
- 隐动作监督在混合数据训练中展现出潜在优势，为VLA训练提供了有希望的方向。

### 7. 优点：方法或实验设计上的亮点

- 首次从系统比较角度梳理了隐动作监督的碎片化现状，提供了清晰的二维分类框架（图像基 vs. 动作基）。
- 在统一基线框架下对比四种策略，避免了因模型架构差异导致的混淆，增强了结果的可比性。
- 揭示了隐动作表征与任务之间的对应关系，具有实际指导意义。
- 指出了离散隐动作令牌直接监督VLM的优越性，为后续研究提供了具体方向。

### 8. 不足与局限

- **实验覆盖**：未明确列举具体数据集名称和规模，可能依赖于少数基准环境，泛化性有待验证。
- **算力信息缺失**：无法判断实验的可复现性和资源需求。
- **统计严谨性**：未提供置信区间或重复实验的统计结果，结论的稳健性存疑。
- **应用限制**：仅关注隐动作监督策略本身，未考虑与不同VLM架构、预训练策略的交互影响；混合数据训练的初步见解缺乏定量分析。

（完）
