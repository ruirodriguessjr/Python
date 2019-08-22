#CriandoumMenuSeOpções

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
	print('=-='*10)
	print('''[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos Números
[5] -  Sair do Programa''')
	opcao = int(input('Qual é a sua opção: '))
	if opcao == 1:
		soma = n1 + n2
		print('A soma entre {} e {} é {}'.format(n1, n2, soma))
	elif opcao == 2:
		mult = n1 * n2
		print('A multiplicação entre {} e {} é {}'.format(n1, n2, mult))
	elif opcao == 3:
		if n1 > n2:
			maior = n1
		else:
			maior = n2
		print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
	elif opcao == 4:
		print('Informe os números novamente!')
		n1 = int(input('Primeiro Valor: '))
		n2 = int(input('Segundo Valor: '))
	elif opcao == 5:
		print('Finalizando!!!')
	else:
		print("Opção Inválida. Tente Novamente!")
print('Fim do Programa. Volte Sempre!')