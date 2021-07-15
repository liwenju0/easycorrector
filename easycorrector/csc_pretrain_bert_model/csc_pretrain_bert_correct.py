import easycorrector.csc_pretrain_bert_model.load_model as mod
import easycorrector.common.common as common
import easycorrector.preprocess.illegal_char_filter as char_check
import torch

model_name = "csc_pretrain_bert_model"


def correct(text="今天去逛家具城，没想到还有进口香皂、家居服、花艺样样聚全"):
    inputs = mod.tokenizer([text], padding=True, truncation=True, return_tensors="pt")

    input_ids, input_tyi, input_attn_mask = inputs['input_ids'], inputs['token_type_ids'], inputs[
        'attention_mask']
    out = mod.model(input_ids, input_tyi, input_attn_mask)
    out = out.argmax(dim=-1)
    output = torch.squeeze(out)
    result = []
    input_ids = torch.squeeze(input_ids)
    for i in range(len(input_ids)):
        instr = mod.tokenizer.decode(input_ids[i])
        idx = text.find(instr)
        if input_ids[i] != output[i] \
                and char_check.isHan(str(mod.tokenizer.decode(input_ids[i]))[0]) \
                and char_check.isHan(str(mod.tokenizer.decode(output[i]))[0]):
            result.append(common.CorrectItem(idx, idx + len(instr), mod.tokenizer.decode(output[i])))

    return result


if __name__ == '__main__':
    correct()
