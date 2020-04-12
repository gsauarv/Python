import random
alpha="abcdefghijklmnopqrstuvwxyz"
def encrypt(original,key=none):
    if key is None:
        l=list(alpha)
        random.shuffle(l)
        key="".join(l)
        new=[]
        for letter in original:
            new.append(key[alpha.index(letter)])
            return["".join(new),key]

e=encrypt("Monoalphabetic",None)
print(e)