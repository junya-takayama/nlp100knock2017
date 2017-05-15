import re
from nlp100utils import Jawiki

jawiki = Jawiki()
jawiki.getArticle("イギリス")
reg = re.compile("=(=+)\s*(.*?)\s*(=+)")

for match in jawiki.rMatch(reg):
    print(match[1],"lv."+str(len(match[0])))
