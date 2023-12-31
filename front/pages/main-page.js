const recognitionMethodSelectLabelText = "Метод распознавания";
const recognizeButtonLabel = "Распознать";
const helpButtonLabel = "Помощь";
const recognitionMethods = [
    {
        name: "Алфавитный",
        value: 1
    },
    {
        name: "Частотных слов",
        value: 2
    },
    {
        name: "Нейросетевой",
        value: 3
    }
]

class MainPage extends Page {
    _currSelectedDocumentText = null;

    buildPage() {
        const self = this;

        const fileInput = ViewUtils.tag({
            name: "input",
            attributes: {
                type: "file",
                id: "file-input",
                class: "double-column-align-center"
            },
            eventListeners: {
                change: function () {
                    const fr = new FileReader();
                    fr.onload = function () {
                        self._currSelectedDocumentText = decodeURI(encodeURI(fr.result));
                    }
                    fr.readAsText(this.files[0], 'utf-8');
                }
            }
        });

        const methodSelectContainer = ViewUtils.tag({
            name: "div",
            attributes: {
                class: "double-column-align-center"
            },
            children: [
                ViewUtils.tag({
                    name: "label",
                    attributes: {
                        for: "method-select",
                        class: "method-select-label"
                    },
                    text: recognitionMethodSelectLabelText
                }),
                ViewUtils.tag({
                    name: "select",
                    attributes: { id: "method-select" },
                    children: recognitionMethods.map(recognitionMethod => ViewUtils.tag({
                        name: "option",
                        attributes: {
                            value: recognitionMethod.value,
                        },
                        text: recognitionMethod.name
                    }))
                })
            ]
        });

        const recognizeButton = ViewUtils.tag({
            name: "button",
            attributes: {
                class: "btn-default"
            },
            eventListeners: {
                click: async () => {
                    const methodSelect = document.getElementById('method-select');
                    const recognizedLanguage = await httpClient.post({
                        path: "recognize_lang",
                        body: {
                            text: this._currSelectedDocumentText,
                            method: +methodSelect.options[methodSelect.selectedIndex].value
                        }
                    });
                    const trainingDocumentsStatistics = await httpClient.get({
                        path: "test_collection_statistics"
                    });
                    recognitionResultPage.buildPage(recognizedLanguage, trainingDocumentsStatistics);
                    router.navigate(recognitionResultPage);
                }
            },
            text: recognizeButtonLabel
        });

        const helpButton = ViewUtils.tag({
            name: "button",
            attributes: {
                class: "btn-default"
            },
            eventListeners: {
                click: () => { alert('1. Выберите файл в формате HTML, язык которого требуется определить.\n2. Выберите метод определения языка.\n3. Нажмите кнопку "Распознать".'); }
            },
            text: helpButtonLabel
        })

        this._page = ViewUtils.tag({
            name: "div",
            attributes: {
                class: "main-page-container"
            },
            children: [
                fileInput,
                methodSelectContainer,
                recognizeButton,
                helpButton
            ]
        });
    }
}