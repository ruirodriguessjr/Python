#Faça um programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
tamanho = float(input('Tamanho em metros quadrados: '))
litros = tamanho / 3
if tamanho%54 == 0:
	latas = tamanho / 54
else:
	latas = int(tamanho / 54) + 1
preco = latas * 80
print('{} latas '.format(latas))
print('R${:.2f}'.format(preco))
#Faça um Programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
#ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas
#e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o preço seja o menor.
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
#considere latas cheias.
tamanho = float(input('Tamanho em metros quadrados: '))
litros = tamanho / 6
if tamanho%54 == 0:
	latas = tamanho / 54
else:
	latas = int(tamanho / 54) + 1
preco = latas * 80
print('{} latas '.format(latas))
print('R${:.2f}'.format(preco))