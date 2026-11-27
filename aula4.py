saldo = 50
valorDaCompra = float(input("Digite o valor da compra:"))
 
print("O saldo disponível é:", saldo)
print("O valor da sua compra foi de:", valorDaCompra)
if valorDaCompra <= saldo:
    print("Seu saldo é de:", saldo - valorDaCompra)
else:
    print("Saldo indisponível")