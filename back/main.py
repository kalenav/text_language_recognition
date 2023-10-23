from document import Document

def recognize_lang(text: str, method: int) -> str:
    if method == 1:
        # return alphabetic(text)
        return 'rus'
    elif method == 2:
        # return frequential(text)
        return 'eng'
    else:
        # return neural(text)
        return 'rus'
        
def get_all_training_documents() -> list[Document]:
    return []