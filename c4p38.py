from nlp100utils import MecabLoader
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
ml = MecabLoader()
matplotlib.rcParams["font.family"] =  'AppleGothic' #日本語ラベル対策

n = 10

_,freqList = zip(*Counter(word["base"] for sent in ml.sentences for word in sent).items())
x_freq,y_sum = zip(*sorted(Counter(freqList).items(),key=lambda x:x[0])[:n])

plt.bar(x_freq,y_sum)
plt.xlabel("frequency")
plt.ylabel("number of types of words")
#plt.xticks(x,word,rotation=30)
plt.show()