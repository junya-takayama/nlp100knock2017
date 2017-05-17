from collections import Counter
hightemp = [line.split("\t") for line in open("./data/hightemp.txt","r")]
count = Counter(line[0] for line in hightemp)
for line in sorted(hightemp,key=lambda x: (count[x[0]],x[0]),reverse=True):
    print("\t".join(line),end="")