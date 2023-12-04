from nltk.stem import PorterStemmer

class WordStemmer:
    def __init__(self):
        self.stemmer = PorterStemmer()

    def stem_words(self, words):
        return [[self.stemmer.stem(word) for word in sublist] for sublist in words]


