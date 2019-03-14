from flask import Flask, json, jsonify, request, Response
from textblob import TextBlob
from tfidf import *

app = Flask(__name__)


def validCorpusObject(corpusObject):
    if ("text" in corpusObject):
        return True
    else:
        return False


def validWordObject(wordObject):
    if ("word" in wordObject):
        return True
    else:
        return False

@app.route("/adddocument", methods=["POST"])
def add_document_to_corpus():
    request_data = request.get_json()
    if(validCorpusObject(request_data)):
        save_file(request_data["text"])
        response=Response("", 201, mimetype="application/json")
        return response
    else:
        return False

@app.route("/sort")
def sort_documents():
    request_data = request.get_json()
    if(validWordObject(request_data)):
        word = request_data["word"]
        bloblist = []
        read_file(bloblist)
        sorted_tuples = sort_by_relevance(word, bloblist)
        sorted_documents = []
        for s in sorted_tuples:
            new_object = {
                'document' : s[0],
                'tfidf' : s[1]
            }
            sorted_documents.append(new_object)
        return jsonify({'documents': sorted_documents})
    else:
        return False


def save_file(document):
    try:
        f = open("corpus.txt", "a")
        f.write(document + "\n")
        f.close()
    except Exception:
        print("File not saved")


def read_file(bloblist):
    try:
        f= open("corpus.txt", "r")
        for document in f.readlines():
            bloblist.append(TextBlob(document))
    except Exception:
        print("Could not read file")

if __name__ == "__main__":
    app.run()

