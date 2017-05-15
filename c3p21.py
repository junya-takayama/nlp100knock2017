from nlp100utils import Jawiki
import re

jawiki = Jawiki()

jawiki.getArticle("イギリス")
regExp = re.compile("\[\[Category:.*\]\]")
print("\n".join(jawiki.extractRow(regExp)))
