name = input(("Digite seu nome: "))

with open("nome.txt", "w") as archive:
    archive.write(name)
