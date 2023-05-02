total = mais100 = menor = 0
print('-'*30)
print('LOJA SUPER BARATÃO'.center(30))
print('-'*30)

while True:
    produtro = str(input('Nome do Produto:'))
    preço = float(input('Preço: R$'))
    continuar = ' '

    total += preço

    if preço > 1000:
        mais100 +=1

    if menor == 0:
        menor = preço
        nomeMenor = produtro
    elif menor > preço:
        menor = preço
        nomeMenor = produtro

    while continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N]')).strip().upper()[0]


    if 'N' in continuar:
        break
print('Fim do Programa'.center(30, '-'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais100} produto custando mais de R$1000,00')
print(f'O produto mais barato foi {nomeMenor} que custa R${menor:.2f}')