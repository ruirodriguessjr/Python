#Soma dos pares

soma = 0
for i in range(1, 7):
	n = int(input("Informe o {}º número: ".format(i)))
	if(n % 2 == 0):
		soma += n
print("A soma dos pares é: {}".format(soma))