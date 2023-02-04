a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))
# buscando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# buscando o maior número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor numero informado foi {}'.format(menor))
print('O maior número informado foi {}'.format(maior))
