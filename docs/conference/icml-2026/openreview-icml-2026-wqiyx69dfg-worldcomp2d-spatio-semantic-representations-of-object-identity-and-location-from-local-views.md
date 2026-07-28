---
title: "WorldComp2D: Spatio-semantic Representations of Object Identity and Location from Local Views"
title_zh: WorldComp2D：从局部视图学习目标身份与位置的空间语义表示
authors: "Seongmin Jin, Doo Seok Jeong"
date: 2026-04-30
pdf: "https://openreview.net/pdf/793905231a19b66e2381aa43b58b9762a5702998.pdf"
tags: ["query:lr"]
score: 6.0
evidence: 学习结构化的隐空间表示用于空间语义推理
tldr: 本文针对现有隐表示方法缺乏显式结构的问题，提出WorldComp2D，通过多尺度局部感受野显式组织隐空间几何。该框架包括近距编码器和定位器，高效捕获空间语义信息。实验表明在空间推理任务上性能优越且计算效率高。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有隐表示方法隐式且计算效率低，缺乏显式空间结构。
method: 构建依赖空间距离的编码器和定位器，显式组织隐空间几何。
result: 在目标定位和空间推理任务上取得高效结果。
conclusion: 显式结构化隐空间能有效支持空间语义推理。
---

## Abstract
Learning latent representations that capture both semantic and spatial information is central to efficient spatio-semantic reasoning. However, many existing approaches rely on implicit latent structures combined with dense feature maps or task-specific heads, limiting computational efficiency and flexibility.
We propose WorldComp2D, a novel lightweight representation learning framework that explicitly structures latent space geometry according to object identity and spatial proximity using multiscale \textit{local} receptive fields. This framework consists of (i) a proximity-dependent encoder that maps a given observation into a spatio-semantic latent space and (ii) a localizer that infers the coordinates of objects in the input from the resulting spatio-semantic representation.
Using facial landmark localization as a proof-of-concept, we show that, compared to SoTA lightweight models, WorldComp2D reduces the numbers of parameters and FLOPs by up to $4.0\times$ and $2.2\times$, respectively, while maintaining real-time performance on CPU. These results demonstrate that explicitly structured latent spaces provide an efficient and general foundation for spatio-semantic reasoning. This framework is open-sourced at https://github.com/JinSeongmin/WorldComp2D.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
现有基于隐表示的空间语义推理方法大多采用隐式潜在结构，结合密集特征图或任务特定头部，导致计算效率低、灵活性差。本文旨在探索一种能够显式组织隐空间几何结构的方法，使得表示既能捕获语义信息又能编码空间位置，从而提升空间推理的效率与泛化能力。

## 2. 方法论
- **核心思想**：通过多尺度局部感受野，显式地将隐空间几何按照物体身份和空间邻近性进行组织，构建一个轻量级表示学习框架 **WorldComp2D**。
- **关键组件**：
  - **近距编码器**：根据空间距离依赖关系，将输入观察映射到空间‑语义隐空间。
  - **定位器**：从得到的隐表示中推断输入中物体的坐标（如人脸关键点）。
- **算法流程**（文字说明）：输入图像 → 多尺度局部感受野编码 → 显式结构化隐空间（空间距离与语义标签对应） → 定位器输出目标坐标。

## 3. 实验设计
- **数据集/场景**：以人脸关键点定位作为概念验证实验（具体数据集名称未在摘要中说明，推测为常见人脸关键点数据集如300W、WFLW等）。
- **基准**：对比了当前最先进的轻量级模型（SoTA lightweight models）。
- **评价指标**：未明确列出，但报告了参数数量、FLOPs和CPU实时性能。

## 4. 资源与算力
文中**未明确说明**使用的GPU型号、数量或训练时长。仅提到模型在CPU上可实时运行，表明对算力要求较低。

## 5. 实验数量与充分性
- **实验数量**：仅在一个任务（人脸关键点定位）上与若干SoTA轻量模型进行对比，未提及多个数据集或跨任务验证。
- **充分性分析**：实验覆盖范围较窄，缺乏消融研究（如不同多尺度设计的影响、编码器‑定位器耦合效应等），也缺少在其他空间推理任务（如目标检测、语义地图）上的评估。因此，实验在泛化性和深入性方面存在不足。

## 6. 主要结论与发现
- WorldComp2D相比SoTA轻量模型，参数减少最多**4.0倍**，FLOPs减少最多**2.2倍**，同时保持CPU实时性能。
- 显式结构化的隐空间能够为空间‑语义推理提供高效且通用的基础，验证了该范式的有效性。

## 7. 优点
- **方法创新**：首次提出通过多尺度局部感受野显式组织隐空间几何，将空间距离与物体身份直接关联。
- **计算高效**：模型极轻量，可在CPU上实时运行，适合嵌入式或资源受限场景。
- **结构可解释性**：隐空间具有显式几何结构，便于后续推理或扩展。

## 8. 不足与局限
- **实验验证不足**：仅在一个任务（人脸关键点）上测试，缺乏在多种空间推理场景（如导航、目标跟踪、3D场景理解）上的泛化性验证。
- **消融分析缺失**：未系统分析各组件（如多尺度感受野大小、编码器深度、定位器结构）的贡献，可能导致方法设计存在冗余或未优化。
- **数据集与对比范围**：未公开具体数据集及对比模型的完整配置，存在评估偏差风险。
- **理论分析缺乏**：对隐空间几何的数学性质（如等距性、拓扑连续性）未作深入讨论，仅停留在实证层面。

（完）
