from datetime import date
anotual = int(date.today().year)
anoNasc = int(input('Infrome o seu ano de nascimento:'))
idade = anotual - anoNasc
categoria = ''
if idade < 10:
    categoria = 'MIRIM'
elif idade < 15:
    categoria = 'INFANTIL'
elif idade < 20:
    categoria = 'JUNIOR'
elif idade < 26:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print('Com {} anos, você o atleta e da categoria:{}'.format(idade, categoria))