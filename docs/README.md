<div class="dpr-home-notice-card dpr-home-panel">
  <div class="dpr-home-notice-header dpr-home-panel-header">
    <h3 class="dpr-home-notice-title">公告与更新</h3>
    <a class="dpr-home-notice-tutorial" href="#/tutorial/README">使用教程 <span aria-hidden="true">›</span></a>
  </div>
  <div class="dpr-home-notice-entry">
    <time class="dpr-home-notice-date" datetime="2026-07-19">07.19</time>
    <div>
      <strong class="dpr-home-notice-entry-title">首页新增社区统计</strong>
      <span class="dpr-home-notice-entry-summary">现在可以看到今天看论文的人数和项目加入人数。</span>
    </div>
  </div>
  <div class="dpr-home-site-stats" data-dpr-site-stats hidden aria-live="polite">
    <span>今天有 <strong class="dpr-home-site-stat-value" data-dpr-daily-readers>--</strong> 人在看论文</span>
    <span class="dpr-home-site-stat-separator" aria-hidden="true">·</span>
    <span>已有 <strong class="dpr-home-site-stat-value" data-dpr-fork-count>--</strong> 人加入 Daily Paper Reader</span>
  </div>
</div>

## 每次日报
- 最新运行日期：2026-07-22
- 运行时间：2026-07-22 21:39:47 UTC
- 运行状态：成功
- 本次总论文数：13
- 精读区：3
- 速读区：10

### 今日简报（AI）
1. 今日精读聚焦CLIP在细粒度分类中的无标签区域评分与潜在空间几何，速读涵盖CLIP微调、小模型知识维度及多模态低秩微调。  
2. 最值得看：CLIP无标签判别区域评分方法（9.0分）实现细粒度分类突破，以及CLIP潜在空间的超球面语义混合模型（8.0分）揭示几何结构。  
3. 建议读者优先阅读精读论文，理解CLIP如何无需标注即可定位关键区域，再结合速读中的自标注对齐方法，可系统提升细粒度任务表现。
- 详情：[/202607/22/README](/202607/22/README)

### 精读区论文标签
1. [CLIP-Guided Label-Free Discriminative Region Scoring for Fine-Grained Classification](/202607/22/2607.13437v1-clip-guided-label-free-discriminative-region-scoring-for-fine-grained-classification)  
   标签：评分：9.0/10、query:seg-llm
   evidence：使用CLIP和SAM进行基于分割的细粒度分类
2. [The Hyperspherical Geometry of CLIP Latent Space: A Semantic Mixture Model](/202607/22/2607.13660v1-the-hyperspherical-geometry-of-clip-latent-space-a-semantic-mixture-model)  
   标签：评分：8.0/10、query:lr
   evidence：使用von Mises-Fisher混合模型建模CLIP隐空间的超球面几何；直接研究多模态大模型隐空间
3. [Debate-on-Graph: Reliable and Adaptive Reasoning of Large Language Model on Uncertain Knowledge Graph](/202607/22/2607.17266v1-debate-on-graph-reliable-and-adaptive-reasoning-of-large-language-model-on-uncertain-knowledge-graph)  
   标签：评分：8.0/10、query:seg-llm
   evidence：在不确定知识图谱上进行大语言模型推理

### 速读区论文标签
1. [Fine-grained CLIP fine-tuning with self-annotated region alignment](/202607/22/2607.13661v1-fine-grained-clip-fine-tuning-with-self-annotated-region-alignment)  
   标签：评分：7.0/10、query:seg-llm
   evidence：用于分割的细粒度区域对齐
2. [The Anatomy of a Truth Direction: Knowledge-Dependent Dimensionality, a Relational Law, and a Convergent Category Geometry in Small Language Models](/202607/22/2607.16741v1-the-anatomy-of-a-truth-direction-knowledge-dependent-dimensionality-a-relational-law-and-a-convergent-category-geometry-in-small-language-models)  
   标签：评分：7.0/10、query:lr
   evidence：小语言模型中真实方向的隐空间分析
3. [MultiLoReFT: Decoupling Shared and Modality-Specific Subspaces in Multimodal Learning via Low-Rank Representation Fine-Tuning](/202607/22/2607.16789v1-multiloreft-decoupling-shared-and-modality-specific-subspaces-in-multimodal-learning-via-low-rank-representation-fine-tuning)  
   标签：评分：7.0/10、query:lr
   evidence：多模态低秩表示解耦共享与模态特定子空间，支持多模态模型的隐空间推理
4. [Selective State-Space Adaptation and Retrieval for Language Model Reasoning](/202607/22/2607.19326v1-selective-state-space-adaptation-and-retrieval-for-language-model-reasoning)  
   标签：评分：7.0/10、query:seg-llm
   evidence：状态空间适配器增强语言模型推理
5. [SAGA: Schema-Aware Grounding for Agentic Text-to-SPARQL Generation](/202607/22/2607.14494v1-saga-schema-aware-grounding-for-agentic-text-to-sparql-generation)  
   标签：评分：6.0/10、query:seg-llm
   evidence：面向文本到SPARQL的智能体推理
6. [MGDT: MLLM-Guided Diffusion Transformer with Relation-Adaptive Mixture-of-Experts for Multimodal Knowledge Graph Completion](/202607/22/2607.15592v1-mgdt-mllm-guided-diffusion-transformer-with-relation-adaptive-mixture-of-experts-for-multimodal-knowledge-graph-completion)  
   标签：评分：6.0/10、query:lr
   evidence：多模态大模型指导的扩散与对齐
7. [How Do VLMs Fail? Vision-Operation Misalignment in Compositional VQA](/202607/22/2607.16094v1-how-do-vlms-fail-vision-operation-misalignment-in-compositional-vqa)  
   标签：评分：6.0/10、query:seg-llm
   evidence：VLM推理机制分析
8. [DAUPNet: Domain-Aware Uncertainty Modeling for Reliable Prototype Discrimination in Cross-Domain Few-Shot Semantic Segmentation](/202607/22/2607.16308v1-daupnet-domain-aware-uncertainty-modeling-for-reliable-prototype-discrimination-in-cross-domain-few-shot-semantic-segmentation)  
   标签：评分：6.0/10、query:seg-llm
   evidence：跨域少样本语义分割结合不确定性建模
9. [TimeLens2: Generalist Video Temporal Grounding with Multimodal LLMs](/202607/22/2607.17423v1-timelens2-generalist-video-temporal-grounding-with-multimodal-llms)  
   标签：评分：6.0/10、query:seg-llm
   evidence：多模态大语言模型的时间推理
10. [ConsiSpace: Learning Geometric Consistency Matters for Video Spatial Reasoning](/202607/22/2607.17599v1-consispace-learning-geometric-consistency-matters-for-video-spatial-reasoning)  
   标签：评分：6.0/10、query:lr
   evidence：在MLLM中构建几何一致性记忆作为隐式证据用于视频空间推理


<div class="dpr-home-promo-card dpr-home-panel">
  <div class="dpr-home-panel-header">
    <h3 class="dpr-home-promo-title">社区与支持</h3>
  </div>
  <p class="dpr-home-promo-copy">欢迎通过 Star、Fork、Issue 或 PR 一起完善 Daily Paper Reader。</p>
  <div class="dpr-home-promo-meta">
    <span>QQ群 <strong>583867967</strong></span>
    <span class="dpr-home-promo-separator" aria-hidden="true">·</span>
    <span>已有 <strong>1,491</strong> 人参与交流</span>
  </div>
</div>
