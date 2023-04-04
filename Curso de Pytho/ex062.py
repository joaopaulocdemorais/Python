print('GERADOR DE PA')
print('-='*10)
Ptermo = int(input('Primero termo: '))
razão = int(input('Razão da PA: '))

for c in range(1,11):
    print('{} -> '.format(Ptermo), end='')
    Ptermo = Ptermo + razão
print('Pausa')
cont = 1
cont2 = 0
quantidade = 10
while cont !=0:
    cont = int(input('Quantos termo você que mostrar a mais: '))
    while cont2 < cont:
        print('{} -> '.format(Ptermo), end='')
        Ptermo = Ptermo + razão
        cont2 += 1
    cont2 = 0
    quantidade = quantidade + cont
    print('Pausa' if cont !=0 else '')
print('Progressão finalizada com {} termos mostrados.'.format(quantidade))