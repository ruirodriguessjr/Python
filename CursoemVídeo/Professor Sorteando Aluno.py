from random import choice
n1 = str(input('Primeiro aluno(a): '))
n2 = str(input('Segundo aluno(a): '))
n3 = str(input('Terceiro aluno(a): '))
n4 = str(input('Quarto aluno(a): '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O(a) aluno(a) sorteado foi {}'.format(escolhido))

