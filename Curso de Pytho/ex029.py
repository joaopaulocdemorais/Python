from colorama import Fore
n = int(input('Qual é a velocidade atual do carro ? '))

if n<=80:
    print(Fore.YELLOW + 'Tenha um bom dia! Dirija com Segurança!')
else:
    valorMulta = 7 * (n - 80)
    print(Fore.RED + 'MULTADO ! Você excedeu o limite permitido que é de 80KM/h')
    print('Você deve pagar uma multa de ' + Fore.YELLOW +'R${}'.format(valorMulta))