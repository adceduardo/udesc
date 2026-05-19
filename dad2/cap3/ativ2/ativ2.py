doc1 = "doc1.txt"
doc2 = "doc2.txt"
doc3 = "doc3.txt"

def createInvertedList(archive, docID):
    with open(archive, 'r') as file:
        pos = 0
        
        for line in file:
            for word in line.split():
                pos += 1
                formatted = word.lower()

                if not formatted in index:
                    index[formatted] = [(docID, [pos])]
                
                else:
                    add = False
                    
                    for i in index[formatted]:

                        if i[0] == docID:
                            i[1].append(pos)
                            add = True
                        
                    if not add:
                        index[formatted].append((docID, [pos]))

def baseFind(word):
    if word in index:
       return index[word]
   
    return []
    
def simpleFind( word):
    output = baseFind(word)

    if len(output) > 0:
        print("-"*32)
        print(f"Resultados para a palavra {word}: ")

        for docID, pos in output:
            freq = len(pos)
            strPos = ", ".join(map(str, pos))
            print(f"Documento {docID} -> {freq} ocorrência(s) encontrada(s) nas posições: {strPos}")
    else:
        print("Nenhuma ocorrência encontrada")

def andFind(words):
    output = []

    for word in words:
        temp = baseFind(word)
        if len(temp) == 0:
            print(f"Palavra {word} não encontrada no dicionário")
            return
        
        else:
            output.append(temp)
        
    docs = []
    for element in output:
        print(element)



    
    


       



##################

index = {}
docs = [doc1, doc2, doc3]
for i, doc in enumerate(docs):
    createInvertedList(doc, i+1)

while True:
    print("\n")
    print("-"*12, "MENU", "-"*12)
    print("1. Simples\n2. Conjuntiva\n3. Disjuntiva\n4.Sair")

    #opc = int(input("\nDigite qual opção de busca deseja realizar: "))
    opc = 2

    if opc == 1:
        wordToFind = str(input("\nDigite qual palavra deseja buscar: "))
        simpleFind(wordToFind)
        

    elif opc == 2:
        #wordToFind = str(input("\nDigite as palavras que deseja encontrar: "))
        #wordToFind  = wordToFind.split()
        andFind(['python', 'dados'])
        break

    elif opc == 3:
        pass
    
    elif opc == 4:
        break




