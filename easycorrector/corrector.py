import easycorrector.confusion_model.confusion_correct as confusion_correct
import easycorrector.ngram_model.ngram_correct as ngram_correct
import easycorrector.preprocess.preprocess as preprocess
import easycorrector.base_bert_model.base_bert_correct as base_bert_correct
import easycorrector.csc_pretrain_bert_model.csc_pretrain_bert_correct as csc_pretrain_bert_correct
import easycorrector.preprocess.cut_sentences as cut_sen
from collections import defaultdict

models = [confusion_correct,
         # ngram_correct,
         # base_bert_correct,
    csc_pretrain_bert_correct]


def correct(text):
    if isinstance(text, list):
        sentences = [preprocess.preprocess(sen) for sen in text]
    else:
        text = preprocess.preprocess(text)
        sentences = cut_sen.cut_sentence(text)
    correct_sentences = []
    for sen in sentences:
        conf_res = confusion_correct.correct(sen)
        csc_pre_res = csc_pretrain_bert_correct.correct(sen)
        ngram_res = ngram_correct.correct(sen)
        res = defaultdict(list)
        for item in conf_res + ngram_res + csc_pre_res :
            res[item.start].append(item)


        cor_sen = ""
        for i in range(len(sen)):
            if i in res:
                cor_sen += res[i][0].replace
            else:
                cor_sen += sen[i]
        print(sen, cor_sen)
        correct_sentences.append(cor_sen)
    return correct_sentences



if __name__ == '__main__':

    # correct('''
    # 1.前不久，D市一男子武某醉驾被查却免于起诉，这引起了社会的广泛关注。该名男子为何酒驾免罚？难道是打法律的“擦边球”？还是执法者滥用职权无视法律？
    #    据悉，武某酒后驾车被执勤交警当场查获，经鉴定达到醉驾标准。武某酒后驾车的行为已涉嫌危险驾驶罪，但为抢救其幼女生命情形紧迫所为，主观恶性较小，属犯罪情节轻微。通过多方查证，证实了武某案发当日酒后驾车事件的紧迫性，经研究，依法对武某作出了相对不起诉的决定。
    #    武某酒驾确实违法了，执法部门也秉公执法了，而相对不起诉则体现了执法新理念，让更多的人体会到法律的温度。其实，法律的最高境界不是无情，而是情与法相对完美的结合，从西周“明德慎罚”到现在的“以人为本”，乃至“未成年人不公开审理”，法律体现了人文关怀和对人格尊严的维护。
    #    近日，该市交警大队执勤民警在城区巡逻过程中，发现西苑路一辆外地货运车临街停车卸货，车用篷布随意堆放，占据了由北向南行驶车道二分之一的路面，导致该车道车辆只能占用对向车道行驶，道路拥挤，存在安全隐患。
    #    经了解，该驾驶员常年从事长途货运，这是第一次来到D市，加之正值“五一”假期，以为没有交警执勤，就在路边停车开始卸货。
    #    交警发现后，第一时间协助清除路面隐患，随后对驾驶员以善意提醒的方式进行教育，详细解释了占用机动车道路的危害和要承担的法律责任，叮嘱驾驶员一定要遵守交通规则，不能方便了自己,却影响了他人的出行安全。
    #    “平常违章了就交罚款，以为今天交警要处罚我，看到公安交警耐心的向我讲道理，并且还告诉我什么该做什么不该做，让我真正了解了交规交法，这样的教育比直接处罚有用多了”，驾驶员感慨地说道。
    #    “景区停车位已满，路两侧有临时停车区域，请有序停放。”5月4日上午十时许，D市国家森林公园景区停车场已经饱和，但前来游览的车辆依旧络绎不绝。
    #    为满足外地游客“五一”假期停车需求，D市公安交警在不影响交通安全的前提下，指挥车辆靠路边临时停车，全力满足景区车辆合理停放需求。清脆响亮的哨声伴着执勤交警挥动的手臂，一辆辆车有序停放、秩序井然。
    #    “去年听同事说假期森林公园车堵得上不了山，今年带着家人来旅游，没想到能直接开到景区门口，停车场没位置了，给我们安排停在路边，真是太方便了，为D市交警的服务点赞。”王先生高兴的说。
    #    车被套牌，不同车型相同车牌，遇到这种情况怎么办？D市给出答案。近日，D市交警部门在微信公众号开通了套牌车报案功能，机动车所有人可以通过D市交警微信公众号进行套牌车自助报案。“‘假套牌’报案微信自助办理渠道的开通，实现了群众在家即可通过网上进行报案，减少群众往来报案的人力、物力，缩短了假套牌违法从报案到查处的时间。”D市交警相关负责人介绍，市民只需通过微信公众号，关注“D市交警”，进入“违法事故”—“套牌车报案”，然后根据报案提示，“选择车辆”-“选择违法”-“填写报案证据”-“上传报案人资料”-“上传车辆资料”，即可实现“假套牌”报案。
    #    “你们交警同志这么耐心的给我们讲道理，下次我再也不违规拉人了，他们也都再也不坐农用车了……”
    #    5月6日，交警大队在进行路检路查过程中，发现一辆农用车违法载人。
    # ''')

    sentences = []
    for txt in open("test_data.txt"):
        sentences.append(txt)

    correct(sentences)
    #     print(txt)
    #     for model in models:
    #         for item in model.correct(txt):
    #             print(model.model_name + ":" + txt[item.start:item.end], "----", item.replace if item.replace else "建议检查")
