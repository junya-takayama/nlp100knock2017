import sys

def head(filename,n):
    with open(filename,"r") as f:
        return "".join(f.readline() for i in range(n)).strip()
    
if __name__ == "__main__":
    print(head(sys.argv[1],int(sys.argv[2])))