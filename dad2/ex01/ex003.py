name = input("\nDigite seu nome: ")
age = input("\nDigite sua idade: ")
city = input("\nDigite sua cidade: ")

with open("usuarios.txt", "a") as archive:
    archive.write(f"\n{name}, {age}, {city}")
