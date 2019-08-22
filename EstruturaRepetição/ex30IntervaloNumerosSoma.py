#Altere o programa anterior para mostrar no final a soma dos números.


soma = 0
num1=int(input("digite um numero--> "))
num2=int(input("digite outro numero--> "))
while num2<num1:
	num1=int(input("digite um numero--> "))
	num2=int(input("digite outro numero--> "))
else:
	for c in range(num1,num2,1):
		print(c)
		soma = soma + c
print(f'A soma dos valores é {soma}')