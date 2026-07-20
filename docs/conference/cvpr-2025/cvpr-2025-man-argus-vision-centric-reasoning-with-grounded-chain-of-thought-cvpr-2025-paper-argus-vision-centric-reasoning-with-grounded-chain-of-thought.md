---
title: "Argus: Vision-Centric Reasoning with Grounded Chain-of-Thought"
title_zh: Argus：基于视觉中心推理与接地思维链
authors: "Man, Yunze, Huang, De-An, Liu, Guilin, Sheng, Shiwei, Liu, Shilong, Gui, Liang-Yan, Kautz, Jan, Wang, Yu-Xiong, Yu, Zhiding"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Man_Argus_Vision-Centric_Reasoning_with_Grounded_Chain-of-Thought_CVPR_2025_paper.pdf"
tags: ["query:lr"]
score: 4.0
evidence: 在MLLM中结合视觉接地思维链进行视觉中心推理，与隐空间推理相关
tldr: 本文提出Argus方法，通过目标级接地作为视觉思维链信号，增强多模态大模型的视觉注意力聚焦，在多种多模态推理基准上取得优异效果，尤其适用需要精确视觉关注的场景。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-man-argus-vision-centric-reasoning-with-grounded-chain-of-thought-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1766, \"height\": 654, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-man-argus-vision-centric-reasoning-with-grounded-chain-of-thought-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 862, \"height\": 844, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-man-argus-vision-centric-reasoning-with-grounded-chain-of-thought-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1800, \"height\": 660, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-man-argus-vision-centric-reasoning-with-grounded-chain-of-thought-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 868, \"height\": 610, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-man-argus-vision-centric-reasoning-with-grounded-chain-of-thought-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 536, \"height\": 438, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-man-argus-vision-centric-reasoning-with-grounded-chain-of-thought-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 580, \"height\": 439, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-man-argus-vision-centric-reasoning-with-grounded-chain-of-thought-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 551, \"height\": 437, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-man-argus-vision-centric-reasoning-with-grounded-chain-of-thought-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1808, \"height\": 772, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-man-argus-vision-centric-reasoning-with-grounded-chain-of-thought-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 867, \"height\": 647, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-man-argus-vision-centric-reasoning-with-grounded-chain-of-thought-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 854, \"height\": 235, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-man-argus-vision-centric-reasoning-with-grounded-chain-of-thought-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 855, \"height\": 335, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-man-argus-vision-centric-reasoning-with-grounded-chain-of-thought-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 850, \"height\": 185, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-man-argus-vision-centric-reasoning-with-grounded-chain-of-thought-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 838, \"height\": 176, \"label\": \"Table\"}]"
motivation: MLLMs在视觉中心场景中推理能力不足，缺乏精准视觉关注。
method: 提出目标级接地机制作为视觉思维链，引导视觉注意力。
result: 在多模态推理和定位任务上显著提升。
conclusion: 为MLLMs视觉推理提供了有效增强方法。
---

## Abstract
Recent advances in multimodal large language models (MLLMs) have demonstrated remarkable capabilities in vision-language tasks, yet they often struggle with vision-centric scenarios where precise visual focus is needed for accurate reasoning. In this paper, we introduce Argus to address these limitations with a new visual attention grounding mechanism. Our approach employs object-centric grounding as visual chain-of-thought signals, enabling more effective goal-conditioned visual attention during multimodal reasoning tasks. Evaluations on diverse benchmarks demonstrate that Argus excels in both multimodal reasoning tasks and referring object grounding tasks. Extensive analysis further validates various design choices of Argus, and reveals the effectiveness of explicit language-guided visual region-of-interest engagement in MLLMs, highlighting the importance of advancing multimodal intelligence from a visual-centric perspective.

---

## 论文详细总结（自动生成）

# 论文详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：当前多模态大语言模型（MLLMs）在视觉-语言任务上表现优异，但在视觉中心场景（如精确的空间关系、特定区域属性）中往往因缺乏精准的视觉关注而推理能力不足。现有MLLMs主要依赖隐式的自注意力机制进行语言引导的视觉关注，缺少显式的、目标驱动的视觉注意力机制。
- **整体含义**：论文提出Argus，通过目标级接地（object-centric grounding）作为视觉思维链信号，显式引导模型聚焦于与问题相关的视觉区域，从而提升视觉推理和定位能力。该工作强调了从“视觉中心”视角推进多模态智能的重要性。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：借鉴认知科学中“刺激驱动注意”与“目标驱动注意”的两种视觉注意力机制，Argus在标准MLLM架构中引入显式的、语言引导的视觉区域兴趣（RoI）搜索与上下文重新参与模块。具体通过预测文本-对象边界框，将框作为视觉CoT信号，然后对RoI进行再编码或重采样，以增强模型对关键视觉区域的关注。
- **关键技术细节**：
  - **视觉编码器**：使用混合视觉专家（MoVE）策略，包含CLIP、ConvNeXt、EVA-02三个视觉编码器。
  - **RoI采样**：模型输出归一化的文本框坐标（[xmin, ymin, xmax, ymax]），用于从原始图像中裁剪相关区域。
  - **显式RoI再参与策略**：论文对比了四种策略：
    1. **隐式自注意力**：仅依靠LLM内部自注意力，无显式引导。
    2. **隐式框引导**：输出框坐标作为文本CoT，但不进行显式视觉再编码。
    3. **显式RoI再编码**：将裁剪的RoI重新输入视觉编码器生成新token，再拼接回序列。
    4. **显式RoI重采样**：从预先缓存的MoVE视觉token中取出与RoI重叠的patch token作为上下文，减少计算量。
  - **训练流程**：两阶段训练：
    - 预训练阶段（LLaVA-595K图像-文本对）：冻结LLM，训练视觉编码器和MLP投影器，并进行视觉专家预对齐。
    - 监督微调阶段：使用Eagle1.8M数据集（通用对话）、VCoT数据集（RoI框标注用于视觉CoT）、GRIT和Shikra数据集（额外接地训练）。全参数更新。
  - **模型架构**：LLM解码器为Llama3-8B，输入分辨率1024×1024（ConvNeXt/EVA-02）和448×448（CLIP），视觉token数1024。

## 3. 实验设计：数据集、基准、对比方法

- **数据集与基准**：
  - **视觉推理**：涵盖通用多模态推理（MMMU, MMB, SEED, GQA）、文本理解（ChartQA, OCRBench, TextVQA, DocVQA）、视觉中心感知（CV-Bench 2D/3D, MMVP, RealworldQA, V-Star）等14个基准。
  - **接地定位**：RefCOCO, RefCOCO+, RefCOCOg（Acc@0.5）。
- **对比方法**：
  - 开源7B/8B规模MLLMs：Mini-Gemini-HD-8B, LLaVA-NeXT-8B, InternVL, QwenVL-7B, Eagle-X3-8B, Visual-CoT-7B等。
  - 专有模型（参考）：GPT-4o, Qwen2.5-VL, InternVL2.5。
  - 接地任务对比：MAttNet, TransVG, UNITER, VILLA, MDETR, G-DINO, Shikra, Ferret, MiniGPT-v2等。
- **实验设计**：在同一参数规模、训练数据量和架构下进行公平比较，使用官方或前人工作中一致的评估协议。

## 4. 资源与算力

- **文中说明**：实验使用NVIDIA A100 GPU进行训练，但未明确给出具体数量、总训练时长、GPU-小时等细节。仅提及两阶段训练各1个epoch，batch size 256，学习率等超参数。未提供总算力消耗。

## 5. 实验数量与充分性

- **实验数量**：
  - 主表（Table 1）在14个多模态推理基准上报告性能。
  - 接地任务（Table 2）在3个数据集6个分割上对比。
  - 消融实验（Table 3-6）覆盖：四种注意力再参与机制、编码器能力、padding策略、非共享MLP、CoT与接地贡献、计算效率。
  - 补充材料中还有更多分析。
- **充分性与公平性**：实验设计较为充分，消融实验控制了变量（如训练数据、模型规模、视觉编码器），但存在一些公平性问题：对比方法采用公开报告结果，可能来自不同训练数据量和策略；文中也承认“完美公平定量比较困难”，但通过统一消融设置尽量保证内部实验的公平。总体而言，实验覆盖了多种任务类型和机制变体，结论可靠。

## 6. 论文的主要结论与发现

- 显式的目标驱动视觉注意力再参与机制显著优于隐式自注意力或仅文本CoT。
- 显式RoI重采样策略在大多数任务上优于再编码策略，但再编码在关注小物体（V-Star）时更优。
- 视觉CoT信号和接地训练共同提升性能：CoT信号本身带来明显提升，进一步加入接地数据集使模型更准确地预测框并最大化CoT效能。
- 更高容量的视觉编码器带来更好性能；重采样对初始编码质量依赖更强。
- 重采样在计算效率上优于再编码（GMACs更少、推理时间更短）。

## 7. 优点：方法或实验设计上的亮点

- **方法创新**：将认知科学中的两种注意力机制引入MLLM设计，系统对比了隐式和显式视觉注意力引导方式，并提出了基于对象接地作为视觉CoT信号的新范式。
- **架构简洁有效**：通过文本坐标表示框，无需额外检测头，兼容现有MLLM。
- **实验全面**：覆盖多种任务（推理、接地、文本理解），消融细致（四种策略、编码器变体、padding、MLP共享等），分析了计算效率。
- **开源与可复现**：基于公开数据集和模型（Eagle、Llama3-8B），训练数据公开。

## 8. 不足与局限

- **算力信息不透明**：未详细报告GPU数量、训练总时长，不利于复现和实际成本评估。
- **对比公平性局限**：主实验对比的方法来自不同代码基和训练细节，可能存在数据泄露或训练规模差异；消融实验内部公平，但与外部方法相比可能不够严格。
- **应用限制**：仅针对单一图像输入，未探索视频或多图场景；RoI采样依赖于模型自身预测的边界框，若框预测不准则后续推理可能失效。
- **数据集依赖**：训练使用了VCoT等接地标注数据，在缺乏此类标注的场景下表现未知。
- **偏差风险**：主要涉及英文和常见视觉对象，对低资源语言或领域可能泛化不足。

（完）
