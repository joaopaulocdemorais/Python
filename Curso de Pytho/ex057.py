sexo = input('Informe seu sexo: [M/F]').strip()
r = 1
while r != 0 :
    if sexo == 'M' or sexo == 'm':
        sexo = 'masculino'
        r = 0
    elif sexo == 'f' or sexo == 'F':
        sexo = 'feminino'
        r = 0
    else:
        sexo = input('Dados inválidos. Por favor, informe seu sexo: ').strip()
print('Sexo {} resgistrado com suscesso!!!'.format(sexo))