import nltk
from natural_language_utils import NaturalLanguageUtils


class Document:
    def __init__(self, name: str, text: str, language: str):
        self.name = name
        self.text = text.lower()
        self.language = language

    def tokenized(self) -> list[str]:
        return nltk.word_tokenize(self.text)

    def normalized(self) -> list[str]:
        return NaturalLanguageUtils().normalize_tokens_only(self.tokenized())
