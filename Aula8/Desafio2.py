import math

n1 = float(input('Insira o valor do cateto oposto: '))
n2 = float(input('Insira o valor do cateto adjacente: '))
hip = math.hypot(n1, n2)

print('O valor do cateto oposto é {}, o do cateto adjacente {}, logo o valor de hipotenusa é {}'.format(n1, n2, hip))


