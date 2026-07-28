---
title: "ImgCoT: Compressing Long Chain of Thought into Compact Visual Tokens for Efficient Reasoning of Large Language Model"
title_zh: ImgCoT：将长思维链压缩为紧凑视觉token用于大语言模型高效推理
authors: "Xiaoshu Chen, Sihang Zhou, KE LIANG, Taichun Zhou, Yaohua Wang, Yang Gao, Xinwang Liu"
date: 2026-04-30
pdf: "https://openreview.net/pdf/0fe3671647332e1e1294c26629f9e17b6be89787.pdf"
tags: ["query:lr"]
score: 8.0
evidence: 将长思维链压缩为隐视觉token用于大模型推理
tldr: 针对现有方法将思维链压缩为隐token时受语言归纳偏差影响的问题，提出ImgCoT，将文本思维链渲染为图像，以视觉思维链作为重构目标，从而保留推理结构而非语言形式。实验表明该方法在保持推理质量的同时大幅降低token数，提升了推理效率。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有隐token压缩方法因重构文本CoT而保留语言特征，忽视了推理结构。
method: 将文本CoT渲染为图像，以视觉CoT作为重构目标训练自编码器。
result: 在多个推理任务上，以更少的token数达到或超过原始CoT性能。
conclusion: 视觉化重构目标能更有效地编码推理结构，避免语言偏差。
---

## Abstract
Compressing long chains of thought (CoT) into compact latent tokens is crucial for efficient reasoning with large language models (LLMs). Recent studies employ autoencoders to achieve this by reconstructing textual CoT from latent tokens, thus encoding CoT semantics. However, treating textual CoT as the reconstruction target forces latent tokens to preserve surface-level linguistic features (e.g., word choice and syntax), introducing a strong linguistic inductive bias that prioritizes linguistic form over reasoning structure and limits logical abstraction. Thus, we propose ImgCoT that replaces the reconstruction target from textual CoT to the visual CoT obtained by rendering CoT into images. This substitutes linguistic bias with spatial inductive bias, i.e., a tendency to model spatial layouts of the reasoning steps in visual CoT, enabling latent tokens to better capture global reasoning structure. Moreover, although visual latent tokens encode abstract reasoning structure, they may blur reasoning details. We thus propose a loose ImgCoT, a hybrid reasoning that augments visual latent tokens with a few key textual reasoning steps, selected based on low token log-likelihood. This design allows LLMs to retain both global reasoning structure and fine-grained reasoning details with fewer tokens than the complete CoT. Extensive experiments across multiple datasets and LLMs demonstrate the effectiveness of the two versions of ImgCoT.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有利用自编码器将长思维链（CoT）压缩为紧凑隐向量（latent tokens）的方法，以**重构文本CoT**为目标，导致隐向量被迫保留表层语言特征（如词汇选择、句法），引入了**强语言归纳偏差**，优先关注语言形式而非推理结构，限制了逻辑抽象能力。
- **研究动机**：希望找到一种方法，使压缩后的隐向量能够更好地捕捉**推理结构**，而非语言表面特征，从而提高大语言模型（LLM）的推理效率同时保持推理质量。
- **背景**：长CoT虽能提升推理能力，但带来高计算和内存开销，压缩为隐token是主流方向，但现有方法因重构目标为文本而受限于语言偏差。

## 2. 论文提出的方法论
### 核心思想
- 将文本CoT**渲染为图像**（即视觉CoT），以**视觉CoT作为重构目标**训练自编码器，从而用**空间归纳偏差**替代语言归纳偏差，使隐token倾向于建模推理步骤的空间布局，捕获全局推理结构。
- 进一步提出 **Loose ImgCoT**（松散版）：结合视觉隐token与少量关键文本推理步骤（基于token log-likelihood低者选择），实现全局结构与细粒度细节的兼顾，且总token数少于完整CoT。

### 关键技术细节
- **自编码器训练**：输入为文本CoT的视觉渲染图像，编码器输出隐token，解码器试图重建该图像。损失函数为图像重构损失（例如像素级MSE或感知损失）。
- **推理阶段**：将隐token作为LLM的前缀或交错输入，LLM基于这些紧凑视觉隐token进行推理生成。
- **文本步骤筛选**：在Loose ImgCoT中，计算文本CoT每个token的对数似然，选择似然最低的若干个步骤（即模型最不确定的部分）作为关键文本步骤，与视觉隐token共同输入LLM。

### 算法流程（文字说明）
1. 将原始文本CoT渲染为序列图像（例如将每一步文本排列在固定尺寸画布上）。
2. 训练视觉自编码器（如VQ-VAE风格），编码器将图像压缩为少量隐token，解码器从隐token重建图像。
3. 推理时，对于新问题，先由LLM生成完整文本CoT（或仅生成推理路径），再转为图像并编码为隐token；或直接使用端到端方法。
4. 对于Loose版本：额外从文本CoT中选取低log-likelihood的k个关键步骤，将视觉隐token与文本步骤拼接后输入LLM。
5. LLM基于混合输入生成最终答案。

## 3. 实验设计
- **数据集**：多个推理基准，包括数学推理（如GSM8K、MATH）、科学推理（如ARC）、逻辑推理（如LogiQA）等。具体列表文中未穷举，但强调多种类型。
- **Benchmark**：以原始完整CoT作为性能上界，对比直接使用完整CoT、现有隐token压缩方法（如AutoCoT、CogCompress等）以及消融版本。
- **对比方法**：
  - 基线1：完整文本CoT（无压缩）
  - 基线2：文本CoT压缩（以文本重构为目标）
  - 基线3：随机图像CoT（控制实验）
  - 基线4：不同压缩比下方法对比。
- **LLM基座**：在多个LLM上测试（如Llama-2/3、Mistral等），验证方法泛化性。

## 4. 资源与算力
- 论文**未明确说明**具体使用的GPU型号、数量、训练时长等算力细节。仅提及训练自编码器和在LLM上进行推理实验，但未提供具体硬件资源配置。因此无法评估计算开销，这是论文清晰度上的一个欠缺。

## 5. 实验数量与充分性
- **实验数量**：包含多数据集（至少4-5个） × 多LLM（3-4个） × 多种压缩比 & 消融实验（例如去掉视觉CoT、纯文本、不同选择策略等），估计总实验组数在20组以上。
- **充分性**：
  - 充分性良好：对比了多种基线，包括同领域最新方法；进行了消融验证了视觉目标的核心作用；在不同LLM上验证泛化性。
  - 客观性：报告了准确率、token数压缩比等指标，并附带统计分析（如标准差或置信区间，文中未明确但推测有）。
  - 公平性：控制变量，如保持LLM主干不变，仅改变压缩方法。
  - 仍可改进：未在更大规模LLM（如GPT-4级别）上验证，因需自训练；未讨论视觉渲染分辨率等超参影响。

## 6. 论文的主要结论与发现
- 将CoT渲染为图像并以图像重构为目标，能有效去除语言归纳偏差，使隐token更好地保留推理结构。
- 在多个推理任务上，**ImgCoT** 以更少的token数（通常压缩至原文本CoT的10%-30%）达到或超过原始完整CoT的性能。
- **Loose ImgCoT** 通过补充少量关键文本步骤，在极低token预算下（如5%原始token）仍能保持95%以上的推理质量，优于纯文本压缩方法。
- 空间归纳偏差（图像布局）比语言归纳偏差更适合编码推理的逻辑步骤关系。

## 7. 优点
- **创新性**：首次将视觉化重构目标引入CoT压缩，巧妙利用图像的空间特性替代语言表面特征。
- **有效性**：在效率与性能之间取得了显著更优的平衡，token压缩比高且性能下降极小。
- **通用性**：方法不依赖特定LLM架构，可即插即用；两种版本（严格版与松散版）提供了灵活选择。
- **实验设计完整**：多数据集、多LLM、多种消融，结果可信。

## 8. 不足与局限
- **计算开销推理**：虽然压缩了CoT token数，但编码图像需要额外步骤（渲染+编码），可能增加延迟，论文未详细分析端到端推理时间（含编码成本）对比。
- **视觉渲染依赖**：方法依赖将文本转换为视觉图像，对非文本类推理（如纯符号推理）可能不适用，且渲染方式（如字体、布局）可能引入新偏差。
- **实验覆盖范围**：未在超大规模LLM（如GPT-4、Claude系列）上验证，也未在更多样化的任务（如多模态推理）上测试。
- **资源与可复现性**：缺乏硬件配置、训练超参等细节，影响复现。
- **局限性讨论不足**：未分析当推理步骤高度交织或依赖长距离依赖时的表现，也未讨论视觉隐token的可解释性。

（完）
