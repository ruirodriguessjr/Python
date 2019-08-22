#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, crie duas listas extras que vão conter apenas os valores pares 
#e os valores ímpares digitados, respectivamente. 
#Ao final, mostre o conteúdo das três listas geradas.

lista = list()
listaPar = list()
listaImpar = list()
while True:
	lista.append(int(input('Informe um valor: ')))
	resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
	print('-='*13)
	if resp in 'Nn':
		break
for c in lista:
	if c % 2 == 0:
		listaPar.append(c)
	elif c % 2 == 1:
		listaImpar.append(c)
print(f'Lista de Números = {lista}')
print(f'Lista de Pares = {listaPar}')
print(f'Lista de Ímpares = {listaImpar}')