from datetime import datetime
trabalhador = {}
trabalhador['Nome'] = str(input('Nome: '))
trabalhador['Idade'] = datetime.now().year - int(input('Ano de nascimento: '))
trabalhador['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Contração'] = int(input('Ano de Contração: '))
    trabalhador['Salário'] = float(input('Salário: R$'))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + (trabalhador['Contração'] + 35) - datetime.now().year
print('---'*30)
for k, v in trabalhador.items():
    print(f'- {k} tem o valor {v}')