import kenlm
from pathlib import Path

language_model_path = Path(__file__).parent / "model_data/chars.klm"
char_lm = kenlm.LanguageModel(str(language_model_path))


def get_char_ngram_lm_model():
    return char_lm
