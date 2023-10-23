from flask import Flask, request, jsonify
from flask_cors import CORS
from main import recognize_lang, get_all_training_documents

app = Flask(__name__)
CORS(app)

@app.route('/recognize_lang', methods=['POST'])
def recognize():
    print(recognize_lang(request.json["text"], request.json["method"]))
    return jsonify(recognize_lang(request.json["text"], request.json["method"]))

@app.route('/test_collection_statistics', methods=['GET'])
def statistics():
    return list(map(lambda document: {
        "name": document.name,
        "snippet": document.text[:300],
        "language": document.language
    }, get_all_training_documents()))

if __name__ == '__main__':
    app.run()