from nlp100utils import MecabLoader
ml = MecabLoader()
result = []
for sent in ml.sentences:
    for i,current in enumerate(sent[1:-2]):
        if current["surface"] == "の":
            prevMorp = sent[i]
            nextMorp = sent[i+2]
            if prevMorp["pos"] == "名詞" and nextMorp["pos"] == "名詞":
                result.append(prevMorp["surface"] + current["surface"] + nextMorp["surface"])
print('\n'.join(result[:10]))