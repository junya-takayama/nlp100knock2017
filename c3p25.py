from pprint import pprint
from nlp100utils import Jawiki

jawiki = Jawiki()
jawiki.getArticle("イギリス")
dic = jawiki.getBasicInfo()

pprint(dic)
