n1 = float(input('INFORME A PRIMEIRA NOTA:'))
n2 = float(input('INFORME A SEGUNDA NOTA:'))
media = (n1 + n2)/2
print('Sua media foi de: {}'.format(media))
if media >=6:
    print('Aprovado com sucesso !')
else:
    print('Ai lascou em parceiro(a)')
print('PARABENS!!!!!!!' if media>=6 else 'Vamos largar o celular {{{(>_<)}}}')
