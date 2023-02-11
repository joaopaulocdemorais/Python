nome = str(input('Qual e o seu nome ?')).strip()

if nome == 'João Paulo':
    print('Que nome lindo !')
elif nome == 'Flamengo':
    print('O melhor time do mundo!')
elif nome in 'Neve Fred Floco Magali':
    print('Otimo nome para um gato!')
else:
    print('Nada de interessante.')
print('Tenha um bom dia, {} !'.format(nome))
