import pymongo
import pandas as pd
from IPython.core.display import display

client = pymongo.MongoClient('localhost', 27017)
db = client.nlp100knock
collection = db.artist

results = []
for i,document in enumerate(collection.find({'tags.value': 'dance'}).sort('rating.count', pymongo.DESCENDING)):
    if i == 10:
        break
    results.append((document["name"],document["rating"]["value"]))

table = pd.DataFrame(results)
table.columns = ["name","rating"]
display(table)
