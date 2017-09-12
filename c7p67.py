import pymongo
from pprint import pprint
import sys

client = pymongo.MongoClient('localhost', 27017)
db = client.nlp100knock
collection = db.artist

for document in collection.find({'aliases.name': sys.argv[1]}):
    pprint(document)