import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from natsort import natsorted


class FilesReader:
    def __init__(self):
        self.docs = []

    def readFiles(self, folder_name):
        file_names = natsorted(os.listdir(folder_name))

        for file in file_names:
            file_path = os.path.join(folder_name, file)
            with open(file_path, 'r') as f:
                document = f.read()
                self.docs.append(document)

        return self.docs

