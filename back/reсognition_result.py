from document import Document


class RecognitionResult:
    def __init__(self, document: Document, language: bool, statistics: str):
        self.document = document
        self.language = language
        self.statistics = statistics

    def save_to_file(self):
        with open('result.html', 'a') as file:
            try:
                file.write(f"Название документа: {self.document.name}\n"
                           f"Язык документа: {'english' if self.language else 'русский'}\n"
                           f"Статистика: {self.statistics}")
            except Exception as e:
                print(f"Произошла ошибка при сохранении данных: {e}")
