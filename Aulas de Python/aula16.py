lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[:2])
print(sorted(lanche))

for comida in range(0, len(lanche)):
    print(lanche[comida])

for c in lanche:
    print(f'Eu vou comer {c}')

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c}, que está na posição {pos}')

