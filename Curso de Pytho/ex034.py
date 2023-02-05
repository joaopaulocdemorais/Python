import time
sal = float(input('Informe o salario de um funcionario ? R$'))

if sal > 1250:
    newsal = sal + (sal * (10/100))
else:
    newsal = sal + (sal * (15/100))
print('O novo salário desse funcionario e de R${}'.format(newsal))
time.sleep(10)
