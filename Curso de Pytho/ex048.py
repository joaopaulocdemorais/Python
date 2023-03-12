n = int(input('Informe um número? '))
soma = 0
quantidade = 0
for c in range(1, n+1):
    if c % 2 == 1:
        if c % 3 == 0:
            print(c)
            soma = c + soma
            quantidade += 1
print('Foram encontrados {} valores e a soma de todos os valores e {}'.format(quantidade, soma))