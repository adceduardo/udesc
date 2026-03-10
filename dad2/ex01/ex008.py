def saveContact(name, phone):
    with open("contatos.txt", "a") as archive:
        archive.write(f"{name},{phone}\n")
    
    print("\nContato salvo com sucesso!")

def listContacts():
    with open("contatos.txt", "r") as archive:
        print(archive.readlines())

def searchContact(name):
    list = []

    with open("contatos.txt", "r") as arquive:
        for line in arquive:
            if name in line:
                list.append(line)

        if len(list) < 1:
            print("\nNenhum contato encontrado")
        
        else:
            print(list)

while True:
    print("\nMenu: ")
    print("1. Adicionar Contato\n2. Listar contatos \n3. Buscar contato \n4. Sair")
    
    opc = int(input("\nDigite uma opção: "))
    
    if opc == 1:
        name = input("\nDigite o nome do contato: ")
        phone = input("\nDigite o telefone: ")
        saveContact(name, phone)

    elif opc == 2:
        listContacts()

    elif opc == 3:
        name = input("\nDigite o nome que deseja encontrar: ")
        searchContact(name)

    elif opc == 4:
        break