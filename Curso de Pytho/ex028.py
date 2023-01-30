from colorama import Fore
import time
import random
print(Fore.YELLOW + '--=' * 40)
print(Fore.BLUE + 'Vou pensar em um número entre 0 e 5. Tente adivnhar...')
print(Fore.YELLOW + '--=' * 40)
n = int(input(Fore.WHITE + 'Em que número eu pensei ? '))
print(Fore.CYAN + 'Processando.......')
nc = random.randint(0, 5)
time.sleep(5)
if n == nc:
    print(Fore.GREEN + 'PARABÉNS! Você consegui vencer!')
else:
    print(Fore.RED + 'GANHEI! Eu pensei no número {} e não no {}'.format(nc, n))

