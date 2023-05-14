numeros = []
while True:
    valor  = int(input('Digite im valor: '))
    if valor in numeros:
        print('Valor duplicado! Não vou adicionar.')
    else:
        numeros.append(valor)
        print('Valor adicionado com sucesso...')

    if 'S' != input('Quer continuar ? [S/N]').strip().upper():
        break
print('-'*60)
print(f'Você digitou os valores {sorted(numeros)}')