#Criando os aqruivos bin:

with open ("dados1.bin", "wb") as archive:
    archive.write(b'\x42\x69\x6e\x61\x72\x69\x6f')

with open("dados2.bin", "wb") as archive:
    archive.write(b'\x42\x69\x6e\x61\x72\x69\x6f\x48')


with open("dados1.bin", "rb") as archive1:
    data1 = archive1.read()

with open("dados2.bin", "rb") as archive2:
    data2 = archive2.read()

size_data = min(len(data1), len(data2))

find = False

for i in range(size_data):
    if data1[i] != data2[i]:
        find = True       
        break

if find == True:
    print(f"\nOs arquivos são diferentes e a primeira diferença está na posição: {i}")

elif len(data1) != len(data2):
    print(f"\nOs arquivos são diferentes e a primeira diferença está na posição {size_data}")
else:
    print("\nOs arquivos são iguais")