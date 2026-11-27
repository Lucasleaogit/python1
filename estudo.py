dia = 1
total = 0
diaComMeta = 0

while dia <= 3:
    print(f'Dia {dia}')
    diaComMeta += int(input('Digite o total de minutos estudados: '))
    if diaComMeta == 20 or diaComMeta > 20:
        print('Meta atingida!')
        dia += 1
    else:
        print('Meta não atingida.')
        dia += 1

total = total + diaComMeta

if total == 60:
    print('Parabéns! Você atingiu a meta de 60 minutos de estudo.')
elif total > 60:
    print(f'Parabéns! Você estudou um total de {total} minutos, ultrapassando a meta de 60 minutos.')
else:
    print(f'Você estudou um total de {total} minutos. Continue se esforçando para atingir a meta de 60 minutos.')
