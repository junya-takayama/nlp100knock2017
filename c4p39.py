from nlp100utils import MecabLoader
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
ml = MecabLoader()
matplotlib.rcParams["font.family"] =  'AppleGothic' #日本語ラベル対策

n = 10

_,freqList = zip(*Counter(word["surface"] for sent in ml.sentences for word in sent).items())
y_freq,x_sum = zip(*sorted(Counter(freqList).items(),key=lambda x:x[0])[:n])

plt.plot(x_sum,y_freq,'o')
plt.xlabel("frequency")
plt.ylabel("rank of word frequency")
plt.xscale('log')
plt.yscale('log')
#plt.xticks(x,word,rotation=30)
plt.show()