import easycorrector.base_bert_model.load_model as mod
import torch
import easycorrector.common.common as common


model_name = "base_bert"

def correct(text="我很好", accept_first_topk=10):
    result = []

    for i in range(len(text)):
        inputs = text[:i] + mod.tokenizer.mask_token + text[i + 1:]
        inputs = mod.tokenizer(inputs, padding=True, return_tensors="pt")
        mask_token_index = torch.where(inputs['input_ids'] == mod.tokenizer.mask_token_id)[1]
        token_logits = mod.model(**inputs).logits
        token_logits = token_logits.view(-1, token_logits.size()[-1])
        mask_token_logits = token_logits[mask_token_index, :]
        top_tokens = torch.topk(mask_token_logits, accept_first_topk, dim=1).indices[0].tolist()
        top_tokens = [mod.tokenizer.decode(token) if mod.tokenizer.decode(token) != "[UNK]" else " " for token in top_tokens]

        if text[i] not in top_tokens:
            replace_char = top_tokens[0]
            result.append(common.CorrectItem(i, i + 1, replace_char))
            text = text[:i] + replace_char + text[i + 1:]

    return result

if __name__ == '__main__':
    correct()