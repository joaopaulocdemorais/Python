from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))
op = 0
while op !=5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    op = int(input('>>>>> Qual é a sua opção: '))
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1,n2, soma))
    elif op == 2:
        mult = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1,n2, mult))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Ente {} e {} o maior é {}'.format(n1, n2, maior))
    elif op == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo Valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print("=-"*15)
    sleep(2)
print('Fim do programa! Volte sempre!')