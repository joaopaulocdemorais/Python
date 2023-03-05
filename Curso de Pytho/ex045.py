from random import randint
from time import sleep
print('''SUAS OPÇÕES:
[1] PEDRA 
[2] PAPEL
[3] TESOURA''')
jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
opc = int(input('Qual e sua jogada ?'))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
sleep(1)
opcc = randint(1,3)
if opc == opcc:
    resultado = 'EMPATE'
elif (opc == 1 and opcc == 3) or (opc == 2 and opcc == 1) or (opc == 3 and opcc == 2):
    resultado = 'O JOGADOR GANHOUUUU!!!!!'
else:
    resultado = 'O COMPUTADOR GANHOU!'
print('='*40)
print('O computador jogou {}'.format(jogadas[opcc - 1]))
print('O Jogador jogou {}'.format(jogadas[opc - 1]))
print('='*40)
print(resultado)

