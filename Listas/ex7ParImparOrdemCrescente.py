#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos 
#e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#No final, mostre os valores pares e ímpares em ordem crescente.

par = list()
impar = list()
lista = list()
for c in range(1, 8):
	lista.append(int(input(f'Informe o {c}º número: ')))
	if c % 2 == 0:
		par.append(c)
	if c % 2 == 1:
		impar.append(c)
par.sort()
impar.sort()
print(f'Lista de Pares: {par}')
print(f'Lista de Ímpares: {impar}')

"""valor = 0
lista = [[], []]
for c in range(1, 8):
	valor = int(input(f'Informe o {c}º número: '))
	if valor % 2 == 0:
		lista[0].append(valor)
	if c % 2 == 1:
		lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Lista de Pares: {lista[0]}')
print(f'Lista de Ímpares: {lista[1]}')"""