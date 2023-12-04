import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from natsort import natsorted

class TokenizationDocument:
    def __init__(self, folder_name):
        self.folder_name = folder_name
        self.stopWords = stopwords.words('english')
        self.docOfTerms = []

    def tokinize(self):
        file_names = natsorted(os.listdir(self.folder_name))

        for file in file_names:
            with open(os.path.join(self.folder_name, file), 'r') as f:
                document = f.read()
            tokenized_docs = word_tokenize(document)
            terms = [word for word in tokenized_docs if word not in self.stopWords]
            self.docOfTerms.append(terms)

        return self.docOfTerms

