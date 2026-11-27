distancia = float(input("Digite a distância em Quilometros: "))

if distancia <= 5:
    print("O valor do frete é R$ 8,00")
elif distancia <= 10:
    print("O valor do frete é R$ 12,00")
else:
    print("O valor do frete é R$ 18,00")

