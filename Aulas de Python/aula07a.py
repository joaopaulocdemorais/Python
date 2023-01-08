n1 = int(input('Informe o primeiro numero ? '))
n2 = int(input('Informe o segundo numero ?'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n a produto é {} \ne a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
