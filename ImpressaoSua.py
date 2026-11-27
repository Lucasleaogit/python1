
LIMITE = 100
TOTAL_SOLICITACOES = 4
PAGINAS_ESPECIAL = 20

total_paginas = 0
qtd_especiais = 0
solicitacao = 1

while solicitacao <= TOTAL_SOLICITACOES:
    print(f"Solicitação {solicitacao}")
    paginas = int(input("Quantidade de páginas: "))
    total_paginas += paginas
    if paginas >= PAGINAS_ESPECIAL:
        qtd_especiais += 1
    solicitacao += 1

print()
print(f"Total de páginas: {total_paginas}")
print(f"Solicitações com 20 páginas ou mais: {qtd_especiais}")
if total_paginas <= LIMITE:
    print("Dentro do limite")
else:
    print("Acima do limite")
print("Registro encerrado")