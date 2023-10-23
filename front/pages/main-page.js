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
    buildPage() {
        const fileInput = ViewUtils.tag({
            name: "input",
            attributes: {
                type: "file",
                id: "file-input",
                class: "double-column-align-center"
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
                        value: recognitionMethod.value,
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
                click: () => { alert(3); }
            },
            text: recognizeButtonLabel
        });

        const helpButton = ViewUtils.tag({
            name: "button",
            attributes: {
                class: "btn-default"
            },
            eventListeners: {
                click: () => { alert(2); }
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