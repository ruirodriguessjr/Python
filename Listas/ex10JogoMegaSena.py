#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
#cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
lista = list()
jogos = list()
print('='*30)
print('     Jogo na Mega Sena')
print('='*30)
qtd = int(input('Informe a quantidade quer que eu sorteei: '))
tot = 1
while tot <= qtd:
	cont = 0
	while True:
		num = randint(1, 61)
		if num not in lista:
			lista.append(num)
			cont += 1
		if cont >= 6:
			break
	lista.sort()
	jogos.append(lista[:])
	lista.clear()
	tot+= 1

print(f'-=-=-= Sorteando {qtd} Jogos -=-=-=')
for i, l in enumerate(jogos):
	print(f'Jogo {i+1}: {l}')
	sleep(1)
print('-=-=-=-=-= < Boa Sorte! > -=-=-=-=-=')
