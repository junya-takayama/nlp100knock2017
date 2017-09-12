import pymongo
import json

client = pymongo.MongoClient('localhost', 27017)

db = client.nlp100knock

collection = db.artist

print("Japanの頻度：",collection.find({"area": "Japan"}).count())