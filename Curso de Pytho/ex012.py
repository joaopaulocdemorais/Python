p = float(input('Qual e o preço do produto: R$'))
d = float(input('Informe o desconto: '))

print('O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}'.format(p, d, p - (p * (d/100))))

