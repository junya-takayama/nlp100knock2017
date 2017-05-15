from pprint import pprint
import re
from nlp100utils import Jawiki

reg26 = re.compile("'+")
reg27 = re.compile("\[{2}([^\]]+?\|)*(.*?)\]{2}")

def preProcess(text):
    text = reg26.sub("",text)
    text = reg27.sub(r"\2",text)
    return text

jawiki = Jawiki()
jawiki.getArticle("イギリス")
dic = jawiki.getBasicInfo(preProcess)

pprint(dic)