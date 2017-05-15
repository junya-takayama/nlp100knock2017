sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

count = [len(string.strip(",.")) for string in sentence.split()]
print(count)
