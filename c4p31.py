from nlp100utils import MecabLoader as ml
sentences = ml()
print("\n".join(morp["surface"] for morp in sentences.extractByPOS("動詞")[:10]))