n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma de todos e: {}'.format(s))
print(f'A soma vale {s}')