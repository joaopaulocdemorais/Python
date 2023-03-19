c = 1
impar = 0
par = 0
while c !=0:
    c = int(input('Imforme um número: '))
    if c != 0:
        if c % 2 ==0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} números par e {} números impar'.format(par, impar))