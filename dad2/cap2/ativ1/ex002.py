values = [113, 117, 97, 100, 114, 108, 116, 105, 99]
table = [None] * 11

def insertTable(key, table):
    h = key % len(table)

    if table[h] is None:
        table[h] = key
        print(f"Elemento {key} inserido na posição {h}")

    else:
        for i in range(1, len(table)):
            aux = (h+i) % len(table)

            if table[aux] is None:
                table[aux] = key
                print(f"Elemento {key} inserido na posição {aux}")
                return

        print("Tabela cheia!")


for v in values:
    insertTable(v, table)


print(table)