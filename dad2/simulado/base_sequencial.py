def Create(plate, year):
    with open("VEICULOS.TXT", "a+") as archive:
        archive.seek(0)
        content = archive.readline() 

        if not content:
            archive.write("0\n")
       
    with open("VEICULOS.TXT", "r+") as archive:
        archive.seek(0)
        content = archive.readline()
        id = int(content) + 1
        archive.seek(0)
        archive.write(f'{id}\n')
        archive.seek(0, 2)
        archive.write(f' ;{id};{plate};{year}\n')

def Delete(idForDelete):
    with open("VEICULOS.TXT", "r+") as archive:
        archive.readline()
        
        while True:
            pos = archive.tell()
            line = archive.readline()

            if not line:
                break

            if line.startswith(' '):
                gravestone = line.split(";")
               
                if int(gravestone[1]) == int(idForDelete):
                    
                    archive.seek(pos)
                    archive.write("*")
                    return True
                
def Update(id, plate):
    with open("VEICULOS.TXT", "r+") as archive:
        archive.readline()

        while True:
            pos = archive.tell()
            line = archive.readline()

            if not line:
                break

            if line.startswith(" "):
                register = line.split(";")

                if register[1] == id:
                    if len(plate) <= len(register[2]):
                        newplate = plate.ljust(len(register[2]))
                        newRegister = ";".join([register[0], register[1], newplate, register[3]])
                        archive.seek(pos)
                        archive.write(newRegister)
             
                    else:
                        newRegister = ";".join([register[0], register[1], plate, register[3]])
                        archive.seek(pos)
                        archive.write("*")
                        archive.seek(0,2)
                        archive.write(newRegister)

def List():
    with open("VEICULOS.TXT", "r") as archive:
        archive.readline()

        print(f"\n{'ID':<5}{'Placa':<10}Ano")
        print("-" * 20)
        while True:
            line = archive.readline()

            if not line:
                break

            if line.startswith(" "):
                content = line.split(";")
                
                print(f"{content[1]:<5}{content[2]:<10}{content[3]}")

                

while True:
    print("\n1. Listar\n2. Inserir\n3. Alterar\n4. Deletar\n5. Sair")

    try:
        opc = int(input("\nDigite uma opção: "))

        if opc == 1:
            List()

        elif opc == 2:
            plate = input("\nDigite a placa do veículo: ")
            year = input ("\nDigite o ano do veículo: ")
            Create(plate, year)

        elif opc == 3:
            id = input("\nDigite qual id deseja alterar: ")
            plate = input("\nDigite a nova placa: ")
            Update(id, plate)

        elif opc == 4:
            id = input("\nDigite qual id deseja deletar: ")
            Delete(id)

        elif opc == 5:
            break

        else:
            print("\nDigite uma opção válida")
    
    except ValueError:
        print("Erro", ValueError)


