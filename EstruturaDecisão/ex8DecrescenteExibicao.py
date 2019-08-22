#Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = int(input("Informe o Primeiro Número: "))
n2 = int(input("Informe o Segundo Número: "))
n3 = int(input("Informe o Terceiro Número: "))
if((n1 > n2) and (n1 > n3)):
	print("O número {} é maior dos Três.".format(n1))
	if(n2 < n3): 
		print("O número {} é o menor dos Três.".format(n2))
		print("Em forma decrescente eles são exibidos assim: {}, {}, {}.".format(n1, n3, n2))
	else:
		print("O número {} é o menor dos Três.".format(n3))
		print("Em forma decrescente eles são exibidos assim: {}, {}, {}.".format(n1, n2, n3))
elif((n2 > n1) and (n2 > n3)):
	print("O número {} é maior dos Três.".format(n2))
	if(n1 < n3): 
		print("O número {} é o menor dos Três.".format(n1))
		print("Em forma decrescente eles são exibidos assim: {}, {}, {}.".format(n2, n3, n1))
	else:
		print("O número {} é o menor dos Três.".format(n3))
		print("Em forma decrescente eles são exibidos assim: {}, {}, {}.".format(n2, n1, n3))

else: 
	print("O número {} é maior dos Três.".format(n3))
	if(n1 < n2): 
		print("O número {} é o menor dos Três.".format(n1))
		print("Em forma decrescente eles são exibidos assim: {}, {}, {}.".format(n3, n2, n1))
	else:
		print("O número {} é o menor dos Três.".format(n2))
		print("Em forma decrescente eles são exibidos assim: {}, {}, {}.".format(n3, n1, n2))
