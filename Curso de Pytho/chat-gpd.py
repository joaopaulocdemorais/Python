# Solicita os valores iniciais da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
num_termos = int(input("Digite o número de termos da PA: "))

# Gera a PA
pa = []
termo_atual = primeiro_termo

for i in range(num_termos):
    pa.append(termo_atual)
    termo_atual += razao

# Exibe a PA gerada
print("A PA gerada é:", pa)
