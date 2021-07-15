import easycorrector.confusion_model.load_model as load_model
import easycorrector.common.common as common

model_name = "confusion_model"


def correct(text):
    confusions = load_model.get_confusion_model()
    result = []
    for err, right in confusions.items():
        idx = text.find(err)
        if idx > -1:
            for i, (e, r) in enumerate(zip(err, right)):
                if e != r:
                    result.append(common.CorrectItem(start=idx + i, end=idx + i + 1, replace=r))
    return result
