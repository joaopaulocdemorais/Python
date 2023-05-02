tot18 = toth = totm20 = 0
condição = 'S'
while True:
    if condição == 'S':
        print('-' * 30)
        print('CADASTRE UM PESSOA')
        print('-' * 30)
        idade = int(input('Idade:'))
        Sexo = ' '
        while Sexo not in 'MF':
            Sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
        if idade >= 18:
            tot18 += 1

        if Sexo == 'M':
            toth += 1

        if Sexo == 'F' and idade < 20:
            totm20 += 1

    else:
        break
    print('-' * 30)
    condição = ' '
    while condição not in 'SN':
        condição = str(input('Quer continuar? [S/N]')).strip().upper()[0]
print(f'Total de pessoas com mais 18 ano: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'E temos {totm20} mulheres com menos de 20 anos')