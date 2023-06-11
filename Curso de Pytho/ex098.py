from time import sleep


def contagem(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-'*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += passo
            sleep(0.5)
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= passo
            sleep(0.5)
        print('FIM')
    print('-' * 30)
contagem(1, 10, 1)
contagem(10, 0, 2)
contagem(int(input('Inicio:')), int(input('Fim:')), int(input('Passo:')))

