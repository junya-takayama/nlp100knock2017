from nlp100utils import MecabLoader
from collections import Counter
from pprint import pprint
ml = MecabLoader()

pprint(
    sorted(
        Counter(
            word["surface"] for sent in ml.sentences for word in sent
        ).items(),
        key=lambda x:-x[1]
    )[:10]
)