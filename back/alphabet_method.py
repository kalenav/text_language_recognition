from path import LOCAL_PATH
import utils
import json
from document import Document


class AlphabetMethod:
    def __init__(self):
        self.distance = 0
        with open('global_symbol_frequency.json', 'r+', encoding="utf-8") as file:
            try:
                self.global_symbol_frequency = json.load(file)
            except json.JSONDecodeError:
                self.global_symbol_frequency = {"eng": {}, "rus": {}}
                folder_path = LOCAL_PATH + "\\documents\\training_documents"

                for item in utils.get_subfolders_list(folder_path):
                    for document in utils.get_all_documents_in_folder(folder_path + "\\" + item):
                        local_symbol_amount = self.count_local_symbol_amount(document)
                        for symbol in local_symbol_amount:
                            if symbol not in self.global_symbol_frequency[item]:
                                self.global_symbol_frequency[item][symbol] = local_symbol_amount[symbol]
                            else:
                                self.global_symbol_frequency[item][symbol] += local_symbol_amount[symbol]

                    self.calculate_symbol_frequency(self.global_symbol_frequency[item])

                json.dump(self.global_symbol_frequency, file, indent=4, ensure_ascii=False)

    def get_local_symbol_frequency(self, document: Document) -> dict[str: float]:
        return self.calculate_symbol_frequency(self.count_local_symbol_amount(document))

    def count_local_symbol_amount(self, document: Document) -> dict[str: float]:
        local_symbol_amount = {}
        count = 0
        for symbol in document.text:
            if symbol.isalpha():
                count += 1
                if symbol not in local_symbol_amount:
                    local_symbol_amount[symbol] = 0
                local_symbol_amount[symbol] += 1
        return dict(sorted(local_symbol_amount.items()))

    def calculate_symbol_frequency(self, symbol_amount: dict[str, int]) -> dict[str, float]:
        for symbol, frequency in symbol_amount.items():
            symbol_amount[symbol] /= sum(symbol_amount.values())
        return symbol_amount

    def find_distance(self, local_symbol_frequency: dict[str: float]) -> float:
        # корень квадратный из суммы квадратов разностей частот
        # если в global_symbol_frequency символ есть, а в local... нет - разность равна global_symbol_frequency
        pass


if __name__ == "__main__":
    print(AlphabetMethod().get_local_symbol_frequency(utils.get_document_by_name("rus_cars.html")))
