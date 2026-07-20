---
title: Perception Tokens Enhance Visual Reasoning in Multimodal Language Models
title_zh: 感知令牌增强多模态语言模型中的视觉推理
authors: "Bigverdi, Mahtab, Luo, Zelun, Hsieh, Cheng-Yu, Shen, Ethan, Chen, Dongping, Shapiro, Linda G., Krishna, Ranjay"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Bigverdi_Perception_Tokens_Enhance_Visual_Reasoning_in_Multimodal_Language_Models_CVPR_2025_paper.pdf"
tags: ["query:lr"]
score: 7.0
evidence: 提出感知令牌作为辅助推理的潜在表示
tldr: 多模态语言模型在需要中间空间推理的任务中表现不佳，该论文提出感知令牌(Perception Tokens)作为内在图像表示，充当类似思维链的辅助推理令牌。这种方法避免了微调或调用外部工具，在3D结构和2D检测推理任务上显著提升了模型性能。感知令牌提供了一种轻量级的隐空间推理机制，使MLM能够在不依赖外部模块的情况下进行更准确的视觉推理。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bigverdi-perception-tokens-enhance-visual-reasoning-in-multimodal-language-models-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 856, \"height\": 563, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bigverdi-perception-tokens-enhance-visual-reasoning-in-multimodal-language-models-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1815, \"height\": 485, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bigverdi-perception-tokens-enhance-visual-reasoning-in-multimodal-language-models-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1533, \"height\": 630, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bigverdi-perception-tokens-enhance-visual-reasoning-in-multimodal-language-models-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 868, \"height\": 427, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bigverdi-perception-tokens-enhance-visual-reasoning-in-multimodal-language-models-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1733, \"height\": 520, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bigverdi-perception-tokens-enhance-visual-reasoning-in-multimodal-language-models-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1481, \"height\": 450, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bigverdi-perception-tokens-enhance-visual-reasoning-in-multimodal-language-models-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1470, \"height\": 332, \"label\": \"Table\"}]"
motivation: 多模态语言模型在3D结构和2D实例推理任务中缺乏中间表示，微调泛化差且外部工具计算昂贵。
method: 设计感知令牌作为内在图像表示，以辅助推理令牌的形式参与模型前向传播，类似思维链提示。
result: 在多个视觉推理基准上，感知令牌显著提升了MLM的准确性，且无需外部工具或专门微调。
conclusion: 感知令牌提供了一种高效、可扩展的隐空间推理增强方法，克服了MLM在基本视觉推理上的局限。
---

## Abstract
Multimodal language models (MLMs) still face challenges in fundamental visual perception tasks where specialized models excel. Tasks requiring reasoning about 3D structures benefit from depth estimation, and reasoning about 2D object instances benefits from object detection. Yet, MLMs can not produce intermediate depth or boxes to reason over. Finetuning MLMs on relevant data doesn't generalize well and outsourcing computation to specialized vision tools is too compute-intensive and memory-inefficient. To address this, we introduce Perception Tokens, intrinsic image representations designed to assist reasoning tasks where language is insufficient. Perception tokens act as auxiliary reasoning tokens, akin to chain-of-thought prompts in language models. For example, in a depth-related task, an MLM augmented with perception tokens can reason by generating a depth map as tokens, enabling it to solve the problem effectively. We propose AURORA, a training method that augments MLMs with perception tokens for improved reasoning over visual inputs. AUROA leverages a VQVAE to transform intermediate image representations, such as depth maps into a tokenized format and bounding box tokens, which is then used in a multi-task training framework. AURORA achieves notable improvements across counting benchmarks: +10.8% on BLINK, +11.3% on CVBench, and +8.3% on SEED-Bench, outperforming finetuning approaches in generalization across datasets. It also improves on relative depth: over +6% on BLINK. With perception tokens, AURORA expands the scope of MLMs beyond language-based reasoning, paving the way for more effective visual reasoning capabilities. Code and data will be released at the https://aurora-perception.github.io.

---

## 论文详细总结（自动生成）

# 论文感知令牌增强多模态语言模型中的视觉推理：详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：多模态语言模型（MLM）在需要中间视觉表示（如深度图、边界框）的推理任务中表现不佳。这类任务（如3D相对深度判断、2D目标计数）对于专用视觉模型来说容易解决，但MLM无法生成或利用这些中间表示进行推理。
- **现有方法局限**：
  - 微调MLM在相关数据上：泛化性差，且容易遗忘原有能力。
  - 外接专用工具（如深度估计器、检测器）：计算开销大、内存效率低，且可能引入级联错误。
- **本文意义**：提出一种轻量级、可扩展的方案，通过在MLM内部引入**感知令牌**作为辅助推理表示，使模型能够像语言模型使用思维链一样，先生成中间视觉令牌，再基于这些令牌完成最终推理。该方法避开了外部工具的依赖，同时避免了大规模微调带来的泛化损失。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 核心思想
- 扩展MLM的词汇表，增加一组**感知令牌**（对应于深度图、边界框等视觉表示），让模型在生成最终答案之前，先输出这些令牌作为中间推理步骤，从而增强推理能力。
- 类比于语言模型中的链式思维（Chain-of-Thought），但将中间步骤从语言扩展到视觉感知表示。

### 关键技术细节
1. **感知令牌的生成与映射**：
   - 对于**像素级表示**（如深度图）：训练一个VQVAE，将深度图（320×320）压缩为10×10的离散代码网格（共100个令牌），代码本大小为128，每个令牌对应代码本索引。引入特殊令牌 `<DEPTH_START>`、`<DEPTH_END>` 以及 128 个深度令牌。
   - 对于**结构化表示**（如边界框）：将图像缩放到336×336像素，引入336个像素位置令牌（`PIXEL_0` 到 `PIXEL_335`）。每个边界框表示为4个令牌（x1, y1, x2, y2）。

2. **训练方法——AURORA**：
   - **蒸馏损失 (式1)**：使用预先训练的专用模型（如Depth Anything、Grounding DINO）的输出分布，通过交叉熵损失引导MLM生成正确的感知令牌。
   - **重构损失 (式2)**：可选，通过轻量级解码器将感知令牌解码回特征空间（如深度图），用MSE损失监督令牌与原始特征的对应关系。
   - **课程学习 (Curriculum Learning)**：
     - 定义任务难度等级，从最简单的“生成感知令牌” → “单步推理（直接回答）” → “多步链式推理（先生成令牌再回答）”。
     - 使用温度退火（式3、式4）动态调整各难度任务的采样概率，逐步增加复杂推理数据的比例。
   - **多任务数据合成**：为每个下游任务准备三类数据：
     - 原子任务数据：仅训练生成感知令牌（如“请生成深度图”）。
     - 链式推理数据：引导模型先输出令牌，再基于令牌得出答案。
     - 直接标注数据：不要求中间步骤，直接给出答案。
   - **推理时约束解码**：在某些步骤强制模型只从感知令牌词汇中采样，保证中间表示的正确性。

## 3. 实验设计：数据集、基准、对比方法

### 任务与基准
- **3D推理（相对深度估计）**：
  - 基准：BLINK（124张图像，2个标记点）、以及作者构建的 HardBLINK（3/4/5个标记点，并加入中点高度约束以避免位置偏差）。
  - 评估：相对深度准确率。
- **2D推理（目标计数）**：
  - 基准：CVBench计数、SEED-Bench计数、BLINK计数子任务。
  - 评估：计数准确率。

### 训练数据来源
- 深度任务：ADE20k（使用Depth Anything生成伪深度图），其中20k张用于原子任务，500张用于链式推理和直接标注。
- 计数任务：LVIS（目标实例分割数据集），选择5k张图像用于原子任务，250张用于链式推理和直接标注。

### 对比方法
- 基础模型：LLaVA 1.5 13B、LLaVA OneVision 72B。
- 微调基线：仅在直接标注数据上微调的LLaVA（无感知令牌）。
- 封闭模型：GPT-4o、GPT-4 Turbo、GPT-4 Turbo + 工具（提供GT深度图或调用Grounding DINO）。
- 其他多模态模型：Unified-IO、Unified-IO 2（用于深度图生成对比）。

## 4. 资源与算力

- **文中未明确说明使用的GPU型号、数量及训练时长。** 仅提到训练VQVAE在ADE20k数据上，以及LLaVA-AURORA的微调过程使用了20k（深度）+ 5k（计数）级别大小的训练集。未提及计算资源细节（例如A100小时数等）。因此无法量化算力开销。

## 5. 实验数量与充分性

- **实验组数**：
  - 深度估计：在BLINK及3个HardBLINK变体共4个设置上对比（表1）。
  - 计数：在3个基准上对比（表2）。
  - 深度图生成质量：对比了VQVAE上界、Unified-IO系列（表3），并展示了定性结果。
  - 未包含消融实验（如课程学习的影响、不同令牌数量的影响等），但通过对比微调基线（无令牌）和不同方法（工具增强、封闭模型）体现了令牌的有效性。
- **充分性与客观性**：
  - 实验覆盖精度、难度递进（从2点到5点），且修改了BLINK的多选题形式以避免语言偏见，较公平。
  - 但缺乏对更多低维视觉任务（如分割、姿态估计）的验证，且仅测试了LLaVA 1.5 13B一种基础模型，泛化性证据稍弱。
  - 未报告训练过程的计算开销和推理速度，不利于评估效率。

## 6. 论文的主要结论与发现

1. **感知令牌显著提升3D推理**：在BLINK相对深度任务上，LLaVA-AURORA比微调基线提升+6.4%，在HardBLINK的5点配置下提升更大。
2. **感知令牌显著提升2D计数**：在BLINK计数上提升+10.8%，CVBench +11.3%，SEED-Bench +8.3%，超越所有开放源模型以及GPT-4 Turbo + 工具组合。
3. **深度图生成质量良好**：虽然未达到VQVAE上界，但优于Unified-IO系列，定性上接近真实深度图。
4. **轻量且可扩展**：仅需少量训练数据（百至千级）即可生效，且无需修改基础模型架构。

## 7. 优点

- **创新性**：首次明确将低级视觉表示作为类似链式思维的中介令牌引入MLM，提升了模型可解释性和推理准确性。
- **实用性**：避免外接工具，减少计算开销；使用课程学习有效缓解灾难性遗忘。
- **通用性**：框架不限于特定表示（支持像素级和结构化令牌），易于扩展到其他视觉特征（如姿态、分割）。
- **实验设计合理**：构建了HardBLINK变体来细化评估难度，并消除了多选题偏见。

## 8. 不足与局限

- **任务覆盖有限**：仅验证了深度和计数，未测试分割、姿态、光流等。
- **基础模型单一**：仅使用LLaVA 1.5 13B，未证明在更大或不同架构（如LLaVA-NeXT、Qwen-VL）上的可迁移性。
- **计算资源未披露**：无法评估训练成本，阻碍复现和比较。
- **缺少消融实验**：未分析课程学习、多任务数据配比、约束解码等因素的贡献。
- **性能上限**：在计数任务上仍低于GPT-4/VL高阶模型，说明感知令牌并非万能。
- **可能存在偏见**：HardBLINK中人为放置标记点可能不完全符合自然场景分布。

（完）
