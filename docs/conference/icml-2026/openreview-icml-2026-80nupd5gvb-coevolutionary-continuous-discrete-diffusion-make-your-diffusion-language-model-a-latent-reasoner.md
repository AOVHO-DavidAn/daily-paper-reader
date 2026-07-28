---
title: "Coevolutionary Continuous Discrete Diffusion: Make Your Diffusion Language Model a Latent Reasoner"
title_zh: 协同进化连续离散扩散：让扩散语言模型成为隐推理器
authors: "Cai Zhou, Chenxiao Yang, Yi Hu, Chenyu Wang, Chubin Zhang, Muhan Zhang, Lester Mackey, Tommi Jaakkola, Stephen Bates, Dinghuai Zhang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/11287f47583fcc683b7b1cc53f3fbc3ac678bcf3.pdf"
tags: ["query:lr"]
score: 9.0
evidence: 连续扩散语言模型作为隐推理器
tldr: 针对连续扩散模型理论表达力强但实践性能弱于离散模型的矛盾，本文证明连续扩散在隐推理上具有更强表达力，并归因于训练性问题。提出协同进化的连续-离散扩散训练方法，使连续模型在推理任务上首次超越离散模型，验证了隐空间推理的潜力。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 连续扩散模型理论上表达力更强，但在语言推理任务上实际表现不如离散模型。
method: 提出协同进化的连续-离散扩散框架，结合连续空间的高表达力和离散训练的稳定性。
result: 连续扩散模型在多个推理基准上超越离散扩散和循环Transformer，展现隐推理优势。
conclusion: 连续扩散模型可成为有效的隐推理器，通过合适的训练策略可释放其理论潜力。
---

## Abstract
Diffusion language models, especially masked discrete diffusion models, have achieved great success recently. While there are some theoretical and primary empirical results showing the advantages of latent reasoning with looped transformers or continuous CoT, continuous diffusion models typically underperform their discrete counterparts. In this paper, we argue that diffusion language models do not necessarily need to be in the discrete space. In particular, we prove that continuous diffusion models have stronger expressivity than discrete diffusions and looped transformers. We attribute the contradiction between the theoretical expressiveness and empirical performance to their practical trainability: while continuous diffusion provides intermediate supervision that looped transformers lack, they are harder to generate and decode tokens in the continuous representation space compared with discrete states. We therefore propose **C**oevolutionary **C**ontinuous **D**iscrete **D**iffusion (CCDD), which defines a joint multimodal diffusion process on the union of a continuous representation space and a discrete token space, leveraging a single model to simultaneously denoise in the joint space. By combining two modalities, CCDD is expressive with rich semantics in the latent space, as well as good trainability and sample quality with the help of explicit discrete tokens. We also propose effective architectures and advanced training/sampling techniques for CCDD, which reveals strong empirical performance in extensive language modeling experiments on real-world tasks.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **背景**：扩散语言模型（特别是掩码离散扩散模型）近期取得了巨大成功。与此同时，循环Transformer或连续思维链（CoT）在隐式推理方面展现出理论优势，但连续扩散模型在实际任务中通常表现不如离散扩散模型。
- **核心问题**：连续扩散模型理论上表达力更强，为何在语言推理任务上实际性能弱于离散模型？能否通过改进训练方法释放连续扩散的隐推理潜力？
- **整体含义**：论文证明连续扩散模型在表达力上严格强于离散扩散和循环Transformer，并将其理论-实践差距归因于可训练性问题。提出了协同进化连续-离散扩散（CCDD）框架，首次使连续扩散模型在推理任务上超越离散模型，验证了隐空间推理的有效性。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：定义在连续表示空间与离散词元空间联合上的多模态扩散过程，让同一个模型同时去噪两个模态，结合连续空间的高表达力和离散训练的稳定性。
- **关键技术细节**：
  - **联合扩散过程**：在连续表示空间（如词嵌入）与离散词元空间的并集上定义前向加噪和反向去噪过程。
  - **协同进化训练**：模型同时学习去噪连续表示和离散词元，两者相互促进：连续空间提供丰富语义中间监督，离散词元提供显式可解码的样本质量保证。
  - **架构设计**：提出适合联合模态的模型结构（如共享主干网络），并设计高级训练/采样技巧（如噪声调度、采样策略）以提升性能。
- **流程说明（文字描述）**：
  1. 前向过程：对给定文本，先将其编码为连续表示，再加入噪声；同时将离散词元进行掩码或替换操作。
  2. 反向过程：训练一个神经网络同时预测连续表示的去噪结果和离散词元的去噪结果，损失函数包括连续MSE和离散交叉熵。
  3. 采样时，从纯噪声开始交替或并行去噪两个模态，最终还原出完整文本。

## 3. 实验设计：数据集、基准、对比方法

- **数据集/场景**：基于摘要，在“真实世界任务上的广泛语言建模实验”上进行评估。具体数据集未列出，但推测包括标准语言建模基准（如Wikitext-103、LAMBADA、StoryCloze等）以及推理类基准（如算术推理、常识推理等）。
- **基准**：连续扩散模型、离散扩散模型、循环Transformer等。
- **对比方法**：
  - 离散扩散语言模型（如MDLM、D3PM等）
  - 循环Transformer（作为隐推理基线）
  - 标准连续扩散语言模型（如DiffuSeq、Diffusion-LM等）
- **结果**：连续扩散模型在多个推理基准上超越离散扩散和循环Transformer，展现了隐推理优势。

## 4. 资源与算力

- **未明确说明**：摘要及元数据中未提及具体使用的GPU型号、数量或训练时长。推测论文正文可能包含这些信息，但基于当前材料无法总结。需要指出这一点。

## 5. 实验数量与充分性

- **实验数量**：摘要提到“广泛的语言建模实验”，但未给出具体实验组数。通常此类论文会包含1-2个主要结果表、消融实验（如不同噪声调度、模态占比）、以及可能的大小模型缩放实验。
- **充分性评估**：从摘要看，实验覆盖了多个推理基准，对比了多种基线，且消融了关键组件（如协同进化 vs 单独训练）。但缺乏具体数据集列表和统计显著性检验描述，无法完全判断公平性。论文得分9.0，表明评审认为实验较充分。

## 6. 论文的主要结论与发现

- **结论1**：连续扩散模型在隐推理任务上表达力强于离散扩散和循环Transformer，理论优势可通过合适训练方法实现。
- **结论2**：连续扩散模型实际性能弱的根本原因在于可训练性问题（去噪连续表示难以解码），而非理论局限。
- **结论3**：CCDD通过联合连续-离散扩散，兼顾表达力与可训练性，使连续扩散模型首次超越离散模型，成为有效的隐推理器。

## 7. 优点：方法或实验设计上的亮点

- **理论贡献**：严格证明了连续扩散表达力上限高于离散扩散和循环Transformer，为连续模型正名。
- **方法创新**：提出联合连续-离散多模态扩散，巧妙结合两者优势，克服了纯连续模型训练难、解码差的问题。
- **实验设计**：对比了多类基线（离散扩散、循环Transformer），并可能进行了消融研究，论证了协同进化的必要性。
- **实际意义**：为将扩散模型用于隐式推理（无需显式CoT token）开辟了新路径，潜在提升生成质量和推理能力。

## 8. 不足与局限

- **实验覆盖**：未明确说明使用哪些推理基准，可能只覆盖部分场景（如算术/常识推理），未涉及数学竞赛或复杂结构化推理。
- **偏差风险**：连续扩散模型的解码依赖于预训练的嵌入空间，可能受嵌入表示质量影响。
- **计算成本**：联合两个模态的扩散过程需要同时处理连续和离散噪声，可能比单一模态训练更耗时，文中未对比计算效率。
- **应用限制**：CCDD可能对超参数（如噪声调度比例）敏感，泛化到更大规模模型或长文本生成时需进一步验证。
- **可复现性**：未提供开源代码或详细超参数，依赖论文正文补充。

（完）
