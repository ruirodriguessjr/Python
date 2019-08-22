#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = list()

for c in range(1, 6):
	valor = int(input(f'Informe o {c}º número: '))
	lista.append(valor)
print(lista)