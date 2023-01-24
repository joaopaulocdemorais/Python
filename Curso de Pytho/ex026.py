frase = str(input('Digite um frase: ')).strip().upper()
print('A letra A aprece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('A ùltima letra A apreceu na posição {}'.format(frase.rfind('A') + 1))