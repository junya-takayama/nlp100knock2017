
res = ""
for pref,temp in zip(open("./data/col1.txt"),open("./data/col2.txt")):
    res += pref.strip() + " " + temp

open("./data/merged.txt",'w').write(res)
