from nlp100utils import Jawiki
import re

jawiki = Jawiki()

text = jawiki.getArticle("イギリス")
for line in text.split("\n"):
    if "Category:" in line:
        print(line)


