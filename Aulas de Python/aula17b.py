valores = []
for i in range(0, 5):
    valores.append(int(input('Valor:')))

print(valores)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')