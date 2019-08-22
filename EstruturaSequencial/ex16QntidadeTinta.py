#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
tamanho = float(input("Informe o tamanho em m² a ser pintados: "))
litros = tamanho / 3
latas = (litros / 18) 
valorLata = latas * 80
print("Você usará o total de {:.0f} latas de tinta.".format(latas))
print("O preço total é de: R${:.2f} reais".format(valorLata))