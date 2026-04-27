table = [None] * 5

def insertKey(key):
    squared = key ** 2
    s = str(squared)
    middle = len(s)//2
    print("Divisão: ", middle)
    h = s[middle-1:middle+1]  
    print(f"Meio: {h}")

    h = int(h) % len(table)
    print(f"Hash gerado: {h}")

    if table[h] == None:
        table[h] = key
        print(f"\nKey {key} inserida na posição {h}")

    elif type(table[h]) == int :
        print("Já existe um elemento nesta posição, inserindo valor na sequência")
        arr = []
        arr.append(table[h])
        arr.append(key)

        table[h] = arr
    
    else:
        print("Nesta posição já exite uma lista, fazendo o append")
        table[h].append(key)


while True:
    print("\n1. Inserir\n2. Imprimir tabela\n3. Sair")
    opc = int(input("\nDigite uma opção: "))

    if opc == 1:
        key = int(input("\nDigite um valor para inserir: "))
        insertKey(key)
        print(table)

    elif opc == 2:
        print(table)

    elif opc == 3:
        break