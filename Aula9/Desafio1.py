

name = input('Qual é o seu nome completo? ').strip()
pname = name.split()


print('Seu nome maiusculo é {}'.format(name.upper()))
print('Seu nome minusculo é {}'.format(name.lower()))
print('Seu nome sem espaços tem {} caracteres'.format(len(name)-name.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(pname[0], name.find(' ')))
