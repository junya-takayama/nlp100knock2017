import pymongo
import json
import time
import sys

client = pymongo.MongoClient('localhost', 27017)

db = client.nlp100knock

#一旦全部消す
client.drop_database(db)

collection = db.artist
count = 0

datas = open("./data/artist.json","r").readlines()
length = len(datas)
start = time.time()

for i,line in enumerate(datas):
    collection.insert_one(json.loads(line))
    
    if not i%500 or i==(length-1):
        now = time.time() - start
        pred = (length-i)*(now/i) if i != 0 else "unknown"
        sys.stdout.write("\rregistering to DB..."+str(i)+"/"+str(length-1)+"\t経過"+str(now)+"秒\tあと"+str(pred)+"秒")
        sys.stdout.flush()



collection.create_index([("name", pymongo.ASCENDING)])
collection.create_index([("rating.value", pymongo.ASCENDING)])
collection.create_index([("tags.value", pymongo.ASCENDING)])
collection.create_index([("aliases.name", pymongo.ASCENDING)])    
client.close()
print("\n\033[92mDone.")