vel = int(input('Qual a km/h que o carro passou? '))

multa = (vel-80) * 7

if vel > 80:
    print('Você foi MULTADO!')
    print('-'*15, 'Calculando o valor da multa...', '-'*15)
    print('O valor da multa é de R${}.00'.format(multa))

else:
    print('Boa viagem!')

