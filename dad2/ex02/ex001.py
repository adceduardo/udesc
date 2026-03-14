
words_to_find = []
while True: 
    word_to_find = input("\nDigite qual palava deseja contar a ocorrência ou 5 para sair: ")

    if word_to_find == "5":
        break 

    words_to_find.append(word_to_find)


if len(words_to_find) > 0:  
    ocurrences = {}

    for key in words_to_find:
        ocurrences[key] = 0

    with open("arquivo.txt", "r") as archive:
        for line in archive:
            words = line.split()

            for word in words:
                if word in words_to_find:
                    ocurrences[word] += 1

    ocurrences_sorted = sorted(ocurrences.items(), key=lambda position: position[1], reverse=True)   
    
    print("-" * 30)
    print("Ocorrência de palavras: ")
    print("-" * 30)
    print(f"{'Palavra':<20}Quantidade")
    print("-" * 30)

    for word, amount in ocurrences_sorted:
        print(f"{word:<20}{amount}")
    print("\n")