ano = int(input('Insira um ano: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('Ele é bissexto!')
        else:
            print('Não é bissexto!')
    else:
        print('Ele é bissexto!')
else:
    print('Ele não é bissexto!')

