#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
temp = []
princ = [] 
mai = men = 0
while True:
	temp.append(str(input('Nome: ')))
	temp.append(float(input('Peso: ')))
	if len(princ) == 0:
		mai = men = temp[1]
	else:
		if temp[1] > mai:
			maior = temp[1]
		if temp[1] < men:
			men = temp[1]
	princ.append(temp[:])
	temp.clear()
	resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
	if resp in 'Nn':
		break
print('=-'*36)
print(f'Os dados foram {princ}')
print(f'Foram cadastrados {len(princ)} pessoa(s).')
print(f'O maior peso foi o de {mai}kg')
print(f'O menr peso foi {men}kg')