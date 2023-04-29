soma = 0
cont = 0
while True:
    n = int(input('Digite uma valor: (999 para parar):'))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} valores foi {soma}! ')
