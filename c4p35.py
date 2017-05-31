from nlp100utils import MecabLoader
ml = MecabLoader()

result = []
for sent in ml.sentences:
    tmp = []
    for word in sent:
        if word['pos'] == "名詞":
            tmp.append(word["surface"])
        else:
            if len(tmp) > 1:
                result.append("".join(tmp))
            tmp = []

print('\n'.join(result[:10]))