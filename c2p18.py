str = "".join(line for line in sorted(open("./data/hightemp.txt"),key=lambda x:-float(x.split("\t")[2])))
print(str)
open("./data/sorted_hightemp.txt","w").write(str)