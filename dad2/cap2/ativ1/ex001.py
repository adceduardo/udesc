table = [None] * 13
output = ""

def insertFunction(key):
    hash = key % 11
    table[hash] = key
    print(f"Elemento {key} inserido na posição {hash}")

insertFunction(27)
insertFunction(30)

for i in range(len(table)):
    if table[i] is not None:
        output += f"{i}, "

print("\nPosições: ", output.rstrip(", "))
