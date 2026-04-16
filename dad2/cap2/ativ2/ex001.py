table = [None] * 11

def spreadFunction(key):
    hash = key % 11
    table[hash] = key
    print(f"Elemento {key} inserido na posição {hash}")

spreadFunction(54)
spreadFunction(26)
spreadFunction(93)
spreadFunction(17)
spreadFunction(77)
spreadFunction(31)

print(table)