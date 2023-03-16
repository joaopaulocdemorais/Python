from datetime import date
contM = 0
contN = 0
ano = date.today().year
for pessoa in range(1,8):
    anoNasc = int(input('Infome o ano de nascimento da {}° pessoa ?'.format(pessoa)))
    idade = ano - anoNasc
    if idade < 18:
        contN = contN + 1
    else:
        contM = contM + 1
print('Nesse grupo de pessoas temos {} MAIORES e {} MENORES'.format(contM, contN))