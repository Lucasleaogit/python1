qtdeCadernos = int(input("Digite a quantidade de cadernos: "))
if qtdeCadernos <= 4:
    print("O produto tem valor abaixo do necessario para desconto.")
elif qtdeCadernos >= 5 and qtdeCadernos <= 9:
    desconto = (20 * qtdeCadernos) * 0.10
    valor_com_desconto = (20 * qtdeCadernos) - desconto
    print(f"O produto tem um desconto de 10%. Valor com desconto: R${valor_com_desconto:.2f}")
else:
    desconto = (20 * qtdeCadernos) * 0.15
    valor_com_desconto = (20 * qtdeCadernos) - desconto
    print(f"O produto tem um desconto de 20%. Valor com desconto: R${valor_com_desconto:.2f}")

