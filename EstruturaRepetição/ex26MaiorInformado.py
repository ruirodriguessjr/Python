#Faça um programa que leia 5 números e informe o maior número.
maior = 0
for c in range(1, 6):
	n = int(input(f'Informe o {c} número: '))
	if n > maior:
		maior = n
print(f'O maior número informado foi {maior}.')