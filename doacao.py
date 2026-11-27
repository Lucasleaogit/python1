TotalItens = 0
Doacoes = 0
NumDoacao = 1

while numDoacao <= 4:
    print(f"Doação {numDoacao} de 4")
    quantidade = int(input("Digite a quantidade de itens doados: "))
    totalItens = totalItens + quantidade

    if quantidade > 10:
        doacoes = doacoes + 1

    numDoacao = numDoacao + 1
print("\nResumo das doações")
print(f"Total de itens doados: {totalItens}")
print(f"Total de doações com mais de 10 itens: {doacoes}")

if totalItens == 40:
    print("Parabéns! Você atingiu a meta de doações!")
elif totalItens > 40:
    print("Parabéns! Você ultrapassou a meta de doações!")
else:
    print("Você não atingiu a meta de doações. Continue participando!")