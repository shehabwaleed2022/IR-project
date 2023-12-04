from Classes.TokenizationClass import TokenizationDocument
from Classes.StemmingClass import WordStemmer
from Classes.FilesReaderClass import FilesReader
####### First part 

# Read 10 files
print('Reading files:')
print(FilesReader().readFiles('Articles'))
print('----------------')

# Apply tokenization
print('Tokenization:')
terms = TokenizationDocument('Articles').tokinize() 
print(terms)
print('----------------')

# Apply stemming
print('Stemming:')
print(WordStemmer().stem_words(terms))
print('----------------')
