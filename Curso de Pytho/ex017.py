from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto dajacente: '))
#hi = (co ** 2 + ca ** 2) **(1/2)
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))