import re

def sentSplit(fp = "./data/nlp.txt"):
    pattern = re.compile("(?P<A>[\.:;!\?]) (?P<B>[A-Z])")
    return [pattern.sub("\g<A>\n\g<B>",line.strip()) for line in open(fp)]
        
if __name__ == "__main__":
    print("\n".join(sentSplit()))