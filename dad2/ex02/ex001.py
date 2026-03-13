
words_to_find = []
while True: 
    word_to_find = input("\nDigite quais palavas deseja contar a ocorrência ou 5 para sair: ")

    if word_to_find == "5":
        break 

    words_to_find.append(word_to_find)

ocurrences = {}

with open("arquivo.txt", "r") as archive:
    for line in archive:
        words = line.split()

        for word in words_to_find:         
            if not word in ocurrences:
                ocurrences[word] = words.count(word)

            else:
                ocurrences[word] += words.count(word)
             

print(ocurrences)
   
# if(ocurrences < 1 ):
#     print("A palavra não foi encontrada nenhuma vez")

# if(ocurrences > 0):
#     print(f"A palavra foi encontrada {ocurrences} vezes")