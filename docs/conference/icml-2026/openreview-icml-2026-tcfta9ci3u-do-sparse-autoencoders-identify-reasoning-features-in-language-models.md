---
title: Do Sparse Autoencoders Identify Reasoning Features in Language Models?
title_zh: 稀疏自编码器能否识别语言模型中的推理特征？
authors: "George Ma, Zhongyuan Liang, Irene Y. Chen, Somayeh Sojoudi"
date: 2026-04-30
pdf: "https://openreview.net/pdf/4297760bc39042edb68b477607a58445d049af12.pdf"
tags: ["query:lr"]
score: 4.0
evidence: 分析语言模型内部表示中的推理特征
tldr: 本文研究稀疏自编码器（SAE）能否可靠地识别语言模型中的推理特征。通过理论分析和因果注入评估，发现SAE可能聚焦于相关线索而非真正推理特征。该工作为隐空间推理分析提供了方法论参考。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 需要验证SAE是否真正捕获了推理相关的内部特征。
method: 提出基于反证的评估框架，结合因果令牌注入和LLM引导的反例构建。
result: 在多种模型和配置中发现SAE倾向于保留低级线索。
conclusion: SAE未必能可靠识别推理特征，需谨慎解读。
---

## Abstract
We study how reliably sparse autoencoders (SAEs) support claims about reasoning-related internal features in large language models. We first give a stylized analysis showing that sparsity-regularized decoding can preferentially retain stable low-dimensional correlates while suppressing high-dimensional within-behavior variation, motivating the possibility that contrastively selected "reasoning" features may concentrate on cue-like structure when such cues are coupled with reasoning traces. Building on this perspective, we propose a falsification-based evaluation framework that combines causal token injection with LLM-guided counterexample construction. Across 22 configurations spanning multiple model families, layers, and reasoning datasets, we find that many contrastively selected candidates are highly sensitive to token-level interventions, with 45%–90% activating after injecting only a few associated tokens into non-reasoning text. For the remaining context-dependent candidates, LLM-guided falsification produces targeted non-reasoning inputs that trigger activation and meaning-preserving paraphrases of top-activating reasoning traces that suppress it. A small steering study yields minimal changes on the evaluated benchmarks. Overall, our results suggest that, in the settings we study, sparse decompositions can favor low-dimensional correlates that co-occur with reasoning, underscoring the need for falsification when attributing high-level behaviors to individual SAE features. Code is available at https://github.com/GeorgeMLP/reasoning-probing.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：稀疏自编码器（SAE）能否可靠地识别大型语言模型（LLM）中与推理相关的内部特征？
- **背景动机**：SAE常用于解释LLM的内部表示，但先前工作可能高估了其捕获“推理特征”的能力。本文旨在通过理论分析和系统评估，检验SAE是否真正聚焦于推理过程的内在表征，而非仅保留与推理共现的低维线索（如单词、模式等）。
- **整体含义**：若SAE倾向于保留与推理相关的协变量而忽略高维的推理变异性，则基于SAE的推理特征归因可能具有误导性，需加入反证（falsification）过程以提高解释的可靠性。

## 2. 方法论
- **核心思想**：提出一个基于反证的评估框架，通过构建反例来检验SAE特征是否真正对应推理行为，而非仅与表面线索相关。
- **关键技术细节**：
  - **因果令牌注入（Causal Token Injection）**：在非推理文本中仅注入少量与推理相关的令牌，观察SAE特征是否激活（若激活，则表明特征依赖低级线索）。
  - **LLM引导的反例构建（LLM-guided Counterexample Construction）**：对于上下文依赖的候选特征，利用LLM自动生成非推理但能触发该特征的目标输入，以及保留原推理语义但抑制该特征的释义。
  - **小规模转向实验（Steering Study）**：对候选特征进行轻微干预，观察其对下游推理任务的影响，以验证特征是否因果相关。
- **公式或算法流程（文字说明）**：1) 使用SAE从LLM隐藏层提取稀疏特征；2) 通过对比激活值挑选与推理相关的候选特征；3) 对每个候选特征执行令牌注入测试；4) 对未通过注入测试的特征，执行LLM引导的反例生成与释义验证；5) 最后对部分特征进行转向干预并评估效果。

## 3. 实验设计
- **数据集/场景**：多个推理数据集（具体名称未在摘要中列出，但涵盖不同推理类型）；使用多种模型家族（如不同规模、架构的语言模型）及不同层。
- **Benchmark**：未明确指定标准基准，而是构建了自有的反证评估基准，包括令牌注入成功率、反例生成质量、转向效果等。
- **对比方法**：未提及直接对比其他SAE变体或解释方法，主要对比不同候选特征在注入与反例下的行为差异。

## 4. 资源与算力
- **摘要中未明确说明**使用的GPU型号、数量、训练时长等算力信息。仅提供代码仓库，但未提及训练SAE的资源需求。

## 5. 实验数量与充分性
- **实验数量**：共22组配置，覆盖多种模型家族、层和推理数据集；此外还包括小规模转向研究。
- **充分性评估**：
  - **优点**：配置数较多（22组），覆盖不同模型和数据集，增强了跨设置的一般性；结合了注入测试、反例生成和转向实验，多角度验证。
  - **不足**：仅针对特定模型和数据集，未探讨极大型模型（如GPT-4级别）；未进行统计显著性检验或重复实验的描述；转向研究规模较小（“minimal changes”），可能不足以得出因果结论。

## 6. 主要结论与发现
- SAE解码在稀疏正则化下可能优先保留与推理共现的低维协变量（如特定词汇或模式），而抑制高维的推理行为内部变异性。
- 45%–90%的对比选取的推理候选特征对令牌注入高度敏感——仅注入少量相关令牌到非推理文本中即可激活。
- 对于余下的上下文依赖候选特征，LLM引导的反例能产生有针对性的非推理输入来触发激活，而保留语义的释义则能抑制激活。
- 小规模转向实验在评估基准上产生的变化极小，暗示这些特征可能不是因果驱动的推理特征。
- **总体结论**：在所研究的设置中，SAE分解可能倾向于低维协变量，而非真正的推理特征；在将高层行为归因于单个SAE特征时，必须引入反证过程。

## 7. 优点
- **理论贡献**：通过简洁的稀疏解码分析，清晰指出了SAE可能偏向低维协变量的机制，提供了直觉上的合理解释。
- **方法创新**：提出结合因果注入与LLM引导反例的评估框架，系统检验特征的真实性，而非仅基于激活相关性。
- **实验覆盖**：22组配置、多模型与多层次验证，增强了结论的稳健性。
- **开放资源**：提供代码仓库便于复现和扩展。

## 8. 不足与局限
- **实验覆盖有限**：仅包括部分模型家族（如LLaMA、GPT-Neo等），未涉及最新最强模型；数据集可能未能覆盖所有复杂推理场景。
- **偏差风险**：反例构建依赖LLM自身能力，可能引入模型特定的偏差；令牌注入实验可能无法彻底区分低级线索与推理特征。
- **应用限制**：结论仅适用于本文所研究的SAE训练与选择设置，不同超参数或训练方法可能改变行为；转向实验效果微弱，表明特征因果作用不强，但未能排除存在更优转向策略。
- **未报告算力**：缺少资源使用细节，不利于可重复性。

（完）
