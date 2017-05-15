from nlp100utils import Jawiki
import sys

jawiki = Jawiki()
print(jawiki.getArticle(sys.argv[1]))