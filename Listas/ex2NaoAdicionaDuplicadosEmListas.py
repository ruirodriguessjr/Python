#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

num = list()
aux = 0
resp = 'S'
while True:
	aux = int(input('Informe um valor: '))
	if aux not in num:
		num.append(aux)
	else:
		print('Valor Duplicado. Não vou Adicionar...')
	resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
	if resp in 'Nn':
		break
print(f'Você Digitou os Seguintes Valores {num}')