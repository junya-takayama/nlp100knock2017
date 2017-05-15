import re
from nlp100utils import Jawiki
jawiki = Jawiki()
jawiki.getArticle("イギリス")
reg = re.compile("\[\[(File|ファイル):(.*?)\|")

for data in jawiki.rMatch(reg):
    print(data[1])
