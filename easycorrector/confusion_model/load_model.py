from pathlib import Path

confusions = {}
for line in open(str(Path(__file__).parent / "model_data/confusion.txt")):
    try:
        s = line.strip().split()
        confusions[s[0].strip()] = s[1].strip()
    except:
        continue


def get_confusion_model():
    return confusions
