info = input('Digite algo: ')

print('Você digitou: {}'.format(info))

print('O tipo do que você digitou é: {}'.format(type(info)))

print('É um caractere numérico? {}'.format(info.isnumeric()))

print('É um caractere alfabético? {}'.format(info.isalpha()))

print('É um caractere alfanumérico? {}'.format(info.isalnum()))

print('Está em maiúsculo? {}'.format(info.isupper()))

print('Esta em minúsculo? {}'.format(info.islower()))

