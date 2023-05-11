nun = [2, 5, 9, 1]
nun[2] = 11
nun.append(7)
nun.sort(reverse=True)
nun.insert(2, 2)
if 4 in nun:
    nun.remove(4)
else:
    print('Essa lista não possui o numero 4')
#nun.pop(2)
print(nun)
print(f'Essa lista tem {len(nun)} elementos')