def saveContact(name, phone):
    with open("contatos.txt", "a") as archive:
        archive.write(f"{name},{phone}\n")
    
    print("\nContato salvo com sucesso!")

def listContacts():
    try:
        with open("contatos.txt", "r") as archive:
            print(f"\n{'Nome':<15}{'Telefone'}")
            print("-" * 28)
            
            for line in archive:
                contact = line.strip().split(",")
                print(f"{contact[0]:<15}{contact[1]}")
    except:
        print("\nAdicione um contato antes de consultar a lista")

def searchContact(name):
    try:
        list = []
        with open("contatos.txt", "r") as arquive:
            for line in arquive:
                if name.lower() in line.lower():
                    print(line)
                    list.append(line.split(",")) 

            if len(list) < 1:
                print("\nNenhum contato encontrado")
            
            else:
                print(f"\n{'Nome':<15}{'Telefone'}")
                print("-" * 28)
                
                for contact in list:
                    print(f"{contact[0]:<15}{contact[1]}")
    except:
         print("\nAdicione um contato antes de consultar a lista")

while True:
    print("\nMenu: ")
    print("1. Adicionar Contato\n2. Listar contatos \n3. Buscar contato \n4. Sair")
    
    opc = input("\nDigite uma opção: ")
    
    if opc == "1":
        name = input("\nDigite o nome do contato: ")
        phone = input("\nDigite o telefone: ")
        saveContact(name, phone)

    elif opc == "2":
        listContacts()

    elif opc == "3":
        name = input("\nDigite o nome que deseja encontrar: ")
        searchContact(name)

    elif opc == "4":
        break
    
    else:
        print("\nDigite uma opção válida")