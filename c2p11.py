text = open("./data/hightemp.txt",'r').readlines()

print("".join(line.replace("\t"," ") for line in text))
