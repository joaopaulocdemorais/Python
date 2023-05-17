expr = str(input('Digite a expressão: '))
pilha = []

for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está invalida!')
