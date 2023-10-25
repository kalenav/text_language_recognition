from document import Document
from alphabet_method import AlphabetMethod
from frequency_words_method import FrequencyWordsMethod
from neural_network_method import NeuralNetworkMethod
import utils
from path import LOCAL_PATH


def recognize_lang(document: Document, method: int) -> str:
    if method == 1:
        RECOGNIZER = AlphabetMethod()
        return RECOGNIZER.find_language(RECOGNIZER.get_local_symbol_frequency(document))

    elif method == 2:
        RECOGNIZER = FrequencyWordsMethod()
        return RECOGNIZER.find_language(RECOGNIZER.get_local_word_frequency(document))
    else:
        RECOGNIZER = NeuralNetworkMethod()
        return RECOGNIZER.predict_language(document)


def get_all_training_documents() -> list[Document]:
    return utils.get_all_documents_in_folder(LOCAL_PATH + "\\documents\\training_documents")
