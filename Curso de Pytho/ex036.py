vcasa = float(input('Informe o valor da casa que você deseja comprar: R$'))
sal = float(input('Informe o valor do seu salário mensal: R$'))
anos = int(input('Em quantos nos você deseja que seja feito seu financiamento ? '))

vpar = vcasa / (anos * 12)
vcond  = sal * (30/100)

print('Para uma casa de R${} em {} anos a prestação será de R${:.2f} '.format(vcasa, anos, vpar))
if vpar > vcond:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo CONCEDIDO!!!')

