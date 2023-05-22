listageral = []
listaPar = []
listaImpar = []

for c in range(1,8):
    n = int(input(f'Informe o {c}º numéro:'))
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)

listageral.append(listaImpar)
listageral.append(listaPar)

print(f'Os numeros impares são {sorted(listageral[0])}')
print(f'Os numeros pares são {sorted(listageral[1])}')