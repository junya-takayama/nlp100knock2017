import redis
import getpass
from collections import Counter

print("Japanの頻度：",Counter(redis.Redis(port=6379,host="localhost",db=0).hvals("area"))[b"Japan"])

"""
#せつぞく
r = redis.Redis(port=6379,host="localhost",db=0)

#値だけ全部抽出
areas = r.hvals("area")

#数え上げて"Japan"の頻度を抽出
count = Counter(areas)
print(count[b"Japan"])
"""