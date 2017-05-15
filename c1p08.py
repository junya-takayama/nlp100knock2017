"""
def cipher(sent):
    return "".join(chr(219-ord(char)) if char.islower() else char for char in sent)
"""

def cipher(sent):
    res = ""
    for char in sent:
        res += chr(219-ord(char)) if char.islower() else char
    return res

if __name__ == "__main__":
    
    ciphered = cipher(input("input: "))
    print("ciphered  : ",ciphered)
    print("deciphered: ",cipher(ciphered))
