from colorama import Fore

n = int(input('Me diga um número qualquer: '))
if (n % 2 == 0):
    print('O número {} é '.format(n) + Fore.BLUE + 'PAR')
else:
    print('O número {} é '.format(n) + Fore.BLUE + 'IMPAR')

