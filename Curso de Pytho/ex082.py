lista = []
listaPar = []
listaImpar = []

while True:
    lista.append(int(input('Digite um número: ')))
    if input('Deseja continuar: [S/N] ') in 'nN':
        break
for n in lista:
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)

print('----' * 30)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {listaPar}')
print(f'A lista de ímpares é: {listaImpar}')