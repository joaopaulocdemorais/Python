from datetime import date
anoNasc = int(input('Informe o ano que você nasceu: '))
anoAtaul = int(date.today().year)
idade  = anoAtaul - anoNasc
if idade < 18:
    print('Com {} anos você ainda vai se alistar, faltam {} anos'.format(idade, 18 - idade))
elif idade > 18 :
    print('Com {} anos ja passou da hora de se alistar em {} anos'.format(idade, idade - 18))
else:
    print('Com {} anos, você deve se alistar!'.format(idade))