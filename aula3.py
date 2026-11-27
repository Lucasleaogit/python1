participantes = int(input("Insira o número de participantes: "))
precoDoCracha = float(2.5)
precoDoLanche = float(7.5)
Orcamento = float(input("Insira o orçamento disponível: "))
precoDoEvento = (precoDoCracha + precoDoLanche) * participantes

print("O preço pra entrar é", precoDoCracha + precoDoLanche)
print("O preço do evento é", precoDoEvento)
if Orcamento > precoDoEvento:
    print("O orçamento é suficiente para o evento.")
elif Orcamento == precoDoEvento:
    print("O orçamento é suficiente para o evento, mas não sobra dinheiro.")
else:
    print("O orçamento não é suficiente para o evento.")
