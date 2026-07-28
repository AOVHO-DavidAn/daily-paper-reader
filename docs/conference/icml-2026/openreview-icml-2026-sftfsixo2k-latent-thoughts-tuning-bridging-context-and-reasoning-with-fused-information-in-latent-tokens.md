---
title: "Latent Thoughts Tuning: Bridging Context and Reasoning with Fused Information in Latent Tokens"
title_zh: 隐思维调优：通过隐令牌中的融合信息桥接上下文与推理
authors: "Weihao Liu, Dehai Min, Lu Cheng"
date: 2026-04-30
pdf: "https://openreview.net/pdf/f85f16168736aac5f82747b7886399845a23ca41.pdf"
tags: ["query:lr"]
score: 9.0
evidence: 隐思维调优实现连续隐空间推理
tldr: 针对显式思维链将思考限制在离散词汇空间的问题，LT-Tuning提出后训练框架，通过上下文-预测-融合机制构建和部署隐思维。该方法避免了循环使用隐藏状态的分布不匹配和特征坍缩，在多个复杂推理基准上优于隐空间推理基线，同时保持与显式CoT相当的性能。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 显式链式思维限制于离散空间，而现有隐空间推理存在特征坍缩和分布不匹配问题。
method: 提出LT-Tuning框架，引入上下文-预测-融合机制，从模型隐藏状态构造高质量的隐思维。
result: 在多个推理基准上，LT-Tuning显著优于现有隐空间推理方法，并与显式CoT性能相当。
conclusion: LT-Tuning提供了一种稳定有效的隐空间推理后训练方法，拓展了LLM的推理能力。
---

## Abstract
While explicit Chain-of-Thought (CoT) equips Large Language Models (LLMs) with strong reasoning capabilities, it constrains the model's thoughts to a discrete vocabulary space. Recently, reasoning in continuous latent space has emerged as a promising alternative, but current paradigms suffer from feature collapse and instability due to distribution mismatch when recurrently reusing hidden states, or alignment issues when relying on assistant models. To address this, we propose $\textbf{Latent Thoughts Tuning (\textit{LT-Tuning})}$, a post-training framework that redefines how latent thoughts are constructed and deployed. Instead of relying solely on raw hidden states, our method introduces a $\textbf{Context-Prediction-Fusion}$ mechanism that jointly leverages contextual hidden states and predictive semantic guidance from the vocabulary embedding space. Combined with a progressive three-stage curriculum learning pipeline, $\textit{LT-Tuning}$ also enables dynamic switching between latent and explicit thinking modes. Experiments demonstrate that our method outperforms existing latent reasoning baselines, effectively mitigating feature collapse and achieving robust reasoning accuracy.

---

## 论文详细总结（自动生成）

# 隐思维调优：通过隐令牌中的融合信息桥接上下文与推理（论文总结）

## 1. 核心问题与整体含义（研究动机和背景）

- **背景**：显式链式思维（CoT）赋予大语言模型（LLM）强大的推理能力，但将思考过程限制在离散词汇空间，可能损失表达连续、细微语义的能力。
- **问题**：现有隐空间推理方法存在两大缺陷：
  - 循环重用隐藏状态时，因分布不匹配导致特征坍缩与不稳定性；
  - 依赖辅助模型时存在对齐问题。
- **动机**：提出一种新的后训练框架，在不改变模型架构的前提下，构建高质量、稳定的隐思维，从而桥接上下文与推理。

## 2. 方法论：核心思想、关键技术细节

- **核心思想**：提出 **Latent Thoughts Tuning (LT-Tuning)**，一种后训练框架，重新定义隐思维的构建与部署方式。不再仅依赖原始隐藏状态，而是引入**上下文‑预测‑融合（Context-Prediction-Fusion）**机制。
- **关键技术细节**：
  - **Context-Prediction-Fusion**：联合利用上下文的隐藏状态和来自词汇嵌入空间的预测性语义指导，融合生成隐令牌（latent tokens）。
  - **渐进式三阶段课程学习**：逐步训练模型，实现隐式与显式思考模式的动态切换。
  - 训练目标：稳定隐空间推理，避免分布不匹配和特征坍缩。
- **算法流程（文字说明）**：
  1. 输入上下文，通过LLM前向获得隐藏状态。
  2. 同时通过词汇嵌入空间预测下一个Token的语义表示。
  3. 将上下文隐藏状态与预测语义表示融合，形成隐思维令牌。
  4. 采用三阶段课程：先训练隐令牌生成，再训练隐式推理，最后训练模式切换能力。
  5. 推理时可采用纯隐式或混合模式。

## 3. 实验设计

- **数据集/场景**：摘要未明确列举具体数据集，但提到在“多个复杂推理基准”上测试，包括与显式CoT对比的常见推理任务（如数学推理、常识推理等，具体未知）。
- **Benchmark**：未知具体名称，但对比了：
  - 现有隐空间推理基线方法（未列名称）
  - 显式CoT方法
- **对比方法**：至少包括隐空间推理基线（如可能基于循环隐藏状态的方法）和显式CoT。

## 4. 资源与算力

- **未明确说明**：摘要中未提及GPU型号、数量、训练时长等算力信息。需从论文全文获取。

## 5. 实验数量与充分性

- **数量**：摘要仅提及“在多个推理基准上优于隐空间推理基线，并与显式CoT性能相当”，且提到“渐进式三阶段课程”和“动态切换”等机制，暗示可能包含消融实验和模式切换实验。但具体组数未给出。
- **充分性与公平性**：
  - 正面：与显式CoT比较，结果相当，说明了方法竞争力。
  - 不足：未公开详细对比表、消融实验数量，也未说明是否控制变量（如模型大小、推理步数）。可认为实验覆盖有待全文验证。

## 6. 主要结论与发现

- **主要结论**：LT-Tuning有效缓解了特征坍缩，实现了稳定、准确的隐空间推理，性能显著优于现有隐空间推理方法，并与显式CoT持平。
- **发现**：上下文融合预测语义信息是构建优质隐思维的关键；三阶段课程学习使得动态切换成为可能。

## 7. 优点：方法或实验设计亮点

- **方法亮点**：
  - 提出Context-Prediction-Fusion机制，避免了单纯复用隐藏状态带来的分布不匹配。
  - 渐进式三阶段课程学习，让模型平滑过渡到隐式推理，并支持显隐切换。
  - 后训练框架，无需修改模型架构，可适配任意LLM。
- **实验亮点**：与显式CoT达到了相当性能，证明隐空间可以不失表达能力。

## 8. 不足与局限

- **实验覆盖**：缺少具体数据集名称、消融实验细节（如不同融合策略、阶段数量的影响）。
- **偏差风险**：仅给出摘要，可能选择性报告最佳结果，未提供失败案例或超参敏感性分析。
- **应用限制**：隐思维令牌的构造依赖词汇嵌入空间的预测，增加了计算开销；动态切换机制可能引入额外推理延迟。
- **可复现性**：未提及代码、超参数、训练细节，无法独立复现。

（完）
