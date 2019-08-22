n1 = float(input("Informe o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
print("A soma dos valores é: {}.".format(n1+n2))
print("A subtração dos valores é: {}.".format(n1-n2))
print("A multiplicação dos valores é: {}.".format(n1*n2))
divisor = int(input("Qual número você quer que divida o outro, 1 ou 2: "))
if(divisor == 1 and n1 != 0):
	print("A divisão dos valores é: {}.".format(n2/n1))	
elif(divisor == 2 and n2 != 0):
	print("A divisão dos valores é: {}.".format(n1/n2))		
else:
	print("Zero não pode dividir outro número.")