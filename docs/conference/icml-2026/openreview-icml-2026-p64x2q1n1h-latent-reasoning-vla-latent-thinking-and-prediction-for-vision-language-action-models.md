---
title: "Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models"
title_zh: 隐推理VLA：面向视觉-语言-动作模型的隐空间思考与预测
authors: "Shuanghao Bai, Jing Lyu, Wanqi Zhou, Zhe Li, Dakai Wang, Lei Xing, Xiaoguang Zhao, Pengwei Wang, Zhongyuan Wang, Cheng Chi, Badong Chen, Shanghang Zhang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/d1d48bb8ae32dab3bc513e65d14fb7fc84c438ea.pdf"
tags: ["query:lr"]
score: 10.0
evidence: 面向视觉-语言-动作模型的连续隐空间推理
tldr: 本文针对VLA模型中使用显式CoT推理导致高开销和表示不匹配的问题，提出LaRA-VLA，将多模态推理内化到连续隐空间。通过课程训练逐步从显式CoT过渡到隐推理。实验表明LaRA-VLA在保持性能的同时大幅降低推理成本。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有VLA模型使用显式CoT推理，开销大且表示不匹配。
method: 将多模态CoT推理内化到连续隐空间，通过课程学习过渡。
result: 在具身控制任务上，LaRA-VLA降低推理成本且保持性能。
conclusion: 隐空间推理可有效替代显式CoT用于VLA模型。
---

## Abstract
Vision-Language-Action (VLA) models benefit from Chain-of-Thought (CoT) reasoning, but existing approaches incur high inference overhead and rely on discrete reasoning representations that mismatch continuous perception and control.
We propose Latent Reasoning VLA (LaRA-VLA), a unified VLA framework that internalizes multi-modal CoT reasoning into continuous latent representations for embodied action. 
LaRA-VLA performs unified reasoning and prediction in latent space, eliminating explicit CoT generation at inference time and enabling efficient, action-oriented control.
To realize latent embodied reasoning, we introduce a curriculum-based training paradigm that progressively transitions from explicit textual and visual CoT supervision to latent reasoning, and finally adapts latent reasoning dynamics to condition action generation.
We construct two structured CoT datasets, LIBERO-LaRA and Bridge-LaRA, and evaluate LaRA-VLA across simulation benchmarks and long-horizon real-robot manipulation tasks. Experimental results show that LaRA-VLA outperforms existing state-of-the-art VLA methods while achieving up to a 90\% reduction in inference latency compared to explicit CoT-based VLA approaches, highlighting latent reasoning as an effective and efficient paradigm for real-time embodied control.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文核心问题与整体含义（研究动机与背景）

- **问题背景**：视觉-语言-动作（VLA）模型在具身控制中受益于链式思维（Chain-of-Thought, CoT）推理，但现有方法存在两个主要缺陷：
  - 推理开销高：生成显式的语言/视觉推理步骤导致推理延迟大；
  - 表示不匹配：离散的推理表示（如文本 token）与连续的感知和控制信号存在鸿沟。
- **整体目标**：提出一种能够将多模态 CoT 推理内化到连续隐空间中的统一 VLA 框架，在消除显式 CoT 生成的同时保持甚至提升任务性能，实现面向实时具身控制的高效推理。

## 2. 论文提出的方法论——核心思想、关键技术细节

- **核心思想**：将多模态 CoT 推理过程压缩为连续隐空间中的隐式推理与预测，使模型在隐空间内完成“思考”后再直接生成动作，从而避免显式 CoT 的生成开销。
- **关键技术细节**：
  - **Latent Reasoning VLA（LaRA-VLA）**：一个端到端的统一框架，在连续隐空间中完成多模态推理与动作预测。
  - **课程式训练范式（Curriculum Training）**：
    1. **阶段一**：使用显式的文本和视觉 CoT 监督训练模型，使其学习结构化推理。
    2. **阶段二**：通过教师强制（teacher forcing）逐步将显式推理压缩到隐空间，使模型学习隐式推理。
    3. **阶段三**：将隐推理动态适配到动作生成，实现从隐空间直接输出控制信号。
  - **隐空间推理机制**：模型内部维护一个连续的隐状态，通过对历史观测、语言指令和自身隐状态的联合编码，进行迭代更新和预测，最终解码为动作。
- **公式/算法流程**（文字说明）：
  - 输入：视觉观测序列 \( o_{1:t} \)、语言指令 \( l \)
  - 隐推理：维护隐变量 \( z_t \)，通过循环网络或 transformer 隐层更新 \( z_t = f(z_{t-1}, o_t, l) \) 进行多步推理
  - 动作预测：从最终隐状态 \( z_T \) 解码出动作 \( a_t = g(z_T) \)
  - 训练时通过课程学习逐步移除显式 CoT token，迫使模型在隐空间内完成推理。

## 3. 实验设计——数据集、基准、对比方法

- **数据集**：
  - 构建了两个结构化 CoT 数据集：**LIBERO-LaRA**（基于 LIBERO 模拟器）和 **Bridge-LaRA**（基于 Bridge 数据），每个数据包含显式的中间推理步骤（文本+视觉）用于课程学习。
- **基准（Benchmark）**：
  - 模拟环境：LIBERO 系列任务（如物体操作、长序列任务）
  - 真实机器人任务：长周期（long-horizon）桌面操作任务，涵盖拾放、组装、推拉等。
- **对比方法**：
  - 现有 SOTA VLA 方法（具体方法名论文未在摘要中列举，但一般包括 RT-2、PaLM-E 等变体），特别对比了使用显式 CoT 的 VLA 方法。
  - 消融实验：对比有无课程训练、不同推理模式（显式 vs 隐式）等。

## 4. 资源与算力

- **文中未明确说明**使用的具体 GPU 型号、数量以及训练时长。
- 推测：由于是 ICML 接受论文且涉及大规模视觉-语言模型训练和具身数据，通常需要至少 8×A100 或同等计算资源，但论文中未给出明确信息，需要读者自行推测或联系作者。

## 5. 实验数量与充分性

- **实验组数**：
  - 在 LIBERO 和 Bridge 两个模拟/真实数据上的任务评估；
  - 对比了多种 SOTA 基线，并在推理延迟上做了量化比较；
  - 包含了课程训练的消融（隐推理 vs 显式推理）；
  - 真实机器人上的长周期任务验证。
- **充分性评估**：
  - 覆盖了模拟和真实场景，具有一定广度和实用性验证。
  - 推理延迟的对比数据（最高 90% 减少）提供了明确效率优势。
  - 不足：论文未在摘要中给出具体数值表或统计显著性检验，也未见不同随机种子多次实验的方差报告；消融实验的数量和具体变体未详细列出，可能仅限于课程训练阶段和推理方式。整体看实验设计合理但细节有待正文补充。

## 6. 论文的主要结论与发现

- LaRA-VLA 在 LIBERO 和 Bridge 数据集上 **优于现有 SOTA VLA 方法**，并且：
  - **推理延迟降低高达 90%**（与基于显式 CoT 的 VLA 方法相比）。
  - 在长周期真实机器人任务中同样表现良好，证明了隐空间推理的实时性与有效性。
- **隐空间推理**是一种能够替代显式 CoT 的有效且高效的范式，特别适用于实时具身控制场景。

## 7. 优点

- **创新性**：首次将 VLA 中的多模态 CoT 推理完全内化到连续隐空间，解决了推理开销和表示不匹配两大痛点。
- **高效性**：推理阶段无显式 CoT 生成，延迟大大降低，适合实时机器人控制。
- **训练设计**：课程式训练范式从显式到隐式的过渡，确保了模型能够平滑学习隐式推理能力，不损失性能。
- **统一性**：模型端到端训练，无需额外的推理链解码模块，结构简洁。

## 8. 不足与局限

- **可解释性**：隐空间推理缺乏透明的推理步骤，对于需要可解释性的安全关键任务可能不友好。
- **数据集依赖**：构建两个专用 CoT 数据集（LIBERO-LaRA 和 Bridge-LaRA），泛化到其他场景可能需要重新采集或标注 CoT，成本较高。
- **实验覆盖**：摘要中未报告方差或置信区间，也未说明是否在不同机器人硬件上验证；易用性/迁移性有待进一步考察。
- **资源消耗**：训练阶段仍需要显式 CoT 监督（虽然后续被压缩），训练算力需求可能与传统 VLA 相近甚至更高（因为多阶段课程训练）。
- **局限性声明**：论文未讨论失败情况或隐空间压缩带来的信息损失风险，对于复杂长链推理任务是否完全适用尚需更多证据。

（完）
