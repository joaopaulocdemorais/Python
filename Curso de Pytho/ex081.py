l = list()
cont = 0
while True:
    l.append(int(input('Informe um valor:')))
    cont += 1
    if input('Deseja continuar: [S/N]').strip() in 'nN':
        break
print('---'*30)
print(f'Você digitou {cont} elementos.')
print(f'O valores em ordem decrescentre {sorted(l,reverse=True)}')
if 5 in l:
    print('O Valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado.')