computador = 1

while computador <= 3:
    print(f"Registrando computador {computador}")
    funcionamento = int(input("Digite 1 se o computador está funcionando ou 0 se não está: "))

    if funcionamento == 1:
        print(f"Computador {computador} está funcionando.")
    else:
        print(f"Computador {computador} não está funcionando.")

    computador += 1

print("Conferência concluída.\n")
