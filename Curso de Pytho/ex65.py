ctr = 'S'
cont = soma = 0
maior = 0
menor = 0
while ctr == 'S':
    n = int(input('Digite um número: '))
    if maior == 0 and menor == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    ctr = str(input('Quer continuar ?')).upper().strip()
    cont += 1
    soma += n
print('Você digitou {} números e média foi {:.2f}'.format(cont, soma/cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))