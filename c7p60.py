import redis
import getpass
import json
import sys
import time

#6379で動いてるredisのdb0に接続
r = redis.Redis(port=6379,host="localhost",db=0)
key = "area"

#とりあえず消す
r.delete(key)

#逐次処理は遅いのでとりあえずpipelineを構築
pipe = r.pipeline()



#jsonからデータを読み込み，キー"area"にデータを追加

datas = open("./data/artist.json","r").readlines()
length = len(datas)
start = time.time()

for i,line in enumerate(datas):
    
    tmp = json.loads(line)
    if "area" in tmp.keys():
        #r.hset(key,tmp["name"],tmp["area"]) #逐次実行（遅い）
        pipe.hset(key,tmp["name"],tmp["area"])
        
    if not i%1000 or i==(length-1):
        now = time.time() - start
        pred = (length-i)*(now/i) if i != 0 else "unknown"
        sys.stdout.write("\rloading..."+str(i)+"/"+str(length-1)+"\t経過"+str(now)+"秒\tあと"+str(pred)+"秒")
        sys.stdout.flush()

print("\nregistering to DB...")
pipe.execute() #一括処理（はやい）
print("\033[92mDone.")