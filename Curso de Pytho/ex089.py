ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar ? [S/N]'))
    if resp in 'nN':
        break
print('---'* 30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print('---'* 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('---'* 30)
while True:
    print('---' * 30)
    opc = int(input('Mostrar notas de qual aluno: (999 interronpe)'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'NOTAS DE {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

