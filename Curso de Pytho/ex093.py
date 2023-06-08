jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for i in range(0, tot):
    partidas.append(int(input(f'Informe a quantidade de gols na {i+1} patida: ')))

jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('---'*30)
print(jogador)
print('---'*30)
for k, i in jogador.items():
    print(f'O campo {k} tem o valor {i}')
print('---'*30)
print(f'O Jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'    => Na partida {i + 1}, fez {v} gols.')
