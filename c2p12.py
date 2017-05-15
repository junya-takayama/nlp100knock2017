
col1 = []
col2 = []
for line in open("./data/hightemp.txt",'r'):
    tmp = line.strip().split("\t")
    col1.append(tmp[0])
    col2.append(tmp[1])

open("col1.txt",'w').write("\n".join(col1))
open("col2.txt",'w').write("\n".join(col2))
