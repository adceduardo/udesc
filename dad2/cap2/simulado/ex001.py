table = [None] * 17

def insertKey(key):
    h = key % len(table)

    if table[h] is None:
        table[h] = key
        print(f"Elemento {key} inserido na posição {h}")

    else:
        for i in range(1, len(table)):
            aux = (h+i) % len(table)

            print(f"Colisão com {h}, tentando inserir em {aux}")
        
            if table[aux] is None:
                table[aux] = key
                print(f"Elemento {key} inserido na posição {aux}")
                return
            
        print("\nLista cheia, impossível inserir mais itens")
        

# while True:
#     print("\n1. Inserir\n2. Imprimir tabela\n3. Sair")
#     opc = int(input("\nDigite uma opção: "))

#     if opc == 1:
#         while True:
#             key = int(input("\nDigite um valor para inserir ou 0 para sair: "))
            
#             if key == 0:
#                 break

#             insertKey(key)

#     elif opc == 2:
#         print(table)

#     elif opc == 3:
#         break

values = [120, 130, 140, 100, 101, 77, 88, 99, 47, 117, 23, 68]

for v in values:
    insertKey(v)

print(table)