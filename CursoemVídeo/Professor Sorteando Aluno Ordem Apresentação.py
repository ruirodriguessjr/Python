'''NUNCA ESQUECER DO USO DA MEMÓRIA, POIS SE VOCÊ COLOCAR DESSE JEITO
FICA LIMITADO QUANTO AO USO DE OUTROS MÓDULOS'''
from random import shuffle
n1 = str(input('Primeiro aluno(a): '))
n2 = str(input('Segundo aluno(a): '))
n3 = str(input('Terceiro aluno(a): '))
n4 = str(input('Quarto aluno(a): '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação dos alunos será:')
print(lista)

