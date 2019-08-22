#Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("Informe o Primeiro Número: "))
n2 = int(input("Informe o Segundo Número: "))
if(n1>n2):
	print("O número {} é maior que o número {}.".format(n1, n2))
else:
	print("O número {} é maior que o número {}.".format(n2, n1))