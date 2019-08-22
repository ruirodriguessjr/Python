#Grupo da Maioridade
cont_maior = 0
cont_menor = 0
ano_atual = 2019
for c in range(1, 8):
	pessoa = int(input("Informe o ano a {}ª pessoa nasceu: ".format(c)))
	if(pessoa > ano_atual):
		print("Informe Novamente. Data acima do ano atual!")
	while(pessoa > ano_atual):
		pessoa = int(input("Informe o ano que você nasceu: "))
		if(pessoa > ano_atual):
			print("Informe Novamente. Data acima do ano atual!")
	idade = ano_atual - pessoa
	if(idade >= 18):
		cont_maior = cont_maior + 1
	else:
		cont_menor = cont_menor + 1

print("Ao todo tivemos {} pessoas maiores de idade.".format(cont_maior))
print("E também tivemos {} pessoas menores de idade.".format(cont_menor))