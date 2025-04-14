nlp = spacy.load("en_core_web_lg")

filepath = 'hughes-txt/sixteen.txt'
f = open(filepath, 'r', encoding='utf8').read()
spacyRead = nlp(f)
for token in spacyRead:
    print(token.text, "---->", token.pos_, ":::::", token.lemma_)
    spacy.explain("VERB")
    def wordCollector(words):
    wordList = []
    count = 0
    for token in words:
        if token.pos_ == "VERB":
            count += 1
            # print(count, ": ", token.text, " lemma: ", token.lemma_, " pos: ", token.pos_)
            # don't forget the underscore after token.lemma_ , token.pos_, etc.!
            wordList.append(token.lemma_)
            # print(count, ": ", token, token.pos_)
    # print(count, ": ", adjectives)
    return wordList
myWords = wordCollector(spacyRead)
print(myWords)
from collections import Counter

word_freq = Counter(myWords)
# most_common() converts the Counter's dictionary to a tuple series and sorts it
ranked = word_freq.most_common()
topTen = word_freq.most_common(10)
print(topTen)
lastTen = word_freq.most_common()[:-11:-1]
print(lastTen)

o = open("verbFreq.txt", "w")
for r in ranked:
    o.write(str(r) + "\n")
    import nltk
from nltk.corpus import wordnet as wn
setOfWords = set(myWords)
lowerCased = [w.lower() for w in setOfWords]

sortedWords = sorted(lowerCased)
print(sortedWords)
for w in myWords:
    synsets = len(wn.synsets(w))
    print("The word ", w, "belongs to ", synsets, "synsets in WordNet.")
    nlp = spacy.cli.download("en_core_web_lg")
    