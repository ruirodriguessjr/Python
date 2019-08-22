#Faça um programa que peça 10 números inteiros, 
#calcule e mostre a quantidade de números pares e a quantidade de números impares.

c = 1
n = par = impar = 0
while c <= 10:
	n = int(input(f'Informe o {c}º número: '))
	if n % 2 == 0:
		par += 1
	if n % 2 == 1:
		impar += 1
	c += 1
print(f'A quantidade de Par é {par} e a quantidade de Impar é {impar}.')