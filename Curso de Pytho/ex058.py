from random import randint
print('Sou o seu computador...')
n = randint(0,10)
print('Acabri de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar que foi ?')
t = 0
c = 0
while t == 0:
    p = int(input('Qual é seu palpite ?'))
    c = c + 1
    if n > p:
        print('Mais... Tente mais uma vez')
    elif n < p:
        print('Menos... Tente mais uma vez')
    else:
        t = 1
print('Acertou com {} tentativas. Parabéns!'.format(c))


