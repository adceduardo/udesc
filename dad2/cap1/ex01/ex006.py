# Para via de testes irei usar o arquivo "lorem_ipsum.txt" e a palvara de teste será: dado

word_to_find = input("Digite a palavra que deseja encontrar: ")
occurrences = 0

with open("lorem_ipsum.txt", "r") as archive:
    for line in archive:
        word = line.split()

        if word_to_find in word:
            occurrences += word.count(word_to_find)

if(occurrences < 1):
    print(f"A palavra {word_to_find} não foi encontrada nenhuma vez")

else:
    print(f"A palvra {word_to_find} foi encontrada {occurrences} vezes")


