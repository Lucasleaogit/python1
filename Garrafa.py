ponto = 1
total = 0

while ponto <= 3:
    print(f"Registrando ponto {ponto}")
    quantidade = int(input("Digite a quantidade de garrafas no ponto: "))
    total += quantidade
    ponto += 1

print(f"Total de garrafas nos pontos: {total}\n")
print("Conferência concluída.\n")