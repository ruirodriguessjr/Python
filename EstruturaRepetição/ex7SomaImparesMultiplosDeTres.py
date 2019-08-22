# Soma ímpares múltiplos de três
soma = 0
cont = 0
for i in range(1, 501):
	if(i % 2 == 1):
		if(i % 3 == 0):
			cont += 1
			soma = soma + i
print("A quantidade de itens somados é: {}".format(cont))
print("A soma dos números ìmpares e divisíveis por 3 é: {}".format(soma))
