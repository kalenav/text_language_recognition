import json
from document import Document
from path import LOCAL_PATH
import utils
import math


class FrequencyWordsMethod:
    def __init__(self):
        with open('global_word_frequency.json', 'r+', encoding="utf-8") as file:
            try:
                self.__global_word_frequency = json.load(file)
            except json.JSONDecodeError:
                self.__global_word_frequency = {"eng": {}, "rus": {}}
                folder_path = LOCAL_PATH + "\\documents\\training_documents"

                for item in utils.get_subfolders_list(folder_path):
                    for document in utils.get_all_documents_in_folder(folder_path + "\\" + item):
                        local_word_amount = self.__count_local_word_amount(document)
                        for word in local_word_amount:
                            if word not in self.__global_word_frequency[item]:
                                self.__global_word_frequency[item][word] = local_word_amount[word]
                            else:
                                self.__global_word_frequency[item][word] += local_word_amount[word]

                    self.__calculate_word_frequency(self.__global_word_frequency[item])

                json.dump(self.__global_word_frequency, file, indent=4, ensure_ascii=False)

    def get_local_word_frequency(self, document: Document) -> dict[str: float]:
        return self.__calculate_word_frequency(self.__count_local_word_amount(document))

    @staticmethod
    def __count_local_word_amount(document: Document) -> dict[str: float]:
        local_word_amount = {}
        for word in document.normalized():
            if word not in local_word_amount:
                local_word_amount[word] = 0
            local_word_amount[word] += 1
        return local_word_amount

    @staticmethod
    def __calculate_word_frequency(word_amount: dict[str, int]) -> dict[str, float]:
        for word, frequency in word_amount.items():
            word_amount[word] /= sum(word_amount.values())
        return word_amount

    def find_language(self, local_word_frequency: dict[str: float]) -> str:
        distances = {}
        for item in self.__global_word_frequency:
            squared_difference = [
                pow(local_word_frequency[word] - self.__global_word_frequency[item].get(word, 0), 2)
                for word in local_word_frequency
            ]
            distances[item] = math.sqrt(sum(squared_difference))
        print(distances)
        return min(distances, key=distances.get)
