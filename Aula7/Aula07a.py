nome = input('Qual é o seu nome?')
print ('Muito prazer {:10}!'.format(nome))

nome = input('Qual é o seu nome?')
print ('Muito prazer {:>10}!'.format(nome))

nome = input('Qual é o seu nome?')
print ('Muito prazer {:<10}!'.format(nome))

nome = input('Qual é o seu nome?')
print ('Muito prazer {:^10}!'.format(nome))

nome = input('Qual é o seu nome?')
print('Muito prazer {}!'.format(nome))

##

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2

print ('A soma é {}, o produto {}, e a divisão {:.3f}'.format(s, m, d), end='')
#               utilize end='' para não quebrar linha
print (' Divisão inteira é {}, a exponenciação {}, e o \n módulo {}'.format(di,e,r))
#               utilize \n para quebrar linha



