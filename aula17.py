cadastro_ativo = int(input("Cadastro ativo? (1 para sim, 0 para não): "))
treinamento_concluido = int(input("Treinamento concluído? (1 para sim, 0 para não): "))
equipamento_com_defeito = int(input("Equipamento com defeito? (1 para sim, 0 para não): "))
revisao_vencida = int(input("Revisão vencida? (1 para sim, 0 para não): "))

requisitos_atendidos = cadastro_ativo == 1 and treinamento_concluido == 1
manutencao_indicada = equipamento_com_defeito == 1 or revisao_vencida == 1

print("\nResultado do solicitante:")
if requisitos_atendidos:
	print("Os requisitos do solicitante são atendidos.")
else:
	print("Os requisitos do solicitante não são atendidos.")

print("\nResultado do equipamento:")
if manutencao_indicada:
	print("Encaminhar o equipamento para manutenção.")
else:
	print("Não há indicação de manutenção pela regra.")
