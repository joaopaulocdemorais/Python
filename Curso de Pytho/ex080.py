lista = list()

for v in range(0,5):
    n = int(input('Digite o valor: '))
    if v == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado a posdição {pos} da lista...')
                break
            pos += 1
print('--'*30)
print(f'Os valores digitaso em ordem foram: {lista}')