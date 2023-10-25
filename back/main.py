from document import Document
from alphabet_method import AlphabetMethod
from frequency_words_method import FrequencyWordsMethod


def recognize_lang(document: Document, method: int) -> str:
    if method == 1:
        RECOGNIZER = AlphabetMethod()
        return RECOGNIZER.find_language(RECOGNIZER.get_local_symbol_frequency(document))

    elif method == 2:
        RECOGNIZER = FrequencyWordsMethod()
        return RECOGNIZER.find_language(RECOGNIZER.get_local_word_frequency(document))
    else:
        # return neural(text)
        return 'rus'


def get_all_training_documents() -> list[Document]:
    return []
