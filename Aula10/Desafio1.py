import random

num = random.randint(0, 5)

print('-'*10, 'Gerando um número...', '-'*10)

chute = int(input('Insira uma numeração de 0 à 5 e tente acertar: '))

if chute == num:
    print('O numero gerado foi {}, parabéns, você acertou o resultado!'.format(num))

else:
    print('O número gerado foi {}, você errou o chute.'.format(num))





