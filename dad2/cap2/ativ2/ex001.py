table = [None] * 11

values = [54, 26, 93, 17, 77, 31]

def insertFunction(key):
    hash = key % 11
    table[hash] = key
    print(f"Elemento {key} inserido na posição {hash}")

for v in values:
    insertFunction(v)

print(table)