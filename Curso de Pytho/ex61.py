print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = int(input('Quantos termos da PA você quer? '))
while termo > 0:
    print('{} -> '.format(primeiro),end='')
    primeiro = primeiro + razao
    termo = termo - 1
print('END')