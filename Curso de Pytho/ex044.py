print('='*10,'LOJAS CAROLINA','='*10)
print('INFORME A FOMRA DE PAGAMENTO')
print('1 - À vista no dinheiro ou cheque')
print('2 - À vista no cantão')
print('3 - Em 2x no cartão')
print('4 - Em 3x ou mais no cartão')
opc = int(input('Escolha a opção de pagamento: '))
valor = float(input('Informe o valor da compras: R$'))
if opc == 1:
    des = valor *(10/100)
    print('Um compra à vista no valor de R${} o cliente deve pagar R${}'.format(valor, valor - des))
elif opc == 2:
    des = valor *(5/100)
    print('Um compra à vista no cartão no valor de R${} o cliente deve pagar R${}'.format(valor, valor - des))
elif opc == 3:
    print('Uma compra de R${} parcelada em 2x o cliente irá pagar parcelas de R${}'.format(valor, valor/2))
elif opc == 4:
    par = int(input('Informe a qunatidade de parcelas: '))
    print('Um compra de R${} parcelada em {}x o cliente irá pagar parcelas de R${} totalizando R${}'.format(valor,par, (valor + valor*(20/100))/par,valor + valor*(20/100)))
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE!!!')