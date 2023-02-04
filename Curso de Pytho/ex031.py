km = float(input('Imforme da ditancia em KM da viagem ? '))
print('O valor da passagem e: R${:.2f}'.format(km * 0.50 if km <=200 else km * 0.45 ))
