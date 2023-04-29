from random import randint
cont = 0
while True:
    print('-=-' * 15)
    print('VAMOS JOGARG PAR OU ÍMPAR')
    print('-=-' * 15)
    n = int(input('DIGA UM VALOR: '))
    computador = randint(0,10)
    escolha = input('PAR ou IMPAR? [P/I]').strip().upper()[0]
    if ((n + computador) % 2 == 0 and escolha == 'P') or ((n + computador) % 2 != 0 and escolha == 'I'):
       r = True
    else:
        r = False
    if r:
        print('-' * 15)
        print(f'Você jogou {n} e o computador jogou {computador}. Total {n + computador} {"DEU PAR" if (n + computador) % 2 == 0 else "DEU IMPAR"}')
        print('-' * 15)
        print('Você venceu!!!!')
        print('Vamos jogar novamente...')
        print('-=-' * 15)
        cont += 1
    else:
        print('-' * 15)
        print(f'Você jogou {n} e o computador jogou {computador}. Total {n + computador} {"DEU PAR" if (n + computador) % 2 == 0 else "DEU IMPAR"}')
        print('-' * 15)
        print('Você perdeu!!!!')
        print('-=-' * 15)
        break

print(f'GAME OVER! Você venceu {cont} veses.')