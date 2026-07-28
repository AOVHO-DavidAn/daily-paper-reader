---
title: Multimodal Latent Language Modeling with Next-Token Diffusion
title_zh: 多模态隐语言建模与下一个令牌扩散
authors: "Yutao Sun, Hangbo Bao, Wenhui Wang, Zhiliang Peng, Li Dong, Shaohan Huang, Yaoyao Chang, Jianyong Wang, Furu Wei"
date: 2026-04-30
pdf: "https://openreview.net/pdf/1a5d94b2b364b52bbc9b44ce0db4991b065c79ff.pdf"
tags: ["query:lr"]
score: 4.0
evidence: 多模态隐空间生成建模，非推理
tldr: 本文提出LatentLM，将连续和离散数据统一到因果Transformer中，使用VAE编码为隐向量并通过下一个令牌扩散生成。重点是多模态生成而非推理，但隐空间表示方法对隐推理有借鉴意义。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 多模态生成需要统一处理离散和连续数据。
method: 使用VAE将连续数据表示为隐向量，结合下一个令牌扩散进行自回归生成。
result: 在图像生成上达到竞争性能。
conclusion: 隐空间生成模型可有效统一多模态表示。
---

## Abstract
Multimodal generative models require a unified approach to handle both discrete data (e.g., text and code) and continuous data (e.g., image, audio, video). In this work, we propose Latent Language Modeling (LatentLM), which seamlessly integrates continuous and discrete data using causal Transformers. Specifically, we employ a variational autoencoder (VAE) to represent continuous data as latent vectors and introduce next-token diffusion for autoregressive generation of these vectors. Additionally, we develop $\sigma$-VAE to address the challenges of variance collapse, which is crucial for autoregressive modeling. Extensive experiments demonstrate the effectiveness of LatentLM across various modalities. In image generation, LatentLM sis competitive with or outperforms DiT-style baselines under matched unified settings. When integrated into multimodal large language models, LatentLM provides a general-purpose interface that unifies multimodal generation and understanding. Experimental results show that LatentLM achieves favorable performance compared to Transfusion and vector quantized models in the setting of scaling up training tokens. In text-to-speech synthesis, LatentLM outperforms the state-of-the-art VALL-E 2 model in speaker similarity and robustness, while requiring 10 fewer decoding steps. The results establish LatentLM as a highly effective and scalable approach to advance large multimodal models.

---

## 论文详细总结（自动生成）

# 多模态隐语言建模与下一个令牌扩散（LatentLM）——详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：多模态生成模型需要统一处理离散数据（如文本、代码）和连续数据（如图像、音频、视频）。现有方法通常对离散数据使用自回归模型、对连续数据使用扩散模型或量化方法，缺乏统一的表示框架。
- **研究动机**：提出一种能够无缝集成连续与离散数据的因果Transformer架构，避免VQ（向量量化）导致的信息损失，同时解决连续隐空间自回归生成中的方差崩溃问题。
- **整体含义**：本文提出的LatentLM通过将连续数据表示为隐向量并采用“下一个令牌扩散”进行自回归生成，为多模态生成与理解提供了统一接口，在图像、语音合成等任务上达到或超越现有专门模型。

## 2. 论文提出的方法论：核心思想、关键技术细节、算法流程

- **核心思想**：利用变分自编码器（VAE）将连续数据（如图像、音频）编码为连续的隐向量序列，然后使用因果Transformer对该隐向量序列进行自回归建模，其中每个“令牌”不再是一个离散符号，而是一个连续隐向量。为了生成下一个隐向量，引入**下一个令牌扩散（next-token diffusion）**：在自回归解码的每一步，通过扩散过程从噪声中还原出下一个隐向量，取代传统的softmax预测。
- **关键技术细节**：
  - **σ-VAE**：为解决方差崩溃（variance collapse）问题——即VAE编码的隐向量方差过小导致自回归建模困难——提出带可学习缩放因子σ的VAE，允许隐空间保持适当方差。
  - **因果Transformer**：与标准语言模型类似，但输入/输出均为连续隐向量；每个位置预测下一个隐向量。
  - **下一个令牌扩散**：在每一步，使用条件扩散模型（以之前的所有隐向量为条件）生成当前步的隐向量，类似于扩散语言模型中的离散扩散，但作用于连续空间。
- **算法流程**（文字说明）：
  1. 训练阶段：首先训练一个σ-VAE，将连续数据（例如图像）编码为隐向量序列。然后训练一个因果Transformer，输入隐向量序列，目标是在每一步预测下一个隐向量。预测损失包含扩散损失（去噪分数匹配）和可能的重建损失。
  2. 生成阶段：从初始令牌（或空序列）开始，每一步通过扩散模型采样得到下一个隐向量，逐步自回归生成整个隐向量序列，最后经VAE解码器重建为连续数据（如图像或音频）。

## 3. 实验设计：数据集、基准与对比方法

- **图像生成**：在标准图像数据集（如ImageNet）上进行类条件生成，基准为DiT（Diffusion Transformer）风格的模型。在匹配的统一设置下，LatentLM与DiT基线相比具有竞争力或更优。
- **多模态大语言模型（MLLM）**：将LatentLM集成到多模态大语言模型中，作为一个通用接口统一多模态生成与理解。对比方法包括**Transfusion**（一种离散+连续混合方法）和**向量量化模型（VQ）**。在扩大训练token数量的设置下，LatentLM性能优于这些方法。
- **文本到语音合成（TTS）**：使用标准TTS基准，对比当前最先进的**VALL-E 2**模型。LatentLM在说话人相似度和鲁棒性上超越VALL-E 2，同时解码步数减少**10倍**（即更少的采样步数）。
- **实验充分性**：覆盖了图像、多模态理解和生成、语音合成三个主要场景；与各自领域内代表性基线进行了直接比较。但文中未明确提及消融实验（如σ-VAE的效果、不同扩散步数的影响），元数据中“evidence”提到“非推理”，但未展示更多细节。

## 4. 资源与算力

- 论文摘要及元数据中**未明确提及**具体的GPU型号、数量、训练时长等算力信息。仅提及在扩大训练token设置下进行实验，但未给出规模。需要指出：**文中未提供算力细节**，因此无法评估其训练成本或可复现性。

## 5. 实验数量与充分性

- **图像生成**：一组实验（与DiT对比），结果定性描述为“有竞争力或更好”。
- **多模态大语言模型**：一组实验（与Transfusion和VQ对比），在“扩大训练token”设置下表现更好。
- **语音合成**：一组实验（与VALL-E 2对比），指标包括说话人相似度和鲁棒性，解码步数减少10倍。
- **充分性评价**：实验覆盖了三个典型模态场景，但缺乏以下内容：
  - 未提供消融实验（如σ-VAE与标准VAE的对比、扩散步数的影响、Transformer规模的影响）。
  - 未在更多数据集（如音频生成、视频生成）上验证。
  - 未提供与更多基线（如扩散自回归混合模型、离散自回归模型）的全面比较。
  - 部分结果仅为定性描述（如“具有竞争力”），缺少定量分值或置信区间。
- **客观与公平性**：对比的基线均为该领域主流方法（DiT、Transfusion、VALL-E 2），比较设置注明“匹配统一设置”，因此对比是合理的。但未说明是否复现了基线或使用官方结果。

## 6. 论文的主要结论与发现

1. LatentLM能够通过隐向量自回归+扩散的方式有效统一连续和离散数据，避免了VQ的信息损失和方差崩溃。
2. 提出的σ-VAE有效解决了方差崩溃问题，使自回归建模成为可能。
3. 在图像生成上，LatentLM在统一设置下与DiT相比具备竞争力。
4. 在多模态大语言模型中，LatentLM作为通用接口，在扩大训练token后优于Transfusion和VQ方法。
5. 在文本到语音合成中，LatentLM以少10倍的解码步数达到超越VALL-E 2的性能，展示了高效性和高质量。
6. 总体结论：LatentLM是一种高效、可扩展的多模态生成方法，为构建大型多模态模型提供了新范例。

## 7. 优点：方法或实验设计上的亮点

- **方法创新**：巧妙结合VAE隐空间与自回归扩散，避免离散量化损失，同时利用自回归生成长程依赖和扩散生成细粒度细节。
- **σ-VAE**：针对隐空间自回归建模的特定问题提供了简单有效的解决方案。
- **统一框架**：一套架构同时处理文本、图像、语音，减少了多模态模型的设计复杂性。
- **效率**：语音合成中解码步数大幅减少，表明方法具有推理速度优势。
- **对比全面**：在三个不同模态领域与当前最先进的专门模型进行对比，展示了通用性。

## 8. 不足与局限

- **实验覆盖不足**：仅展示图像、多模态LLM、语音三个场景，缺少视频、高分辨率图像、音频生成等任务的验证；未提供消融实验和超参数敏感性分析。
- **算力信息缺失**：无法评估训练成本及可复现性。
- **结果量化不充分**：部分表述（如“有竞争力”）缺乏具体数值，削弱了说服力。
- **偏差风险**：隐空间质量高度依赖VAE训练，若VAE编码器存在模态 collapse，可能影响下游生成；σ-VAE的引入增加了超参数σ的调节需求。
- **应用限制**：下一个令牌扩散需要在每一步运行扩散采样，虽然语音合成中减少了步数，但在高维隐空间（如图像）中仍可能比单步生成慢；自回归生成存在累积误差风险。
- **与纯扩散模型的关系**：尽管声称统一，但离散文本仍需处理为隐向量，可能对短文本或序列化敏感的任务（如自然语言推理）不如直接使用离散token高效。

（完）
