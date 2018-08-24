from random import sample

a1 = input('Insira o nome do primeiro aluno: ')
a2 = input('Insira o nome do segundo aluno: ')
a3 = input('Insira o nome do terceiro aluno: ')
a4 = input('Insira o nome do quarto aluno: ')
ordem = [a1, a2, a3, a4]

sample(ordem, k=4)
print('A sequencia de alunos será: {}.'.format(ordem))
