from nlp100utils import MecabLoader as ml
from pprint import pprint
corpus = ml()
pprint(corpus()[:10])