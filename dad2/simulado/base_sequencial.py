def create(plate, year):
    with open("VEICULOS.TXT", "a+") as archive:
        archive.seek(0)
        content = archive.readline() 

        if not content:
            archive.write("0\n")
       

    with open("VEICULOS.TXT", "r+") as archive:
        archive.seek(0)
        content = archive.readline()
        id = int(content) + 1
        print(id) #so para fins de debug mesmo depois eu tiro

        archive.seek(0)
        archive.write(f'{id}\n')
        archive.seek(0, 2)
        archive.write(f';{id};{plate};{year}\n')



create('4b97', 2022)
create('4b98', 2024)
create('4b99', 2011)
       

