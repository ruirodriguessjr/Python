#DigitandoValorParada

n = int(input('Informe um número: [999 para parar]: '))
soma = 0
nNum = 0
n = int(input('Informe um número: [999 para parar]: '))
while n != 999:
	if n == 999:
		break
	else:
		soma = soma + n
		nNum += 1
	n = int(input('Informe um número: [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(nNum, soma))