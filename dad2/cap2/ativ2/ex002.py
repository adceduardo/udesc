table = [None] * 11

def insertKey(key):
    h = key % len(table)
    table[h] = key
    print(f"Elemento {key} inserido na posição {h}")

def findKey(table, key):
    h = key % len(table)

    if table[h] and table[h] == key:
        print(f"Elemento {key} encontrado na posição {h}")
    else:
        print("Elemento não encontrado")
        
while True:
    print("\n1. Inserir\n2. Buscar\n3. Imprimir tabela\n4. Sair")
    opc = int(input("\nDigite uma opção: "))

    if opc == 1:
        key = int(input("\nDigite um valor para inserir: "))
        insertKey(key)

    elif opc == 2:
        key = int(input("\nDigite um valor para buscar: "))
        findKey(table, key)

    elif opc == 3:
        print(table)

    elif opc == 4:
        break