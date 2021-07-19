import torch
from chinesebert import ChineseBertForMaskedLM, ChineseBertTokenizerFast, ChineseBertConfig

pretrained_tokenizer_name = "junnyu/ChineseBERT-base"
pretrained_model_name = "ShannonAI/ChineseBERT-base"

tokenizer = ChineseBertTokenizerFast.from_pretrained(pretrained_tokenizer_name)
config = ChineseBertConfig.from_pretrained(pretrained_tokenizer_name)
model = ChineseBertForMaskedLM.from_pretrained(pretrained_model_name, config=config)

