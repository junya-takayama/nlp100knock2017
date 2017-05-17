import sys

def row_split(filename,n):
    sentence = open(filename,"r").readlines()
    l = len(sentence)/n
    return ["".join(sentence[int(start*l):int((start+1)*l)]) for start in range(n)]

if __name__ == "__main__":
    print("--\n".join(row_split(sys.argv[1],int(sys.argv[2]))))