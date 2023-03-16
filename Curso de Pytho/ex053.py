frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Você digitou a frase "{}"'.format(junto))
inverso = ''
for letra in range(len(junto) -1,-1,-1 ):
    inverso = inverso + junto[letra]
print('O inverso e: ',inverso)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não e um palíndromo!')



