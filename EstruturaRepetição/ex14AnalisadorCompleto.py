#Analisador completo
menorVinte = 0
contIdade = 0
contSexoFeminino = 0
soma = 0
media = 0
maior = 0
menor = 0
idade = 0
nomeMaior = ""
for c in range(1, 5):
	print("===== {}ª PESSOA =====".format(c))
	nome = str(input("Nome: ").upper())
	
	idade = int(input("Idade: "))
	if(idade < 0):
		print("Idade inválida. Informe Novamente!")
	else:
		maior = idade
		menor = idade
		contIdade = contIdade + 1
		soma = soma + idade
	while(idade < 0):
		Idade = int(input("Idade: "))
		if(idade < 0):
			print("Idade inválida. Informe Novamente!")
		else:
			if(maior > idade):
				nomeMaior = nome
				maior = idade
			elif(menor < idade):
				menor = idade		
			cont = cont + 1
			soma = soma + idade

	sexo = int(input("Informe seu sexo: [1] - Feminino [2] - Masculino: "))
	while(sexo != 1 or sexo != 2):
		if (sexo == 1):
			if(idade < 20):
				contSexoFeminino +=1
				menorVinte = menorVinte + 1
				break
		elif(sexo == 2):
			break
		else:
			print("Informe Novamente!")

media = soma / contIdade
print("A média de idade do grupo é de {:.2f} anos.".format(media))
print("O homem mais velho do grupo tem {} anos e seu nome é {}".format(maior, nomeMaior))
print("Ao todo são {} mulheres com menos de 20 anos.".format(contSexoFeminino))