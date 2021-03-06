from pprint import pprint
import re
import requests
from nlp100utils import Jawiki

reg26 = re.compile("'+") #強調マークアップ
reg27 = re.compile("\[{2}([^\]]+?\|)*(.*?)\]{2}") #内部リンク・ファイル・カテゴリ
reg28a = re.compile("\[([^\]]+?\s)?(.*?)\]") #外部リンク
reg28b = re.compile("\<.+?\>") #HTMLタグ
reg28c = re.compile("\{{2}[l|L]ang\|.+\|(.+)\}{2}") #言語情報

def preProcess(text):
    text = reg26.sub("",text)
    text = reg27.sub(r"\2",text)
    text = reg28a.sub("",text)
    text = reg28b.sub("",text)
    text = reg28c.sub(r"\1",text)
    return text

jawiki = Jawiki()
jawiki.getArticle("イギリス")
dic = jawiki.getBasicInfo(preProcess)

api = "https://en.wikipedia.org/w/api.php"
params = {"action" : "query", 
          "titles" : "File:{}".format(dic["国旗画像"]),
          "prop" : "imageinfo",
          "format" : "json",
          "iiprop" : "url"}

data = requests.get(api, params=params).json()
pprint(data)

def searchImageURL(data):
    target = data["query"]["pages"]
    result = []
    for pageID in target.keys():
        for elem in target[pageID]["imageinfo"]:
            if "url" in elem.keys():
                result.append(elem["url"])
    return result
        
print("\n".join(searchImageURL(data)))