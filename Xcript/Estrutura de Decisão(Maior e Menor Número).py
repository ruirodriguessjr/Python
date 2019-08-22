#Faça um Programa que peça dois números e imprima a soma.
n1 = int(input('Primeiro Numero: '))
n2 = int(input('Segundo Número: '))
maior = 0
menor = 0
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))