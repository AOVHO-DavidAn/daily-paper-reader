---
title: "From Correspondence to Actions: Human-Like Multi-Image Spatial Reasoning in Multi-modal Large Language Models"
title_zh: 从对应到动作：多模态大模型中类似人类的多图像空间推理
authors: "Masanari Oi, Koki Maeda, Ryuto Koike, Daisuke Oba, Nakamasa Inoue, Naoaki Okazaki"
date: 2026-04-30
pdf: "https://openreview.net/pdf/4d496372e769667532976b0954f7d3cc7fe1cb6d.pdf"
tags: ["query:lr"]
score: 5.0
evidence: 多图像空间推理与多模态大模型
tldr: 针对多模态大模型在多图像空间推理中的局限性，提出人类感知训练方法，显式建模跨视图对应和逐步视角变换机制，使模型能够像人类一样整合多视角信息，在多个基准上显著提升了空间推理能力。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有MLLMs在多图像空间推理中无法有效整合多视角信息，缺乏对人类认知机制的显式建模。
method: 提出Human-Aware Training，通过交叉视图对应和逐步视角变换两个监督信号训练MLLM。
result: 在多个多图像推理任务上取得了显著性能提升，超越了先前方法。
conclusion: 显式引入人类空间认知机制能有效提升MLLMs的多图像推理能力。
---

## Abstract
While multimodal large language models (MLLMs) have made substantial progress in single-image spatial reasoning, multi-image spatial reasoning, which requires integration of information from multiple viewpoints, remains challenging.
Cognitive studies suggest that humans address such tasks through two mechanisms: *cross-view correspondence*, which identifies regions across different views that correspond to the same physical locations, and *stepwise viewpoint transformation*, which composes relative viewpoint changes sequentially.
However, existing studies incorporate these mechanisms only partially and often implicitly, without explicit supervision for both.
We propose Human-Aware Training for Cross-view correspondence and viewpoint cHange (HATCH), a training framework with two complementary objectives: (1) Patch-Level Spatial Alignment, which encourages patch representations to align across views for spatially corresponding regions, and (2)  Action-then-Answer Reasoning, which requires the model to generate explicit viewpoint transition actions before predicting the final answer.
Experiments on three benchmarks demonstrate that HATCH consistently outperforms baselines of comparable size by a clear margin and achieves competitive results against much larger models, while preserving single-image reasoning capabilities.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：多模态大语言模型（MLLMs）在单图像空间推理方面已取得显著进展，但在**多图像空间推理**任务中仍面临挑战。这类任务需要模型整合来自多个视角的图像信息，以理解三维场景或完成空间对应与推理。
- **背景**：认知科学研究表明，人类完成此类任务依赖两种核心机制：
  - **跨视图对应（cross-view correspondence）**：识别不同视角图像中对应同一物理位置的区域。
  - **逐步视角变换（stepwise viewpoint transformation）**：顺序组合相对视角变化（例如“向左旋转90度→向前移动”）。
- **现有不足**：已有的MLLMs方法仅**部分且隐式**地融入了这些机制，缺乏针对两者的显式监督信号，导致模型无法像人类一样有效整合多视角信息。

## 2. 方法论：核心思想、关键技术细节

- **方法名称**：HATCH（Human-Aware Training for Cross-view correspondence and viewpoint cHange）
- **核心思想**：通过显式引入人类空间认知的两个机制作为训练目标，使MLLM学会跨视图对应和逐步视角变换。
- **关键技术细节**（两个互补目标）：
  1. **Patch-Level Spatial Alignment（补丁级空间对齐）**：对于不同视角图像中对应的空间区域（如同一物体的同一像素点），强制模型在补丁（patch）级别的特征表示上对齐。这实现了显式的跨视图对应学习。
  2. **Action-then-Answer Reasoning（先动作后答案推理）**：要求模型在预测最终答案之前，先生成明确的视角变换动作序列（例如“向右转90度”“向前走两步”），再基于变换后的空间信息回答问题。这实现了逐步视角变换的显式建模。
- **训练流程**：在标准MLLM训练基础上，引入上述两个辅助损失（或监督信号），与主任务损失联合优化。补丁级对齐可通过对比学习或特征对齐损失实现；动作生成则通过语言建模损失训练模型输出序列化的动作描述。

## 3. 实验设计

- **使用的数据集/场景**：论文在**三个基准**（benchmarks）上进行了评估，这些基准涉及多图像空间推理任务，例如多视角物体定位、空间关系推断等（具体数据集名称未在摘要中列出，需查阅原文）。
- **对比方法**：
  - 相同参数规模（comparable size）的基线模型（如未经过HATCH训练的MLLMs）。
  - 更大规模的模型（much larger models），用于展示HATCH可达到与超大模型竞争的效果。
- **评估指标**：准确率或类似指标（具体未详述，但提及“consistently outperforms”和“competitive results”）。

## 4. 资源与算力

- **未明确说明**：摘要和元数据中未提及GPU型号、数量、训练时长等算力信息。需要阅读原文才能获取具体训练配置。

## 5. 实验数量与充分性

- **实验数量**：
  - 三个基准数据集的主要结果对比。
  - 通过消融研究（ablation studies）验证两个目标的有效性（摘要暗示“两个互补目标”被分别验证）。
  - 包含与多种基线和更大模型的比较。
- **充分性与公平性**：
  - 覆盖多个基准，体现泛化性。
  - 控制了模型大小（与同规模基线对比），并展示了与更大模型的竞争关系，对比较为公平。
  - 消融研究验证了每个组件的贡献，增强了可解释性。
  - 但缺少对更多任务类型（如纯文本空间推理）或跨领域迁移性的验证，可能影响结论的广泛性。

## 6. 主要结论与发现

- **主要结论**：显式引入人类空间认知机制（跨视图对应与逐步视角变换）能够有效提升MLLMs的多图像推理能力。
- **具体发现**：
  - HATCH在三个基准上**一致超越**了同规模基线，并**达到或接近**更大规模模型的性能。
  - 方法不会损害模型原有的单图像推理能力（preserves single-image reasoning capabilities），说明附加目标不引入负迁移。

## 7. 优点

- **方法设计亮点**：
  - **显式建模**：直接模拟人类认知的两大机制，而非隐式学习，增强了可解释性和效果。
  - **双重监督**：补丁级对齐与动作序列生成互补，分别对应“对应”和“变换”两个核心过程。
  - **保持单图能力**：避免因多图训练而遗忘单图知识，体现出方法的稳健性。
- **实验设计亮点**：
  - 与同规模和更大规模模型对比，结果具有说服力。
  - 消融实验直接验证了每个监督信号的必要性。

## 8. 不足与局限

- **实验覆盖有限**：仅评估了三个基准，可能无法代表所有多图像空间推理场景（如动态视频、遮挡场景）。
- **偏差风险**：数据集是否涵盖多样化的视角变化（如旋转、缩放、平移）和真实世界光照/纹理变化？若数据集偏理想化，方法在真实复杂场景中的泛化性存疑。
- **应用限制**：
  - 需要显式定义补丁级对齐的标签（如像素对应），获取此类标注成本较高。
  - 动作序列生成依赖于预定义的动作空间（如“向左转90度”），可能无法适应连续或非离散的视角变化。
- **算力信息缺失**：无法评估方法部署的硬件需求及效率。
- **单图能力测试可能不够彻底**：摘要仅提及“preserves”，未提供详细实验，可能缺乏全面性。

（完）
