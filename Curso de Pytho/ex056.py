nome = ''
idade = 0
sexo = ''
somaidade = 0
idadeMaisVelho = 0
nomeMaisVelho = ''
mulher20 = 0
for p in range(1,5):
    print('-'*5,'{}ª PESSOA'.format(p),'-'*5)
    nome = input('NOME: ').strip()
    idade = float(input('IDADE:'))
    sexo = input('SEXO [M/F]: ').strip()
    somaidade = somaidade + idade
    if (sexo == 'f' or sexo == 'F') and idade < 20:
        mulher20 = mulher20 + 1
    if p == 1 and (sexo =='M' or sexo == 'm'):
        idadeMaisVelho = idade
        nomeMaisVelho = nome
    else:
        if idadeMaisVelho < idade and sexo in 'Mm':
            idadeMaisVelho = idade
            nomeMaisVelho = nome

print('A média de idade do grupo é de {:.2f} anos'.format(somaidade /p))
print('O homen mais velho tem {} anos e se chama {}.'.format(idadeMaisVelho, nomeMaisVelho))
print('Temos no total {} mulheres com menos de 20 anos'.format(mulher20))