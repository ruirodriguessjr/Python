#Faça um programa que leia 5 números e informe a soma e a média dos números.

media = soma = 0
for c in range(1, 6):
	n = int(input(f'Informe o {c}º número: '))
	soma = soma + n
media = soma / c
print(f'O maior número informado foi {media:.2f}.')