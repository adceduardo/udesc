with open("usuarios.txt", "r") as archive:
    print("-" * 45)
    print(f"{'Nome':<20}{"Idade":<10}{"Cidade":<15}")
    print("-" * 45)

    for line in archive:
        user = line.strip().split(",")
        print(f"{user[0]:<20}{user[1]:<10}{user[2]:<15}")

