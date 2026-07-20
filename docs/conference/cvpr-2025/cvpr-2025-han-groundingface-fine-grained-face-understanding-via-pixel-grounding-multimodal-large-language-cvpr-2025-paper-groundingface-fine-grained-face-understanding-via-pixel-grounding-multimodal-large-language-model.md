---
title: "GroundingFace: Fine-grained Face Understanding via Pixel Grounding Multimodal Large Language Model"
title_zh: GroundingFace：通过像素级定位多模态大模型实现细粒度人脸理解
authors: "Han, Yue, Zhang, Jiangning, Zhu, Junwei, Hou, Runze, Ji, Xiaozhong, Lin, Chuming, Hu, Xiaobin, Xue, Zhucun, Liu, Yong"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Han_GroundingFace_Fine-grained_Face_Understanding_via_Pixel_Grounding_Multimodal_Large_Language_CVPR_2025_paper.pdf"
tags: ["query:seg-llm"]
score: 7.0
evidence: 通过像素级定位多模态大模型实现细粒度人脸分割与推理
tldr: 本文提出GroundingFace框架，用于细粒度人脸理解。构建了首个大规模像素级定位人脸标注数据集FacePlayGround-240K，结合多模态大模型实现人脸部件分割与推理，显著提升了现有模型在人脸区域的理解能力。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-han-groundingface-fine-grained-face-understanding-via-pixel-grounding-multimodal-large-language-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1785, \"height\": 815, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-han-groundingface-fine-grained-face-understanding-via-pixel-grounding-multimodal-large-language-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1299, \"height\": 928, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-han-groundingface-fine-grained-face-understanding-via-pixel-grounding-multimodal-large-language-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1808, \"height\": 280, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-han-groundingface-fine-grained-face-understanding-via-pixel-grounding-multimodal-large-language-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1815, \"height\": 958, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-han-groundingface-fine-grained-face-understanding-via-pixel-grounding-multimodal-large-language-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 504, \"height\": 268, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-han-groundingface-fine-grained-face-understanding-via-pixel-grounding-multimodal-large-language-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1698, \"height\": 563, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-han-groundingface-fine-grained-face-understanding-via-pixel-grounding-multimodal-large-language-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 845, \"height\": 321, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-han-groundingface-fine-grained-face-understanding-via-pixel-grounding-multimodal-large-language-cvpr-2025-paper/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1704, \"height\": 416, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-han-groundingface-fine-grained-face-understanding-via-pixel-grounding-multimodal-large-language-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1803, \"height\": 378, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-han-groundingface-fine-grained-face-understanding-via-pixel-grounding-multimodal-large-language-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 864, \"height\": 304, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-han-groundingface-fine-grained-face-understanding-via-pixel-grounding-multimodal-large-language-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 862, \"height\": 175, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-han-groundingface-fine-grained-face-understanding-via-pixel-grounding-multimodal-large-language-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 860, \"height\": 250, \"label\": \"Table\"}]"
motivation: 现有像素级定位模型在细粒度人脸理解上表现不足。
method: 提出GroundingFace框架，通过像素级定位多模态大模型增强人脸部件分割。
result: 在人脸分割和问答任务上达到最优性能。
conclusion: 该工作为人脸理解提供了高质量数据集和有效框架。
---

## Abstract
Multimodal Language Learning Models (MLLMs) have shown remarkable performance in image understanding, generation, and editing, with recent advancements achieving pixel-level grounding with reasoning. However, these models for common objects struggle with fine-grained face understanding. In this work, we introduce the FacePlayGround-240K dataset, the first pioneering large-scale, pixel-grounded face caption and question-answer (QA) dataset, meticulously curated for alignment pretraining and instruction-tuning. We present the GroundingFace framework, specifically designed to enhance fine-grained face understanding. This framework significantly augments the capabilities of existing grounding models in face part segmentation, face attribute comprehension, while preserving general scene understanding. Comprehensive experiments validate that our approach surpasses current state-of-the-art models in pixel-grounded face captioning/QA and various downstream tasks, including face captioning, referring segmentation, and zero-shot face attribute recognition.

---

## 论文详细总结（自动生成）

# GroundingFace 论文详细总结

## 1. 核心问题与整体含义（研究动机与背景）

### 研究动机
- 现有像素级定位的多模态大语言模型（如GLaMM、LISA等）在通用场景中表现优异，但在**细粒度人脸理解**上严重不足：这些模型“cannot determine”（无法确定）人脸相关的属性，在回答人脸QA问题时效果差。
- 现有数据集（如CelebA、FFHQ-Text等）存在以下缺陷：
  - 属性不充分：描述简短、缺乏语义层次；
  - 缺乏属性间关系：模板生成的描述割裂了属性关联；
  - 缺少人脸QA数据：社区严重缺乏带推理能力的人脸QA对；
  - 区域掩码不足：当前人脸解析仅有19个类别，无法支持像素级定位所需的区域-文本对齐。

### 整体含义
作者旨在构建**首个大规模、像素级定位的人脸描述与问答数据集**（FacePlayGround-240K）及配套的**GroundingFace框架**，实现细粒度人脸部件分割、人脸属性理解，同时保持通用场景理解能力，从而填补现有MLLM在人脸领域的空白。

## 2. 方法论：核心思想、关键技术细节

### 核心思想
基于GLaMM框架进行改进，针对人脸理解对高分辨率、细粒度分割、多粒度属性理解的需求，引入三大模块：

#### (1) 细粒度人脸部件分割（Fine-grained Face Part Segmentation）
- **HQ-SAM Adapter**：将SAM的浅层特征（富含像素级细节）与深层特征融合，通过Shallow-Deep Fusion模块（反卷积+线性层）增强小部件分割精度。
- 可视化显示浅层特征更能捕捉细微结构（如皱纹、痣），而深层特征偏向高层语义，融合两者可提升小部件分割效果。

#### (2) 细粒度人脸属性理解（Fine-grained Face Attribute Understanding）
- **Face Prior Sampler**：利用人脸五点检测先验，通过仿射变换将SAM特征（64×64）中的人脸区域裁剪并对齐至48×48，再使用像素重排（Pixel Unshuffle）和可学习线性层压缩特征，在保留高分辨率细节的同时减少token数量，降低LLM计算负担。
- 引入额外的Projector将这些人脸token与全局视觉特征对齐。

#### (3) 训练策略与MoE（Training Recipe + Mixture of Experts）
- **两阶段训练**：
  - Stage-1：在通用数据+人脸数据上微调，冻结预训练LoRA1，训练LoRA2、Projector1和掩码解码器，用于整合人脸概念。
  - Stage-2：冻结Stage-1所有可训练参数，仅训练LoRA3、Projector2和HQ Adapter，在高质量手工标注子集和细粒度部件掩码子集上微调，学习高精度分割。
- **LoRA MoE（Mixture of Experts）**：使用Top-1路由器将HQ（高质量）token和LQ（低质量）token路由到对应两阶段的LoRA专家，确保模型在接收高质量数据时使用精细的LoRA3，在接收粗粒度数据时使用粗的LoRA2，避免了粗掩码对细粒度学习的影响。同时引入负载均衡损失。

### 数据构建流程（FacePlayGround-240K数据集）
- **数据来源**：CelebAMask-HQ（30K）、FFHQ（70K）、EasyPortrait（40K）、LAION-Face（98K）等，总计240K张靠近拍摄的单人高分辨率人脸图像。
- **综合人脸描述生成**：借助Face++ API获取定量属性（年龄、性别、情绪强度、皮肤分析等），用InternVL生成七个方面的初始描述，再用LLM去重改写，形成包含短描述、详细描述、整体描述三个语义层次的描述。
- **细粒度部件掩码标注**：通过词频分析得到47个新概念，分为6个超类：
  - 结构区域/线：利用MediaPipe 478点面部地标分解；
  - 皮肤分析：商业皮肤分析API获取斑点、皱纹等；
  - 头发分析：利用GroundingDINO+SAM；
  - 手工标注化妆品与面部装饰：10位标注员对3,745张图像标注眼线、眼影等清晰边界的装饰。
- **文本-掩码对齐**：用SpaCy提取名词短语，与类别同义词表匹配，相似度阈值过滤。
- **定位分层语义QA**：使用LLM从定位描述生成三级QA对：具体属性级、抽象特征级、整体印象级。单目标掩码的QA用于指代分割，多目标掩码的QA用于定位QA。

## 3. 实验设计

### 数据集与基准
- **数据集**：FacePlayGround-240K划分为训练集232.5K、验证集2.5K、测试集5K。
- **评估指标**：
  - 描述质量：METEOR
  - 掩码质量：类无关掩码AP（定位任务）、gIoU（指代分割）
  - 文本-掩码对应准确度：AP50、mIoU（定位描述/QA）
- **基线模型**：主要对比**GLaMM**（目前最相关的像素级定位MLLM），以及Qwen-VL、InstructBLIP、LLaVA-v1.5、InternVL-v1.5用于零样本属性识别。

### 任务与对比方法
1. **像素级定位人脸描述（Pixel Grounded Face Caption）**：对比GLaMM、Stage-1、Ours（GroundingFace）。
2. **人脸指代分割（Face Referring Segmentation）**：类似对比。
3. **人脸定位描述与QA（Face-oriented Grounded Caption and QA）**：对比GLaMM、Stage-1、Ours。
4. **零样本人脸属性识别（Zero-shot Face Attribute Recognition）**：对比Qwen-VL、InstructBLIP、LLaVA-v1.5、InternVL-v1.5，在RAF-DB、LFWA、AgeDB三个数据集上评估情绪、属性、性别、年龄准确率。

### 消融实验
- 在表2中对HQ-SAM Adapter、HQ Facial Tokens（Face Prior Sampler）、MoE三个关键组件进行消融，验证每个组件的贡献。
- 比较不同深度的SAM特征（6th+24th vs 6th+12th+18th+24th）。
- 对比单阶段（Stage-1）与两阶段训练策略。

## 4. 资源与算力

论文中未明确说明训练所使用的GPU型号、数量、训练时长等具体算力信息。仅在数据集构建中提到使用了商业API（Face++）和开源模型（InternVL、LLM）进行标注，但未报告计算资源消耗。在模型训练部分，仅提及“fine-tune”和“two-stage training”，未给出硬件细节。

## 5. 实验数量与充分性

- **实验组数**：包含4个主要benchmark的实验，每组均有量化结果（表2、3、4）。消融实验在表2中做了6组（Idx.1-8，含不同特征深度对比），较为全面。
- **充分性**：实验覆盖了主要的定位任务（描述、QA、指代分割）和零样本属性识别，对比了当前多个通用MLLM，且消融实验验证了每个组件的有效性。但缺少对FacePlayGround-240K数据集本身与现有数据集（如仅为CelebA-HQ）的直接训练对比（如仅使用19类掩码的模型性能），且未与专门的人脸解析模型（如FaceParsing）进行分割性能对比。总体而言，实验设计客观、公平（使用相同训练/测试集、相同评估指标），但零样本属性识别中Ours模型参数量为7B，而InternVL-v1.5为26B，在参数量不等的条件下对比，可能存在不公平。

## 6. 主要结论与发现

- GroundingFace在像素级定位人脸描述/QA任务上显著超越GLaMM（METEOR从1.1提升至23.1，gIoU从6.6提升至88.9）。
- 在零样本人脸属性识别中，GroundingFace在RAF-DB（情绪91.7%）、LFWA（属性73.1%）、AgeDB（性别98.5%）上均达到最优，年龄MAE为6.92优于其他模型。
- 消融实验证明：HQ-SAM Adapter、HQ Facial Tokens、MoE每个组件均有效，两阶段训练优于单阶段，使用4层SAM特征（6/12/18/24）并未提升性能。
- 两阶段训练策略有效结合了自动生成掩码与手工高质量掩码，MoE路由器能区分粗/细粒度token，防止知识遗忘。

## 7. 优点

1. **数据集创新**：FacePlayGround-240K是首个大规模、像素级定位的人脸描述与QA数据集，包含47个掩码类别、5.4M掩码、7.3M定位区域，覆盖皮肤细节、装饰等细粒度概念，且具有分层语义结构。
2. **框架设计精巧**：Face Prior Sampler利用人脸先验高效提取高分辨率特征，避免全图高分辨率处理的巨大计算开销；LoRA MoE解决了粗/细粒度数据混合训练时的矛盾，保持通用场景能力。
3. **综合能力强**：不仅能做细粒度人脸理解，还能在零样本属性识别上超越通用MLLM，且保留了对常见物体的分割能力（通过LoRA MoE）。
4. **实验覆盖全面**：从像素级定位到零样本属性识别，多个典型人脸理解任务均有评估。

## 8. 不足与局限

1. **计算资源未报告**：缺乏训练硬件、时长等信息，可复现性存疑。
2. **对比基线选择有限**：未与专门的人脸解析模型（如FaceParsing网络）或传统人脸属性识别方法（如直接使用CNN分类器）对比，主要对比对象仅为通用MLLM。
3. **零样本评估存在参数量不平等**：Ours仅7B，但InternVL-v1.5为26B，在年龄任务上Ours的MAE更高（6.92 vs 19.26？实际是Ours更好），但其他任务上Ours更优，但参数量差异可能影响公平性。
4. **数据偏差风险**：数据集来源主要为高清、正向、单人图像，对于遮挡严重、多面、低分辨率、非正面场景的泛化能力未进行充分测试。
5. **应用限制**：依赖多个外部API（Face++、MediaPipe）和开源模型（InternVL、SAM），整个流程部署成本较高；同时手工标注仅3,745张，可能对化妆品等细分类别的覆盖不全。
6. **缺乏对通用场景遗忘的定量分析**：虽有MoE保留通用能力，但未定量测试在COCO等通用数据集上的分割/定位性能是否下降。

（完）
