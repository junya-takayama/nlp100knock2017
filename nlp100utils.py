import re
from collections import OrderedDict

def ngram(seq,n,char=False):
    if isinstance(seq,str):
        #seqがstr型だったらカンマとピリオドの処理
        seq = re.sub(",|\.","",seq)
        if not char:
            #単語n-gramならseqをスペースで分割してリスト化
            seq = seq.split()
    return [seq[i:i+n] for i in range(len(seq) - n + 1)]

class Jawiki:
    def __init__(self,filepath="./data/jawiki-country.json"):
        import json
        self.text = ""
        self.data = [json.loads(line) for line in open(filepath)]
        return

    def getArticle(self,key):
        #タイトルをキーに記事全文を取得する
        #結果はインスタンス変数に代入される
        for article in self.data:
            if key == article["title"]:
                self.text = article["text"]
                break
        return self.text

    def extractRow(self,regExp):
        #regExpで与えられた正規表現にマッチした行を返す
        return [line for line in self.text.split("\n") if regExp.match(line)]
    
    def rMatch(self,regExp):
        #regExpで与えられた正規表現に対し、マッチした部分だけ返す
        return [match for match in regExp.findall(self.text)]

    def getAllTitles(self):#使わない
        #全記事のタイトルを返す
        return [self.data[i]["title"] for i in range(len(self.data))]

    def getBasicInfo(self,preProcess=lambda x: x):
        #基礎情報を辞書形式で返す
        #テキストに対して前処理を施したい場合はpreProcessに関数オブジェクトを渡す
        reg = re.compile("\{\{(基礎情報[\s\S]+?)\}\}\n")
        text = self.rMatch(reg)
        dic = OrderedDict()
        reg = re.compile("\|(.+)\s\=\s(.+)")
        for match in self.rMatch(reg):
            dic[match[0]] = preProcess(match[1])
        return dic
    