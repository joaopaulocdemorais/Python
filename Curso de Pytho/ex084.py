temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if maior < temp[1]:
            maior = temp[1]
        if menor > temp[1]:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    if input('Quer continuar? [S/N] ') in 'nN':
        break

print(f'Os dados foram {princ}')
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior} Kg. Sendo eles: ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menos peso foi de {menor} Kg. Sendo eles: ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()