aula = 'Curso em Vídeo de Python'

print(aula[3])
print(aula[3:13])
print(aula[:14])
print(aula[14:])
print(aula[3:13:2])
print(aula[5::2])
print(aula[::2])
print(aula.count('Curso'))
print(aula.upper())
print(aula.upper().count('o'))
print(len(aula))
print(aula.replace('o', 'a'))
print('Curso' in aula)
print(aula.find('de'))
print(aula.split())
divido = aula.split()
print(divido[1][1])

print("""Existem alguns sites que oferecem funcionalidades semelhantes ao Snapdrop, aqui estão alguns exemplos:

WeTransfer: permite transferir arquivos de até 2GB sem precisar criar uma conta.
Send Anywhere: permite transferir arquivos de vários tipos e tamanhos, incluindo fotos, vídeos, música e documentos.
Jumpshare: permite compartilhar arquivos de até 250MB e inclui recursos de colaboração e comentários.
Filemail: permite enviar arquivos de até 4GB e oferece recursos como envio automático e notificações de entrega.
TransferNow: permite compartilhar arquivos de até 4GB e inclui recursos de segurança avançada e acompanhamento de envio.

Esses são alguns exemplos de sites que oferecem funcionalidades semelhantes ao Snapdrop, sempre é importante verificar
as limitações e recursos que cada um oferece para escolher a melhor opção para sua necessidade.""")



