galera = list()
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome:'))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['Sexo'] in 'MmFf':
            break
        else:
            print('Erro! Informe M para masculino ou F para feminino.   ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        sair = str(input('Deseja cadastrar mais uma pessoa? [S/N]')).upper()[0]
        if sair in 'SN':
            break
        print('ERRO!, informe S para sim ou N para não.')
    if sair == 'N':
        break
print('---'*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas!')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) O nome das mulheres cadastradas são: ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] > media:
        print(f'{p["Nome"]} ', end='')
print('<<ENCERRADO>>')
