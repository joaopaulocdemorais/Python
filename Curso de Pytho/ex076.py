listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 34.90)

print('-' * 40)
print(f'LISTAGEM DE PREÇO'.center(40))
print('-' * 40)
for p in range(0 ,len(listagem)):
   if p % 2 == 0:
       print(f'{listagem[p]:.<30}', end='')
   else:
       print(f'R$ {listagem[p]:>5.2f}')
print('-' * 40)