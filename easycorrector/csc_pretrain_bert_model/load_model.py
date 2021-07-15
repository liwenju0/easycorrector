import pickle
import torch
from pathlib import Path
from transformers import BertTokenizer, BertModel, BertConfig
import torch.nn as nn

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
language_model_path = Path(__file__).parent / "model_data/model.pkl"


class BertFineTune(nn.Module):
    def __init__(self, bert, device):
        super(BertFineTune, self).__init__()
        self.device = device
        self.config = bert.config
        embedding_size = self.config.to_dict()['hidden_size']
        self.bert = bert.to(device)
        self.sigmoid = nn.Sigmoid().to(device)

        bert_embedding = bert.embeddings
        word_embeddings_weight = bert.embeddings.word_embeddings.weight
        embeddings = nn.Parameter(word_embeddings_weight, True)
        bert_embedding.word_embeddings = nn.Embedding(self.config.vocab_size, embedding_size, _weight=embeddings)
        self.linear = nn.Linear(embedding_size, self.config.vocab_size)
        self.linear.weight = embeddings

        self.softmax = nn.LogSoftmax(dim=-1)

    def forward(self, input_ids, input_tyi, input_attn_mask):
        h = self.bert(input_ids=input_ids, token_type_ids=input_tyi, attention_mask=input_attn_mask)
        out = self.softmax(self.linear(h.last_hidden_state))
        return out


tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
bert = BertModel.from_pretrained('bert-base-chinese', return_dict=True)
model = BertFineTune(bert, device)
state_dict = torch.load(open(str(language_model_path), 'rb'), map_location=torch.device('cpu'))
model.load_state_dict(state_dict, strict=False)
