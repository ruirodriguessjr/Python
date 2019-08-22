#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
#Não utilize a função de potência da linguagem.

n1 = int(input('Informe o Primeiro Número: '))
n2 = int(input('Informe o Segundo Número: '))
total = 1
for c in range(1, n2+1):
	total = total * n1
print(f'A base de {n1} elevado a {n2} é: {total}')