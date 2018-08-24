frase = str(input('Insira uma frase: ')).strip().lower().replace('á','a').replace('ã','a').replace('à','a').replace('â','a')
print('A letra "a" aparece {} vezes: \n A primeira letra "a" aparece na {} posição \n A segunda letrar "a" aparece na {} posição'.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))





#               utilizamos o "rfind" pois ele começa a procurar do lado direto para o esquerdo.


#               utilizamos o +1