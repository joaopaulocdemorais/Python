peso = float(input('Imforme seu peso: (Kg) '))
altura = float(input('Imforme sua altura: (m) '))

imc  = peso / (altura * altura)

if imc < 18.5:
    print('Com o IMC {:.2f}, você está abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Com o IMC {:.2f}, vocês está no peso ideal!'.format(imc))
elif imc > 25 and imc <= 30:
    print('Com o IMC {:.2f}, você esta com sobrepeso! Execicios fisicos pode te ajudar!'.format(imc))
elif imc > 30 and imc <= 40:
    print('Com o IMC {:.2f}, você está com Obesidade. Melhore sua alimetação e faça exercicios !'.format(imc))
else:
    print('Com o IMC {:.2f}, você está com obesidade mórbida, procure ajuda medica!'.format(imc))