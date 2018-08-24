print('=' * 15, 'BEM VINDO À LB VIAGENS!', '=' * 15)

dis = int(input('Digite a distância da viagem em KM: '))

print('     Calculando o valor da viagem...     ')

if dis > 200:
    print('O valor da passagem será de R${}.'.format(0.45 * dis))

else:
    print('O valor da passagem será de R${}.'.format(0.50 * dis))

