from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import utils
from document import Document
from path import LOCAL_PATH


class NeuralNetworkMethod:
    def __init__(self):
        self.__vectorizer = CountVectorizer()
        self.__classifier = MultinomialNB()

        self.__labels = [*["eng"]*5, *["rus"]*5]
        self.__label_dict = {label: idx for idx, label in enumerate(set(self.__labels))}
        self.__training_texts = [document.text for document in
                               utils.get_all_documents_in_folder(LOCAL_PATH + "\\documents\\training_documents")]

        # training bayes classifier
        training_input = self.__vectorizer.fit_transform(self.__training_texts)
        training_output = [self.__label_dict[label] for label in self.__labels]
        self.__classifier.fit(training_input, training_output)

    def predict_language(self, document: Document) -> str:
        test_input = self.__vectorizer.transform([document.text])
        return [lang for lang, idx in self.__label_dict.items() if idx == self.__classifier.predict(test_input)][0]
