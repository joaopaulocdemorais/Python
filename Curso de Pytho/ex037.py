n = int(input('Informe um número inteiro: '))
print('-=-'*10, 'MENU', '-=-'*10)
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
op = int(input('Sua Opção: '))
if op == 1:
    conv = bin(n)[2:]
    text = "BINÁRIO"
elif op == 2:
    conv = oct(n)[2:]
    text = 'OCTAL'
elif op == 3:
    conv = hex(n)[2:]
    text = 'HEXADECIMAL'
else:
    print('Opção invalida, tente novamente !')
    conv = 'null'
    text = 'null'

print('{} convertido para {} é igual a {}'.format(n, text, conv))