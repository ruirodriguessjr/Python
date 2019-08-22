print('Adicionando dados na minha lista criada')
teste = list()
teste.append('Gustavo')
teste.append(40)
print('='*30)
print('Adicionando minha lista teste dentro da minha lista galera')
galera = list()
galera.append(teste[:]) # [:] = Copia meus dados da lista como se fosse um intervalo do range ou fatiamento de string
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print('='*30)
print('Como uma matriz trabalho as matrizes(listas)')
pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoas[0])
print(pessoas[0][0])
print(pessoas[0][1])
print(pessoas[1][1])
print(pessoas[3][0])
print(pessoas[2][1])
print('='*30)
print('Mostro na minha tela os dados e as idades de toda a minha lista')
for c in pessoas:
	print(f'{c[0]} tem {c[1]} anos de Idade!!!')
print('='*30)
print('Crio uma lista para nome e outra pra idade.')
print('Faço um clone usando [:], caso não use esse elemento ele não adiciona.')
print('Exemplo sem [:]!!!')
gente = list()
dados = list()
for c in range(0, 3):
	dados.append(str(input('Nome: ')))
	dados.append(int(input('Idade: ')))
	gente.append(dados)
	dados.clear()
print(gente)
print('='*30)
print('Exemplo Com [:]!!!')
gente = list()
dados = list()
for c in range(0, 3):
	dados.append(str(input('Nome: ')))
	dados.append(int(input('Idade: ')))
	gente.append(dados[:])
	dados.clear()
print(gente)
print('='*30)
print('Mostrando idade e se é maior ou menor dela.')
totmaior = totmenor = 0
for c in gente:
	if c[1] >= 21:
		print(f'{c[0]} é maior de idade!')
		totmaior += 1
	else:
		print(f'{c[0]} é menor de idade!')
		totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')