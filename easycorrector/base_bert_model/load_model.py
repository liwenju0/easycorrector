from transformers import AutoModelWithLMHead, AutoTokenizer
import torch

bert_version = "hfl/chinese-roberta-wwm-ext"
tokenizer = AutoTokenizer.from_pretrained(bert_version)
model = AutoModelWithLMHead.from_pretrained(bert_version)
