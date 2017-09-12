from nltk.stem.porter import PorterStemmer
from c6p51 import wordSplit

if __name__ == "__main__":
    stemmer = PorterStemmer()
    words = [word for sent in wordSplit() for word in sent]
    stems = list(map(stemmer.stem,tmp))
    for word,stem in zip(words,stems):
        print(word,"--->",stem)