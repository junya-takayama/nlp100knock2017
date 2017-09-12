import re
from c6p50 import sentSplit

def wordSplit(fp = "./data/nlp.txt"):
    return [[word for word in line.split()] for line in sentSplit(fp)]

if __name__ == "__main__":
    print("\n".join([word for sent in wordSplit() for word in sent]))