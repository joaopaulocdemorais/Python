matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
somaPar = 0
somaTerceiraColuna = 0
maiorSegundalinha = 0
for l in range(0,3):
    for c in range(0, 3):
        matriz [l][c] = int(input(f'Digite um valor para posição [{l}][{c}]: '))

print('---'*30)
for l in range(0 , 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^6}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        if c == 2:
            somaTerceiraColuna += matriz[l][c]
        if l == 1:
            if c == 0 or matriz[l][c] > maiorSegundalinha:
                maiorSegundalinha = matriz[l][c]
    print()
print('---'*30)
print(f'A soma dos valores pares é: {somaPar}')
print(f'A soma dos valores da Terceira coluna são: {somaTerceiraColuna}')
print(f'O maior valor da segunda linha è: {maiorSegundalinha}' )
