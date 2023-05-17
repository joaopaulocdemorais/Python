teste = []
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'oi seu lindo'
teste[1] = [6]
galera.append(teste[:])
print(galera)