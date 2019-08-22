#Maior e menor peso da sequência

maior = 0
menor = 0
peso = float(input("Informe o peso da 1º pessoa: "))
maior = peso
menor = peso
for c in range(2, 6):
	peso = float(input("Informe o peso da {}ª pessoa: ".format(c)))
	if(peso > maior):
		maior = peso
	elif(peso < menor):
		menor = peso
print("O maior peso é: {:.2f}kg.".format(maior))
print("O menor peso é: {:.2f}kg.".format(menor))