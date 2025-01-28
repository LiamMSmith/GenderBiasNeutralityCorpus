# Identifying and Neutralizing Gender Bias from Text

## Overview
This repository contains the code and dataset for our project, **Identifying and Neutralizing Gender Bias from Text**, conducted as part of the Stanford CS224N course. Our project addresses gender bias in text, particularly in social media posts, by developing a **parallel Gender Bias Neutrality Corpus (GBNC)** and fine-tuning **GPT-3.5 and LLaMA-2** models to neutralize biased language.

## Motivation
Gender bias in text perpetuates harmful stereotypes, often unintentionally reinforcing systemic inequalities. Prior research has explored bias **detection** and **debiasing embeddings**, but **gender bias neutralization**—editing biased text to produce unbiased yet semantically consistent alternatives—remains an underexplored area.

Our work aims to bridge this gap by:
1. **Creating a high-quality parallel corpus (GBNC)** of biased and neutralized sentences.
2. **Fine-tuning large language models (LLMs)** for automatic gender bias correction.
3. **Evaluating performance using quantitative metrics (BLEU, BERTScore) and qualitative analysis**.

## Dataset: Gender Bias Neutrality Corpus (GBNC)
We constructed a dataset of **1,049 labeled and corrected social media posts** sourced from:
- **Broad Twitter Corpus**
- **EXIST database** (English subset)

Each biased sentence was manually labeled and corrected to remove bias while preserving meaning. Our dataset includes six **types of gender bias**:
1. **Gendered Nouns** – e.g., "chairman" → "chairperson"
2. **Male-Defaulted Pronouns** – e.g., "A leader inspires *his* team" → "A leader inspires *their* team"
3. **Ideological Bias** – e.g., "Only women receive support in domestic violence cases" → "Both partners can receive support..."
4. **Stereotyping** – e.g., "Only a woman can nurture children properly" → "Anyone can nurture children properly"
5. **Misogyny** – Direct hostility towards women
6. **Sexual Violence** – Explicit content (some posts were removed entirely)

## Model Fine-Tuning
We fine-tuned two state-of-the-art models:

### **1. GPT-3.5 Fine-Tuning**
- Used **GPT-3.5-turbo-0125** via OpenAI’s fine-tuning API.
- Preprocessed data into **JSONL format** with system instructions.
- Hyperparameters:
  - **Temperature** = 1.0
  - **Max length** = 280 characters (social media post constraint)
  - **No repetition penalties** (to preserve unbiased text)

### **2. LLaMA-2 Fine-Tuning (LoRA)**
- Used **LLaMA-2-7B** from Hugging Face.
- Applied **Low-Rank Adaptation (LoRA)** for efficient fine-tuning with limited GPU resources.
- Fine-tuned using **PyTorch & Hugging Face Transformers**.
- **Quantized** model for reduced memory usage.

## Results & Performance
### **Quantitative Metrics**
| Model | BLEU Score (↑) | BERTScore Precision (↑) | BERTScore Recall (↑) | BERTScore F1 (↑) |
|--------|-------------|----------------|---------------|------------|
| **GPT-3.5 Base** | 0.489 | 0.932 | 0.935 | 0.934 |
| **GPT-3.5 Fine-tuned** | **0.811** | **0.974** | **0.969** | **0.971** |
| **LLaMA-2 Base** | 0.340 | 0.670 | 0.688 | 0.678 |
| **LLaMA-2 Fine-tuned** | **0.627** | **0.967** | **0.930** | **0.947** |

**Key Findings:**
- Both models **significantly improved** after fine-tuning, especially in **BLEU scores** (indicating better alignment with human-edited text).
- **LLaMA-2 showed the most improvement in semantic similarity (BERTScore).**
- The models struggled with **highly explicit or slang-heavy inputs**, sometimes refusing to process highly biased text.

## Limitations & Future Work
- **Data annotation bias**: Since the dataset was manually labeled, some **implicit biases** may persist.
- **Handling extreme bias**: Current LLM policies prevent responses to highly toxic inputs.
- **Expanding the dataset**: More data across **different languages and social contexts** would improve robustness.
- **Exploring reinforcement learning**: RLHF (Reinforcement Learning with Human Feedback) could further refine responses.

## Contributors ✨
This project was developed by equal contribution from **Maya Bedge**, **Dante Danelian**, and **Liam Smith** 

## Citation 📖
If you use our dataset in your work, please cite us:

```
@misc{gbnc2024, 
  title={Gender Bias Neutrality Corpus (GBNC)}, 
  author={Bedge, Maya and Danelian, Dante and Smith, Liam}, 
  year={2024}, 
  howpublished={GitHub}, 
  url={https://github.com/LiamMSmith/GenderBiasNeutralityCorpus.git} }
```
