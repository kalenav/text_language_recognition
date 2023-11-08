from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
import utils
from document import Document
from path import LOCAL_PATH


class NeuralNetworkMethod:
    def __init__(self):
        labels = [*["eng"] * 5, *["rus"] * 5]
        self.__label_dict = {label: idx for idx, label in enumerate(set(labels))}
        training_texts = [document.text for document in
                          utils.get_all_documents_in_folder(LOCAL_PATH + "\\documents\\training_documents")]

        self.__vectorizer = TfidfVectorizer()
        training_input = self.__vectorizer.fit_transform(training_texts)
        training_output = [self.__label_dict[label] for label in labels]

        self.__classifier = MLPClassifier()
        self.__classifier.fit(training_input, training_output)

    def predict_language(self, document: Document) -> str:
        test_input = self.__vectorizer.transform([document.text])
        return [lang for lang, idx in self.__label_dict.items() if idx == self.__classifier.predict(test_input)][0]
