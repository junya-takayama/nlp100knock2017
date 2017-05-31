from nlp100utils import MecabLoader as ml
sentences = ml()
print("\n".join(morp["base"] for morp in sentences.extractByPOS(pos1 = "サ変接続")[:10]))