#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

num = list()
n = cont = 0
while True:
	num.append(int(input('Informe um valor: ')))
	resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
	if resp in 'Nn':
		break
print('-='*30)
print(f'A quantidade de números digitados foram: {len(num)}')
num.sort(reverse=True)
print(f'Você Digitou os Seguintes Valores de forma Decrescente: {num}')
if 5 in num:
	print('O valor 5 faz parte da lista!')
else:
	print('O valor 5 não faz parte da lista!')