def simpleInsert(key, table):
    h = key % len(table)
    
    if table[h] is not None: 
        print(f"Elemento {table[h]} perdido")
    
    table[h] = key

def linearInsert(key, table):
    h = key % len(table)

    if table[h] is None:
        table[h] = key

    else:
        for i in range(1, len(table)):
            aux = (h+i) % len(table)

            if table[aux] is None:
                table[aux] = key
                return

def quadraticInsert(key, table):
    h = key % len(table)

    if table[h] is None:
        table[h] = key
    
    else:
        for i in range(1, len(table)):
            aux = (h + i**2) % len(table)

            if table[aux] is None:
                table[aux] = key   
                return

def doubleInsert(key, table):
    h = key % len(table)

    if table[h] is None:
        table[h] = key
    
    else:
        h2 = (key % (len(table) -2 )) + 1

        for i in range(1, len(table)):
            aux = (h + i * h2) % len(table)

            if table[aux] is None:
                table[aux] = key
                return
    
def testFunction(func, values):
    table = [None] * 7

    for v in values:
        func(v, table)

    print("Saída final: ", table)

############

values = [14, 15, 1, 35, 18]

print(f"\nInserção simples: ")
testFunction(simpleInsert, values)

print(f"\nInserção sondagem linear: ")
testFunction(linearInsert, values)

print(f"\nInserção sondagem quadrática: ")
testFunction(quadraticInsert, values)

print(f"\nInserção sondagem duplo hash: ")
testFunction(doubleInsert, values)

