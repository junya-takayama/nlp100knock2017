import re
from nlp100utils import Jawiki

jawiki = Jawiki()

jawiki.getArticle("イギリス")
regExp = re.compile("\[\[Category:(.+)\]\]")
print("\n".join(jawiki.rMatch(regExp)))
