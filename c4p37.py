from nlp100utils import MecabLoader
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
ml = MecabLoader()
matplotlib.rcParams["font.family"] =  'AppleGothic' #日本語ラベル対策


word,freq = zip(
    *sorted(
        Counter(
            word["base"] for sent in ml.sentences for word in sent
        ).items(),key=lambda x:-x[1]
    )[:10]
)

x = [i for i in range(10)]
plt.bar(x,freq)
plt.xlabel("surface of words")
plt.ylabel("frequency")
plt.xticks(x,word,rotation=30)
plt.show()