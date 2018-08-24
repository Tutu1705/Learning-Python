

frase = 'Curso em Vídeo Python'
frase2 = '  Curso Python  '




# 1 - FATIAMENTO

#       printfrase[9])      retornará somente a letra com no índice 9
#       print(frase[3:9])   retornará tudo entre 3 e 8, o última número é retirado
#       print(frase[9:21:2])    irá considerar as letras de 9 à 20 e pulará de 2 em 2 casas
#       print(frase[:5])    retornará do começo até o indice 5
#       print(frase[15:])   retornará do 15 até o final
#       print(frase[9::3])  irá considerar do 9 até o final pulando de 3 em 3 casas


# 2 - ANALISE

#       print(len(frase))   retornará o comprimento da fase
#       print(frase.count('o'))     retornará a quantidade de X em que a letra 'o' aparece
#           print(frase.count('o',0,13))    este é semalhante ao acima, apenas utilizei o range de fatiamento
#       print(frase.find('deo'))
#           print(frase.find('Android'))    este é semelhante ao acima, mas ao tentar utilizar uma palavra que não está na variável, o retorno será de -1
#       print('Curso' in frase)     retornará True ou False se a palavra existe na variável


# 3 - TRANSFORMACAO

#       print(frase.replace('Python','Android'))    substituirá o Python por android
#       print(frase.upper())    retornará toda a string em maiuscula
#       print(frase.lower())    retornará toda a string em minuscula
#       print(frase.capitalize())   retornará toda a frase em minusculo, deixando apenas a primeira letra em maiuscula
#       print(frase.title())    ele fará o "capitalize" em todas as frases da string
#       print(frase2.strip())   removerá todos os espaços inúteis, do começo e do final da frase
#       print(frase2.rstrip())  removerá todos os últimos espaços da frase
#       print(frase2.lstrip())  removerá todos os primeiros espaços da frase


# 4 - DIVISAO

#       print(frase.split())    removerá todos os espaços, tornando cada palavra uma string e cada letra com um índice. Cada palavra ganha um índice em uma lista
#       neste, para a operação, considere "frase.split [0][3:8]", o primeiro range é a primeira palavra, e o segundo range é o indice da primeira palavra.


# 5 - JUNCAO

#       print(''.join(frase))   juntará todos os elementos separados pelo "split" com o espaço.