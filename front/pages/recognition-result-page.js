const columnHeaders = ["Наименование документа", "Сниппет", "Язык"];

class RecognitionResultPage extends Page {
    async buildPage(recognizedLanguage, trainingDocumentsStatistics = []) {
        this._page = ViewUtils.tag({
            name: "div",
            children: [
                ViewUtils.tag({ name: "p", text: "Распознанный язык:" }),
                ViewUtils.tag({ name: "h2", text: this._getLanguage(recognizedLanguage) }),
                ViewUtils.tag({ name: "hr", attributes: { class: "recognition-result-page-hr" } }),
                ViewUtils.tag({ name: "p", text: "Сводка по тренировочной коллекции документов:" }),
                ViewUtils.tag({
                    name: "table",
                    attributes: {
                        class: "doc-statistics-table"
                    },
                    children: [
                        ViewUtils.tag({
                            name: "tr",
                            children: columnHeaders.map(header => ViewUtils.tag({ name: "th", text: header }))
                        }),
                        ...trainingDocumentsStatistics.map(documentInfo => ViewUtils.tag({
                            name: "tr",
                            children: [
                                ViewUtils.tag({ name: "td", text: documentInfo.name }),
                                ViewUtils.tag({ name: "td", text: documentInfo.snippet }),
                                ViewUtils.tag({ name: "td", text: this._getLanguage(documentInfo.language) })
                            ]
                        }))
                    ]
                }),
                ViewUtils.tag({
                    name: "button",
                    attributes: {
                        class: "back-btn"
                    },
                    eventListeners: {
                        click: () => {
                            router.navigate(mainPage);
                        }
                    },
                    text: "Назад"
                })
            ]
        })
    }

    _getLanguage(shortLanguage) {
        return shortLanguage === "rus" ? "Русский" : "Английский";
    }
}