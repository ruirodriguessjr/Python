#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = list()

for c in range(1, 11):
	valor = float(input(f'Informe o {c}º número: '))
	lista.append(valor)
lista.sort(reverse=True)
print(lista)