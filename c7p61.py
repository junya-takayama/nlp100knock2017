import redis

#6379で動いてるredisのdb0に接続
r = redis.Redis(port=6379,host="localhost",db=0)

print("area: ",r.hget("area",input("artist: ")).decode())