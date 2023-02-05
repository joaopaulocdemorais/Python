print('-=-' * 20)
print(" "*18 + 'ANALIZANDO TRIANGULOS')
print('-=-' * 20)
r1 = float(input('Informe o primeiro segmento: '))
r2 = float(input('Informe o segundo segmento: '))
r3 = float(input('Informe o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segimentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segimento acima NÃO PODEM FORMAR UM triângulo!')