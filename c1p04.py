from collections import OrderedDict

sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = [word.strip(",.") for word in sent.split()]

targets = [1, 5, 6, 7, 8, 9, 15, 16, 19]

dic = OrderedDict([(words[i][0] if i+1 in targets else words[i][:2],i)for i in range(len(words))])

print(dic)
