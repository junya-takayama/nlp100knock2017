import random

thre = 4
dfltText = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

"""
#ボツ
def wShuffle(word):
    if len(word) > thre:
        tmp = list(word[1:-1])
        random.shuffle(tmp)
        return word[0] + "".join(tmp) + word[-1]
    else:
        return word
"""

def wShuffle(word):
    length = len(word)
    if length > thre:
        tmp = random.sample(word[1:-1],length-2)
        return word[0] + "".join(tmp) + word[-1]
    else:
        return word

def typoglycemia(sent):
    return " ".join(map(wShuffle,sent.split()))

if __name__ == "__main__":
    print(typoglycemia(dfltText))
