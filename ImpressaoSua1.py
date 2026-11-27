totalPaginas = 0
solicitacoesCom20OuMais = 0
numeroSolicitacao = 1

while numeroSolicitacao <= 4:
    print(f"Solicitação Numero : {numeroSolicitacao}°")
    paginas = int(input("Digite a quantidade de páginas: "))

    totalPaginas = totalPaginas + paginas

    if paginas >= 20:
        solicitacoesCom20OuMais = solicitacoesCom20OuMais + 1

print(f"Total de páginas: {totalPaginas}")
print(f"Solicitações com 20 páginas ou mais: {solicitacoesCom20OuMais}")

if totalPaginas <= 100:
    print("Dentro do limite")
else:
    print("Acima do limite")