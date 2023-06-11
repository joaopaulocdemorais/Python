def area(l ,c):
    a = l * c
    return a


print('Controle de Terrenos')
print('---------------------')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
print(f'A área de um terreno {l} x {c} é de {area(l, c):.2f}m² ')