table = [None] * 11

def insertKey(key):
    h = key % len(table)

    if not table[h]:
        table[h] = key
        print(f"Elemento {key} inserido na posição {h}")

    else:
        for i in range(1, len(table)):
            aux = (h+i) % len(table)

            print(f"Colisão com {h}, tentando inserir em {aux}")
        
            if not table[aux]:
                table[aux] = key
                print(f"Elemento {key} inserido na posição {aux}")
                return
            
        print("\nLista cheia, impossível inserir mais itens")
        

while True:
    print("\n1. Inserir\n2. Imprimir tabela\n3. Sair")
    opc = int(input("\nDigite uma opção: "))

    if opc == 1:
        key = int(input("\nDigite um valor para inserir: "))
        insertKey(key)

    elif opc == 2:
        print(table)

    elif opc == 3:
        break