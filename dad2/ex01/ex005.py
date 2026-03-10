line_amount = 0
word_amount = 0

with open("lorem_ipsum.txt", "r") as archive:
    for line in archive:
        words = line.split()
        word_amount +=len(words)
        line_amount+=1

print("Quantidade de linhas: ", line_amount)
print("Quantidade de palvaras: ", word_amount)
