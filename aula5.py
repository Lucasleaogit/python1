capacidade = int(input("Capacidade máxima da oficina: "))
inscritos = int(input("Pessoas já inscritas: "))
pedido = int(input("Quantidade de vagas solicitadas: "))

if inscritos + pedido <= capacidade:
	print("Pedido inteiro confirmado.")
else:
	print("Pedido não confirmado.")
	
print("Capacidade máxima da oficina:", capacidade)
print("Pessoas já inscritas:", inscritos)
