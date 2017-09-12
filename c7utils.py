import redis
import pymongo

class RedisSearch:
    def __init__(self,port=6379,host="localhost",db=0):
        self.r = redis.Redis(port=port,host=host,db=db)
        
    def search_tags(self,artist):
        print("keyword:",artist)
        for data in eval(self.r.hget("tags",artist)):
            print("\t"+data["value"]+" ("+str(data["count"])+")")
            
    def search_area(self,artist):
        print("keyword:",artist)
        print("area:",self.r.hget("area",artist).decode())
        
    def allartists(self,key="area"):
        return list(map(bytes.decode ,self.r.hkeys(key)))
    
class MongoSearch:
    def __init__(self,port=27017,host="localhost"):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.nlp100knock
        self.collection = self.db.artist
        
    def ngram(self,text,n=2):
        return [text[i:i+n] for i in range(len(text)-n+1)] if len(text) > n else [text]
    
    def search(self,keyword,tags="",mode="ngram",n=2,descending=False):
        if type(keyword) != str and type(tags) != str or keyword=="":
            return []
        
        if mode == "ngram": #ngram検索．毎回ngram化の処理を行うので激重
            keyword = keyword.replace(" ","").lower()
            n = n if len(keyword) > n else len(keyword)
            keyword = self.ngram(keyword,n=n)[:15]
            
            #まずは　OR 検索で絞り込むことで少しでも軽く
            tags = tags.split()
            if len(tags) > 0:
                print("a")
                tmp = self.collection.find({"$and":[
                    {"$or":[{"name":{"$regex": elem}} for elem in keyword] + [{"aliases.name":{"$regex": elem}} for elem in keyword]},
                    {"$or":[{"tags.value":{"$regex":tag}} for tag in tags]}
                ]})
            else:
                tmp = self.collection.find({"$or":
                    [{"name":{"$regex": elem}} for elem in keyword] + 
                    [{"aliases.name":{"$regex": elem}} for elem in keyword]
                })
            result = []
            
            #ngramの類似度が0.4以上のものだけ表示
            cnt = 0
            for document in tmp:
                names = [document["name"]]
                if "aliases" in document.keys():
                    names.extend([alias["name"] for alias in document["aliases"]])
                
                score = 0
                for name in names:
                    value = self.ngram(name.replace(" ","").lower(),n=n)
                    n_vocab = len(set(value + keyword))
                    n_intersection = len(set(value).intersection(set(keyword)))
                    tmpscore = n_intersection/n_vocab
                    score = tmpscore if tmpscore > score else score

                if score > 0.3:    
                    result.append([score,document])
                    cnt += 1

                if cnt == 1000:
                    break
            
            #類似度が高い順にソート
            if len(result) > 0:
                _,result = zip(*sorted(result,key=lambda x:-x[0]))
            else:
                result = []
            
        elif mode == "like": #前方後方一致検索
            keyword = keyword.split()
            tags = tags.split()
            if len(tags) > 0:
                result = self.collection.find({"$and":[
                    {"$or":[{"name":{"$regex": elem}} for elem in keyword] + [{"aliases.name":{"$regex": elem}} for elem in keyword]},
                    {"$or":[{"tags.value":{"$regex":tag}} for tag in tags]}
                ]})
            else:
                result = self.collection.find({"$or":
                    [{"name":{"$regex": elem}} for elem in keyword] + 
                    [{"aliases.name":{"$regex": elem}} for elem in keyword]
                })
            
        else: #完全一致検索
            tags = tags.split()
            if len(tags) > 0:
                result = self.collection.find({"$and":[
                    {"$or":[{"name":keyword},{"aliases.name":keyword}]},
                    {"$or":[{"tags.values":tag} for tag in tags]}
                ]})
            else:
                result = self.collection.find({"$or":[{"name":keyword},{"aliases.name":keyword}]})
        
        if descending:
            result.sort("rating",pymongo.DESCENDING)
            
        return list(result)[:50]
        
    def close(self):
        self.client.close()
        return None