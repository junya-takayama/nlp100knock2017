from nlp100utils import ngram

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(ngram(str1,2,char=True))
Y = set(ngram(str2,2,char=True))

print("和集合:",X.union(Y))
print("積集合:",X.intersection(Y))
print("差集合:",X.difference(Y))

print("\"se\" in X:","se" in X)
print("\"se\" in Y:","se" in Y)
