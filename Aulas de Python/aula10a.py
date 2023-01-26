nome = str(input('Aqual é o seu nome ?')).strip()
if nome == 'joao':
    print('Como seu nome e lindo!')
else:
    print('Seu nome e bem chato!')
print('Bom dia {}'.format(nome.upper()))
