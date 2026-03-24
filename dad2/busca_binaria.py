vet = [2, 4, 6, 8, 10, 12, 14]

def busca(valor, lista):
    inicio = 0
    fim = len(lista)-1
    meio = (inicio + fim) // 2

    while inicio <= fim:
        if lista[meio] == valor:
           print('achou', lista[meio])
           break
       
       
        if lista[meio] > valor:
           fim = meio - 1
           print('novo fim' , fim)
        else:
            inicio = meio + 1
            print('novo inici', inicio)
        
        meio = (inicio + fim) // 2
        print('novo meio', meio)
           

busca(14, vet)