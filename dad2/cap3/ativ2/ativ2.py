import re

doc1 = "doc1.txt"
doc2 = "doc2.txt"
doc3 = "doc3.txt"

def createInvertedList(archive, docID):    
    with open(archive, 'r', encoding="utf-8") as file:
        pos = 0
        stopWords = {"a", "e", "o", "da", "de", "do"}
        
        for line in file:
            for word in line.split():
                pos += 1
                formatted = re.sub(r'\W+', '', word.lower())

                if formatted in stopWords:
                    continue

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

def printResult(output):
    for word, data in output.items():
        print("-"*48)
        result = (f"Palava: {word}\nResultados encontrados:\n")
       
        for value in data:
            strPos = ", ".join(map(str, value[1]))
            result+=(f"Documento -> {value[0]} posições: {strPos}\n")
            
        
        print(result)
    
def simpleFind( word):
    output = {}
    temp = baseFind(word)
    
    if len(temp) > 0:
        output[word] = temp
        printResult(output)

    else:
        print("Nenhuma ocorrência encontrada")

def conjuntFind(words):
    output = []
    resultBaseFind = []

    for word in words:
        temp = baseFind(word)
        if len(temp) == 0:
            print(f"Palavra {word} não encontrada no dicionário")
            return
        
        else:
            resultBaseFind.append(temp)
            docs = set()
            
            for docID, pos in temp:
                docs.add(docID)

            output.append(docs)

    
    docs = output[0]  
    for element in output[1:]:
       docs = element.intersection(docs)

    
    output = {}
    
    for i, data in enumerate(resultBaseFind):
        for docID, pos in data:

            if docID in docs:
                if not words[i] in output:
                    output[words[i]] = []
                
                output[words[i]].append((docID, pos))
    
    
    printResult(output)
                        
def disjuntFind(words):
    output = {}

    for word in words:
        temp = baseFind(word)
        if len(temp) == 0:
            print(f"\nPalavra {word} não encontrada no dicionário")
            continue
        
        else:
            for docID, pos in temp:
                if not word in output:
                    output[word] = []
                
                output[word].append((docID, pos))  

    printResult(output)

def printList():
    for word, data in index.items():
        print(word, data)

###############################

index = {}
docs = [doc1, doc2, doc3]
for i, doc in enumerate(docs):
    createInvertedList(doc, i+1)

while True:
    try:
        print("\n")
        print("-"*12, "MENU DE BUSCAS", "-"*12)
        print("1. Simples\n2. Conjuntiva\n3. Disjuntiva\n4. Imprimir lista\n5. Sair")

        opc = int(input("\nDigite a opção desejada: "))

        if opc == 1:
            wordToFind = str(input("\nDigite qual palavra deseja buscar: "))
            simpleFind(wordToFind)

        elif opc == 2:
            wordToFind = str(input("\nDigite quais palavras deseja buscar: "))
            wordToFind = wordToFind.split()
            conjuntFind(wordToFind)

        elif opc == 3:
            wordToFind = str(input("\nDigite quais palavras deseja buscar: "))
            wordToFind = wordToFind.split() 
            disjuntFind(wordToFind)
        
        elif opc == 4:
            printList()

        elif opc == 5:
            break

    except:
        print("\nDigite uma opção válida")




