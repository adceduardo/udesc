docs = {
    1: "Sei que sou",
    2: "Sou o que sei, sou",
    3: "Sou especial"
}

output = {}

for key, text in docs.items():
    
    for position, word in enumerate(text.split()):
        formated_word = word.lower()

        if not formated_word in output:
            output[formated_word] = [(key, position+1)]
            

        else:
            output[formated_word].append((key, position+1))
         

for key, value in output.items():
    print(f"{key}: {value}")