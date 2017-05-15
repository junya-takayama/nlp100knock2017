def fmt(X,Y,Z):
    #フォーマットは引数の型strじゃなくてもいいっぽい？
    return "{0}時の{1}は{2}".format(X,Y,Z)

print(fmt(12,"気温",22.4))
