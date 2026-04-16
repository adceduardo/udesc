output = []

with open("produtos.txt", "r", encoding="utf-8") as archive:
    for line in archive:
        product = line.split(",")
        name = product[0]
        price = float(product[1]) 
        amount = int(product[2])
        total = price * amount
        output.append([name, price, amount, total])

print("\nRelatório de estoque: \n")
print(f"{'Produto':<20}{'Preço':<15}{'Quantidade':<15}Total")
print("-" * 60)

for product in output:
    print(f"{product[0]:<20}{'R$':<3}{product[1]:<12.2f}{product[2]:<15} R$ {product[3]:.2f}")