from pprint import pprint
import re
from nlp100utils import Jawiki

reg26 = re.compile("'+")

def preProcess(text):
    text = reg26.sub("",text)
    return text

jawiki = Jawiki()
jawiki.getArticle("イギリス")
dic = jawiki.getBasicInfo(preProcess)

pprint(dic)