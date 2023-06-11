def escreve(texto):
    valor = len(texto) + 2
    print(f'-'* valor)
    print(texto.center(valor))
    print(f'-' * valor)


escreve(str(input('Informe o texto: ')))