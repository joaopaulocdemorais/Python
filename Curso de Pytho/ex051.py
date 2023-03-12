print('='*30)
print('10 TERMOS DE UM PA'.center(30))
print('='*30)
p = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = p + (10-1) * razao
for c in range(p, decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('acabou !!!!')