dias = int(input('Quantos dias o carro foi alugado ?'))
km = float(input('Quantos KM forma rodados ? '))

print('O total a pagar e de: R${:.2f}'.format((60 * dias) + (0.15 * km)))