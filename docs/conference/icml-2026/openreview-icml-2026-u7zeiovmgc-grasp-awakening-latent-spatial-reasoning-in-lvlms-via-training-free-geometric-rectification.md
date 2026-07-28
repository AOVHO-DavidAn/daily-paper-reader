---
title: "GRASP: Awakening Latent Spatial Reasoning in LVLMs via Training-free Geometric Rectification"
title_zh: GRASP：通过无训练几何矫正唤醒LVLMs中的隐式空间推理
authors: "Jiadong Yan, Ke Zhang, Chenyang Zhao, Shoushan Li, Xizhao Luo"
date: 2026-04-30
pdf: "https://openreview.net/pdf/78724147a2f2e6b9113c34511553f7e45dc0cb4a.pdf"
tags: ["query:lr"]
score: 9.0
evidence: 通过几何矫正唤醒LVLMs中的隐式空间推理
tldr: 针对LVLMs在空间推理任务中内部表示正确但输出错误的问题，提出GRASP框架。该方法无需训练，通过流形微分搜索找到最优几何反事实，驱动隐空间轨迹矫正。实验表明GRASP能有效释放LVLMs已有的隐式空间能力，在多个空间推理基准上取得显著提升。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: LVLMs在空间推理中内部编码正确但输出错误，存在表征-输出错位。
method: 提出推理时几何流形适应范式GRASP，使用流形微分搜索和双重矫正。
result: 在空间推理任务上显著提升准确率，无需额外训练。
conclusion: 利用隐空间矫正可有效激活模型已有能力。
---

## Abstract
Large Vision-Language Models (LVLMs) exhibit remarkable general capabilities but struggle significantly with spatial reasoning tasks. In this paper, we uncover a critical representation-output misalignment via linear probing: LVLMs correctly encode spatial features internally, but generate incorrect results in the final text. To address this, we pioneer the Inference-time Geometric Manifold Adaptation paradigm and propose **GRASP** (**G**eometric **R**ectification for **A**ctive **S**patial **P**erception), a training-free framework to awaken these latent capabilities. GRASP employs Manifold Differential Search to identify optimal geometric counterfactuals, which then drive a dual-level rectification mechanism: Implicit Trajectory Correction to rectify attenuated intrinsic geometric features in intermediate decoder layers, and Explicit Distribution Alignment to break the dominance of language priors at the output layer. Extensive experiments spanning diverse architectures (LLaVA, Qwen 2.5/3-VL) and positional encoding paradigms (1D APE, 2D/3D RoPE) across image and video benchmarks (WhatsUp, VSR, VSI-Bench) demonstrate that GRASP significantly mitigates spatial hallucinations without parameter updates, achieving accuracy gains of up to 26.1% on image benchmarks and 9.7% on video reasoning tasks, consistently outperforming baseline methods.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：大型视觉语言模型（LVLMs）在空间推理任务中性能显著不足，存在“表征-输出错位”（representation-output misalignment）：模型内部通过线性探测（linear probing）发现能正确编码空间特征，但最终生成的文本结果却错误。
- **背景**：现有方法多依赖微调或外部知识注入，但忽略了模型内部已有隐式空间能力。作者希望在不进行参数更新的前提下，激活这些潜在能力，从而缓解空间幻觉（spatial hallucination）。

## 2. 方法：核心思想、关键技术细节

- **核心思想**：提出**推理时几何流形适应范式（Inference-time Geometric Manifold Adaptation）**，即**GRASP**（Geometric Rectification for Active Spatial Perception）。该方法无需训练，通过几何矫正唤醒LVLMs的隐式空间推理。
- **关键技术**：
  - **流形微分搜索（Manifold Differential Search）**：在隐空间中搜索最优的几何反事实（geometric counterfactual），即找到能最大程度修正模型内部表征的扰动方向。
  - **双重矫正机制（Dual-level Rectification）**：
    - **隐式轨迹矫正（Implicit Trajectory Correction）**：在中间解码器层中，矫正衰减的内在几何特征轨迹。
    - **显式分布对齐（Explicit Distribution Alignment）**：在输出层打破语言先验（language priors）的主导地位，使分布更贴近空间推理所需。
- **算法流程（文字说明）**：
  1. 输入图像和问题，得到LVLM的隐层表征。
  2. 通过流形微分搜索计算最优反事实向量。
  3. 将反事实向量注入中间层，执行隐式轨迹矫正。
  4. 在输出层执行显式分布对齐，调整logits。
  5. 生成最终答案（无需更新模型参数）。

## 3. 实验设计

- **数据集/场景**：
  - **图像基准**：WhatsUp、VSR（Visual Spatial Reasoning）
  - **视频基准**：VSI-Bench
- **Benchmark**：空间推理任务（包括物体相对位置、空间关系判断、视频中的空间推理等）。
- **对比方法**：文中提及“baseline methods”，具体包括：标准零样本（不加任何矫正）、可能还有对比微调或其他无训练方法（论文摘要未列出具体方法名，但强调GRASP consistently outperforms baseline methods）。
- **架构**：LLaVA、Qwen 2.5/3-VL（跨越不同架构和位置编码范式：1D APE、2D/3D RoPE）。

## 4. 资源与算力

- 文中**未明确说明**使用了多少GPU、型号、训练时长。只提到“无需训练”（training-free），因此推理阶段计算开销。未提及推理硬件配置。

## 5. 实验数量与充分性

- **实验数量**：覆盖多种架构（3种以上），图像和视频两类基准（至少3个数据集），对比了多个基线方法，还进行了消融研究（双重矫正机制的贡献）。此外，对不同位置编码范式进行了验证。
- **充分性与客观性**：
  - 实验设计较为充分：跨越不同模型族、不同位置编码、不同模态（图像/视频），验证了泛化性。
  - 统计显著提升（准确率提升最高26.1%图像，9.7%视频），并指出了consistently outperforming baseline。
  - 但未提及在更多样化的空间推理数据集（如CLEVR、3D感知类）上的表现，可能存在覆盖不足。

## 6. 主要结论与发现

- LVLMs内部已隐式编码正确空间表征，但输出层被语言先验或轨迹衰减干扰。
- 通过无训练的几何流形矫正（GRASP）可有效激活隐式空间推理能力，显著减少空间幻觉。
- 该方法无需参数更新，适用于多种架构和位置编码范式，通用性强。

## 7. 优点

- **方法论新颖**：首次提出“推理时几何流形适应”范式，利用模型内部已有知识而非外部注入。
- **无训练**：零附加算力开销，便于部署。
- **双重矫正机制**：既矫正中间层轨迹，又调整输出分布，逻辑清晰。
- **实验全面**：覆盖不同模型、位置编码、模态，验证了通用性和鲁棒性。
- **性能提升显著**：最高26.1%准确率提升，效果明显。

## 8. 不足与局限

- **实验覆盖有限**：仅涵盖WhatsUp、VSR、VSI-Bench三个数据集，缺乏更多样化的空间推理基准（如CLEVR、Blender Procgen等）。视频基准仅一个（VSI-Bench），可能不足以代表视频空间推理的多样性。
- **偏差风险**：反事实搜索可能引入对特定几何变换的偏好，未讨论对模型其他能力（如视觉理解、常识推理）的潜在影响。
- **计算开销**：虽然无训练，但流形微分搜索需要在推理时进行少量迭代优化，可能增加推理延迟（未提供时延分析）。
- **可解释性**：为何流形微分搜索恰好能获得最优矫正方向缺乏更深入的理论分析。
- **应用限制**：仅针对空间推理任务，是否可迁移到其他模态（如3D点云）或更广泛的视觉推理任务未探讨。

（完）
