import tempfile
events_amount = int(input("\nQuantos eventos deseja registrar?: "))
save = input("\nDeseja salvar o log permanentemente? (s/n) ")

if save == "s":
    delete_archive = False
else:
    delete_archive = True

with tempfile.NamedTemporaryFile(delete=delete_archive) as temp:
    for i in range(events_amount):
        content = f'Log {i+1}\n'
        temp.write(content.encode())   
  
    if save == "s":
        with open("logs.txt", "w") as archive:
            temp.seek(0)
            archive.write(temp.read().decode())



