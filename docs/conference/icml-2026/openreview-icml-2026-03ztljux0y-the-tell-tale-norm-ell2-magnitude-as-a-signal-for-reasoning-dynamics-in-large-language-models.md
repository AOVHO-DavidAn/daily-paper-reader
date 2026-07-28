---
title: "The Tell-Tale Norm: $\\ell_2$ Magnitude as a Signal for Reasoning Dynamics in Large Language Models"
title_zh: 告密范数：l2幅度作为大语言模型推理动态的信号
authors: "Jinyang Zhang, Hongxin Ding, Yue Fang, Weibin Liao, Muyang Ye, Junfeng Zhao, Yasha Wang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/8c99eb36bf751b2a852b58cdd3d31a3f6d3c2186.pdf"
tags: ["query:lr"]
score: 6.0
evidence: 隐藏状态l2范数作为大模型推理动态的信号
tldr: 本文发现大语言模型隐藏状态的l2范数可以作为推理强度的内生信号，利用稀疏自编码器观察到推理特征激活在后期层中急剧上升。理论上证明了隐藏状态范数约束了推理特征的激活强度，为理解模型内部推理动态提供了新的分析工具。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 缺乏一种模型内生的、能捕捉逐层推理动态的原则性信号。
method: 通过稀疏自编码器探测推理特征，并建立l2范数与推理强度的理论联系。
result: 验证了l2范数在后期层与推理特征激活高度相关。
conclusion: l2范数是一种有效的推理动态指示器，可用于分析模型行为。
---

## Abstract
Recent work has sought to understand Large Language Models (LLMs) reasoning, yet a principled, model-intrinsic signal that captures its *layer-wise reasoning dynamics* remains underexplored. We bridge this gap by demonstrating that **the $\ell_2$ norm of hidden states serves as an endogenous signal of the model's reasoning intensity**. Using Sparse Autoencoders (SAEs) as a diagnostic probe, we observe that LLMs' internal reasoning is marked by a sharp increase in reasoning feature activations concentrated in late layers. Motivated by this pattern, we establish a formal link between reasoning intensity and the model's latent geometry and theoretically prove that the $\ell_2$ norm of hidden states bounds the activation strength of SAE reasoning features. Empirical correlation analysis and causal interventions further prove $\ell_2$ norm as a faithful indicator, where heightened norms consistently correspond to critical reasoning steps. We then introduce three test-time scaling techniques guided by $\ell_2$ norms: Adaptive Layer-wise Reasoning Recursion, (ii) Endogenous Reasoning State Steering, and (iii) $\ell_2$-guided Response Selection, which requires no additional training or data and is compatible with advanced inference engines. Experiments across model architectures and benchmarks show that $\ell_2$-norm-based techniques significantly improve reasoning performance, offering a principled yet simple lens to perceive and control LLM latent reasoning dynamics. Our codes are available at https://github.com/zjy1298/The-Tell-Tale-Norm.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

现有研究试图理解大语言模型（LLMs）的推理机制，但缺乏一种 **模型内生的、能捕捉逐层推理动态的原则性信号**。现有方法多依赖外部探测或行为分析，无法直接利用模型自身的隐藏状态来指示推理强度。本文旨在填补这一空白，提出将隐藏状态的 **ℓ2 范数** 作为推理强度的内生信号，从而提供一种简单而有效的分析工具，用于感知和控制 LLM 的推理动态。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：隐藏状态的 ℓ2 范数能够反映模型推理特征的激活强度，尤其是在后期层中推理特征急剧上升，与 ℓ2 范数高度相关。
- **关键技术细节**：
  - 使用 **稀疏自编码器（Sparse Autoencoders, SAEs）** 作为诊断探针，从隐藏状态中分离出与推理相关的特征。
  - 理论上证明：隐藏状态的 ℓ2 范数约束了 SAE 推理特征的激活强度（即 ℓ2 范数上界与推理特征激活强度存在形式化联系）。
  - 提出三种基于 ℓ2 范数的测试时缩放技术（无需额外训练或数据，兼容高级推理引擎）：
    1. **自适应逐层推理递归（Adaptive Layer-wise Reasoning Recursion）**：根据层间 ℓ2 范数变化动态调整递归次数。
    2. **内生推理状态引导（Endogenous Reasoning State Steering）**：利用 ℓ2 范数识别关键推理状态，进行状态导向。
    3. **ℓ2 引导的响应选择（ℓ2-guided Response Selection）**：基于 ℓ2 范数选择高质量响应。
- **核心公式/理论证明**（文字说明）：论文从数学上建立了推理强度与隐藏状态几何的正式联系，证明 ℓ2 范数是 SAE 推理特征激活强度的上界约束。

## 3. 实验设计

- **数据集/场景**：论文未明确列出具体数据集名称，仅说明“在多种模型架构和基准上进行了实验”。通常这类工作会使用数学推理基准（如 GSM8K, MATH, SVAMP 等），但此处信息缺失。
- **Benchmark**：未指定具体基准，仅提及跨模型架构和基准测试。
- **对比方法**：论文未列出具体对比基线，但强调了所提三种技术 **无需额外训练或数据**，且兼容高级推理引擎。可能存在与其他测试时缩放或推理增强方法的对比，但摘要未详述。

## 4. 资源与算力

论文中 **未明确提及** 使用的 GPU 型号、数量或训练时长。仅说明三种技术无需额外训练，因此算力消耗可能主要来自推理过程中的 ℓ2 范数计算和稀疏自编码器的前向传播（SAE 是预训练的）。具体算力信息缺失。

## 5. 实验数量与充分性

- **实验数量**：摘要中仅报告了“相关性分析和因果干预”验证 ℓ2 范数作为忠实指示器，以及“跨模型架构和基准”的性能提升。未提供具体实验组数（如消融实验、不同层数、不同模型规模、不同数据集的详细对比）。
- **充分性与公平性**：由于缺乏具体数据集、对比方法和消融实验细节，无法判定实验是否充分。因果干预实验（causal interventions）增强了论证的因果关系，但整体实验覆盖度有限，存在一定偏差风险。

## 6. 论文的主要结论与发现

1. 隐藏状态的 ℓ2 范数可以作为模型推理强度的 **内生信号**，在后期层中与稀疏自编码器推理特征激活高度相关。
2. 通过因果干预证明 ℓ2 范数是推理动态的 **忠实指示器**，高范数对应关键推理步骤。
3. 基于 ℓ2 范数的三种测试时缩放技术显著提升了推理性能，且无需额外训练或数据，具有原理性且简单有效。

## 7. 优点（方法或实验设计上的亮点）

- **内生性**：使用模型自身隐藏状态的 ℓ2 范数，避免了外部探针或人工标注的偏差。
- **理论基础**：提供了形式化的数学证明，约束关系清晰，不仅依赖经验观察。
- **实用性**：提出的三种技术无需额外训练，即插即用，兼容现有推理引擎，计算开销小（仅需计算 ℓ2 范数）。
- **因果验证**：采用因果干预实验确认 ℓ2 范数与推理强度的因果关系，而非仅仅相关，增强了结论可信度。

## 8. 不足与局限

- **实验覆盖不足**：未明确列出使用的数据集、对比方法和具体数值结果，仅给出定性结论，难以独立复现和验证。
- **资源信息缺失**：未报告计算资源配置，无法评估方法的实际成本。
- **SAE 依赖**：虽然 ℓ2 范数本身无需 SAE，但论文中 SAE 用于探测推理特征并验证相关性，SAE 的训练质量和特征分离能力可能影响结论的泛化性。
- **应用限制**：ℓ2 范数作为推理信号是否适用于所有任务（如非推理任务、多模态模型、超大规模模型）未经充分验证。另外，高 ℓ2 范数也可能对应其他非推理特征（如重复模式、情绪表达），论文未讨论混淆因素。

（完）
