import pymongo
from pprint import pprint

client = pymongo.MongoClient('localhost', 27017)
db = client.nlp100knock
collection = db.artist

for document in collection.find({'name': "Queen"}):
    pprint(document)