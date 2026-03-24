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
        archive.write(f';{id};{plate};{year}\n')

def Delete(idForDelete):
    with open("VEICULOS.TXT", "r+") as archive:
        header = archive.readline()
        
        while True:
            pos = archive.tell()
            print('pos', pos)
            line = archive.readline()
           

            if not line:
                break

            gravestone = line.split(";")
            print('grave', gravestone)

            if int(gravestone[1]) == int(idForDelete):
                print("batatinha")
                archive.seek(pos)
                archive.write("*")

            



Create('4b97', 2022)
Create('4b98', 2024)
Create('4b99', 2011)

Delete(1)
       

