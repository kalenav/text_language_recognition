from document import Document
from alphabet_method import AlphabetMethod
from frequency_words_method import FrequencyWordsMethod
from neural_network_method import NeuralNetworkMethod
import utils
from path import LOCAL_PATH


class RecognizerFactory:
    _recognizers = {}

    @staticmethod
    def get_recognizer(method_type):
        if method_type not in RecognizerFactory._recognizers:
            if method_type == 'neural_network':
                RecognizerFactory._recognizers[method_type] = NeuralNetworkMethod()
            elif method_type == 'frequency_words':
                RecognizerFactory._recognizers[method_type] = FrequencyWordsMethod()
            elif method_type == 'alphabet':
                RecognizerFactory._recognizers[method_type] = AlphabetMethod()
            else:
                raise ValueError("Unsupported method type")

        return RecognizerFactory._recognizers[method_type]


def recognize_lang(document: Document, method: int) -> str:
    if method == 1:
        RECOGNIZER = RecognizerFactory.get_recognizer(method_type="alphabet")
        return RECOGNIZER.find_language(RECOGNIZER.get_local_symbol_frequency(document))

    elif method == 2:
        RECOGNIZER = RecognizerFactory.get_recognizer(method_type="frequency_words")
        return RECOGNIZER.find_language(RECOGNIZER.get_local_word_frequency(document))
    else:
        RECOGNIZER = RecognizerFactory.get_recognizer(method_type="neural_network")
        return RECOGNIZER.predict_language(document)


def get_all_training_documents() -> 'list[Document]':
    return utils.get_all_documents_in_folder(LOCAL_PATH + "\\documents\\training_documents")


