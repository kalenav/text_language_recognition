from path import LOCAL_PATH
import utils
import json
from document import Document
import math


class AlphabetMethod:
    def __init__(self):
        with open('global_symbol_frequency.json', 'r+', encoding="utf-8") as file:
            try:
                self.__global_symbol_frequency = json.load(file)
            except json.JSONDecodeError:
                self.__global_symbol_frequency = {"eng": {}, "rus": {}}
                folder_path = LOCAL_PATH + "\\documents\\training_documents"

                for item in utils.get_subfolders_list(folder_path):
                    for document in utils.get_all_documents_in_folder(folder_path + "\\" + item):
                        local_symbol_amount = self.__count_local_symbol_amount(document)
                        for symbol in local_symbol_amount:
                            if symbol not in self.__global_symbol_frequency[item]:
                                self.__global_symbol_frequency[item][symbol] = local_symbol_amount[symbol]
                            else:
                                self.__global_symbol_frequency[item][symbol] += local_symbol_amount[symbol]

                    self.__calculate_symbol_frequency(self.__global_symbol_frequency[item])

                json.dump(self.__global_symbol_frequency, file, indent=4, ensure_ascii=False)

    def get_local_symbol_frequency(self, document: Document) -> dict[str: float]:
        return self.__calculate_symbol_frequency(self.__count_local_symbol_amount(document))

    @staticmethod
    def __count_local_symbol_amount(document: Document) -> dict[str: float]:
        local_symbol_amount = {}
        for symbol in document.text:
            if symbol.isalpha():
                if symbol not in local_symbol_amount:
                    local_symbol_amount[symbol] = 0
                local_symbol_amount[symbol] += 1
        return dict(sorted(local_symbol_amount.items()))

    @staticmethod
    def __calculate_symbol_frequency(symbol_amount: dict[str, int]) -> dict[str, float]:
        for symbol, frequency in symbol_amount.items():
            symbol_amount[symbol] /= sum(symbol_amount.values())
        return symbol_amount

    def find_language(self, local_symbol_frequency: dict[str: float]) -> str:
        distances = {}
        for item in self.__global_symbol_frequency:
            squared_difference = [
                pow(global_frequency - local_symbol_frequency.get(symbol, 0), 2)
                for symbol, global_frequency in self.__global_symbol_frequency[item].items()
            ]
            distances[item] = math.sqrt(sum(squared_difference))
        return min(distances, key=distances.get)
