numeros = []
maior = 0
menor = 0
for n in range(0,5):
    numeros.append(int(input(f'Digite um valor para Posição {n}:')))
    if n == 0:
        maior = menor = numeros[n]
    if numeros[n] > maior:
        maior = numeros[n]
    if numeros[n] < menor:
        menor = numeros[n]
print('-='*30)
print(f'Você digitou os valores: {numeros}')
print(f'O menor número digitado foi: {menor}, encontrados nas posições: ', end='')
for i ,v in enumerate(numeros):
    if menor == v:
        print(f'{i}...',end='')

print(f'\nO maior número digitado foi: {maior}, encontrados nas posições: ', end='')
for i ,v in enumerate(numeros):
    if maior == v:
        print(f'{i}...',end='')