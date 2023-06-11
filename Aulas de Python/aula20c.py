def contador(*n):
    print(n)
    print(f'Você informou {len(n)} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(valor):
    pos = 0
    while pos < len(valor):
        valor[pos] *= 2
        pos += 1


valores = [8, 3, 9, 5, 10]
dobra(valores)
print(valores)