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

class Morph(object):
    def __init__(self,surface,pos,pos1,base):
        self.surface = surface
        self.pos = pos
        self.pos1 = pos1
        self.base = base
    def __call__(self):
        #pprint用。呼ばれたら辞書で返事
        return {"surface":self.surface,
                "pos":self.pos,
                "pos1":self.base,
                "freq:":self.freq}
    
class MecabLoader:
    """
    mecab解析結果のテキストファイルを読み込んでいい感じに処理してくれるやつ
    第４章で使用
    """
    def __init__(self,filepath="./data/neko.txt.mecab"):
        separator = re.compile('\t|\,')
        self.sentences = []
        morphDict = dict()
        tmp = []
        for line in open(filepath):
            line = line.strip()
            if 'EOS' in line:
                if len(tmp) is not 0:
                    self.sentences.append(tmp)
                    tmp = []
                continue
            if line in morphDict.keys():
                """
                既知の形態素なら過去に生成した辞書オブジェクトを再利用
                """
                tmp.append(morphDict[line])
            else:
                """
                未知の形態素なら辞書オブジェクトを生成
                morphDictにkey:line,value:生成した辞書オブジェクト  を追加し、
                以降同じ形態素が出てきたら再利用できるようにする。
                全単語数２０００００以上に対し使われている語彙数は１５０００とかなので
                メモリ使用量をかなり節約できるはず
                """
                surface,pos,pos1,_,_,_,_,base = separator.split(line)[:8]
                tmp_m = {
                    "surface":surface,
                    "pos":pos,
                    "pos1":pos1,
                    "base":base,
                }
                #tmp_m = Morph(surf,pos,pos1,base)
                morphDict[line] = tmp_m
                tmp.append(tmp_m)
        self.morphs = list(morphDict.values())
        return
    
    def __call__(self):
        return self.sentences
    
    def extractByPOS(self,pos=None,pos1=None):
        """
        品詞または品詞細目で検索して、一致する形態素を返す
        31,32,33で使用
        """
        c_pos = lambda x: x["pos"] if pos else None
        c_pos1 = lambda x: x["pos1"] if pos1 else None
        tmp = [morph 
            for sent in self.sentences
            for morph in sent 
            if pos == c_pos(morph) and pos1 == c_pos1(morph)]
        return tmp
        