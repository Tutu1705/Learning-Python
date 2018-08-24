cash = int(input('Insira o seu salário: R$ '))

sup = cash / 10
inf = sup + (sup / 1/2)

print('='*15, 'CALCULANDO VALOR DO AUMENTO...', '='*15)

if cash > 1250:
    print('O valor do seu aumento será de R${}, portanto, seu salário total será de R${}.'.format(sup, cash+sup))
if cash <= 1250:
     print('O valor do seu aumento será de R${}, portanto, seu salário total será de R${}.'.format(inf, cash+inf))

