from random import randint
números = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print('Os valores sorteados foram: ', end='')
for n in números:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi: {max(números)}')
print(f'O menor valor sorteado foi: {min(números)}')