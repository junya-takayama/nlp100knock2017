import sys

def tail(filename,n):
    #こっちもで１４番と同様に必要な行だけ読み込む形にしたい
    #やり方わかる人がいたら教えてください
    return "".join(line for line in open(filename,"r").readlines()[-n:]).strip()

if __name__ == "__main__":
    print(tail(sys.argv[1],int(sys.argv[2])))