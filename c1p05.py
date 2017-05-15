from nlp100utils import ngram
import time

sent = "I am a NLPer."
    
print("単語bigram :",ngram(sent,2))
print("文字bigram :",ngram(sent,2,char=True))
