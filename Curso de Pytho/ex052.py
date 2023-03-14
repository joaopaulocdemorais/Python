from colorama import Fore
cont = 0
n = int(input('Digite um número: '))
for c in range(1,n+1):
    if n % c == 0:
        print(Fore.CYAN + '{}'.format(c), end=' ')
        cont = cont + 1
    else:
        print(Fore.WHITE + "{}".format(c), end= ' ')

print('\nO número {} foi divisível {} vezez'.format(n,cont))
if cont > 2:
    print(Fore.RED + 'Por isso ele NÃO E PRIMO!')
else:
    print(Fore.GREEN + 'Por isso ele e PRIMO!!!')