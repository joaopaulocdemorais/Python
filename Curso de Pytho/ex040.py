n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluno: '))
media = (n1 + n2) / 2

if media < 5:
    print('Com a media {:.2f}, o aluno esta REPROVADO !'.format(media))
elif media >= 5 and media < 7:
    print('Com a media {:.2f}, o aluno de RECUPERAÇÃO !'.format(media))
else:
    print('Com a media {:.2f}, o aluno esta APROVADO!'.format(media))
