docs = {
    1: "Sei que sou",
    2: "Sou o que sei",
    3: "Sou especial"
}

output = {}

for key, text in docs.items():
    
    for word in text.split():
        formated_word = word.lower()

        if not formated_word in output:
            output[formated_word] = [key]

        else:
            output[formated_word].append(key)


for key, value in output.items():
    print(f"{key}: {value}")