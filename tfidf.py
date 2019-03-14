import math
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

"""
counterlist = []
word = "very"

bloblist = []
f= open("corpus.txt", "r")
for document in f.readlines():
    bloblist.append(tb(document))

print(bloblist)

def sort_by_relevance(word, bloblist):
    for i, blob in enumerate(bloblist):
        counter=(i+1, tfidf(word, blob, bloblist))
        if(counter[1] != 0):
            counterlist.append(counter)
    sortedList = sorted(counterlist, key=lambda x: x[1], reverse=True)
    return sortedList"""

def sort_by_relevance(word, bloblist):
    counterlist = []
    for blob in bloblist:
        counter=(str(blob), tfidf(word, blob, bloblist))
        if(counter[1] != 0):
            counterlist.append(counter)
    sortedList = sorted(counterlist, key=lambda x: x[1], reverse=True)
    return sortedList


"""print(len(sort_by_relevance(word, bloblist)))
print(sort_by_relevance(word, bloblist))"""