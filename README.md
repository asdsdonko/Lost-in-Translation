# Lost in Translation: Attention Mechanisms for Low-Resource NMT

This project evaluates the performance of attention mechanisms—Scaled Dot Product, Multi-head, and Cross Attention—on Neural Machine Translation for low-resource language simulation. The goal of this project was to test different types of Neural Machine Translation models to find the best-suited one for the transaltion of low-resource datasets. This was inspired by the gap in quality of translation for underrepresented languages in many NMT models.

## OpenNMT and Hugging Face Hub

Models from HuggingFace were used along with many installed programs from the open source repo, OpenNMT.

## Goals

- Test attention mechanisms on low-resource settings (simulated with small EN-DE dataset)
- Evaluate performance using BLEU and Perplexity (PLP) metrics
- Identify the best mechanism for accurate, accessible translation

![Diagram](results/imageLIT.png)

## Usage

```bash
bash scripts/tokenize.sh
python3 scripts/train.py
python3 scripts/translate.py --model models/scaled_dot_model --src data/input_easy.txt
python3 scripts/evaluate.py


