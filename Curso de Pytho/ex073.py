times = ('Cruzeiro', 'Botafogo', 'Fortaleza', 'Fluminense', 'Palmeiras', 'Internacional', 'Grêmio', 'Vasco', 'São Paulo', 'Atlético-MG', 'Santos',
        'Bragantino', 'Flamengo', 'Athletico-PR', 'Bahia', 'Goiás', 'Corinthians', 'América-MG', 'Cuiabá', 'Coritiba')

print('-=-'*15)
print(f'Lista de times do Brasileirão:  {times}')
print('-=-'*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=-'*15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=-'*15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=-'*15)
print((f'O Flamengo está na {times.index("Flamengo") + 1}ª posição'))