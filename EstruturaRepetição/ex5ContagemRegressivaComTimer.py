#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
from time import sleep

print('=' * 35)
print("Contagem Regressiva Começando!!!")
for i in range(10, -1, -1):
	print(i)
	sleep(0.6)
print("Feliz Ano Novo!!!")
print('=' * 35)