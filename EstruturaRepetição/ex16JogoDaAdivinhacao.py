#JogoDaAdivinhacao

from random import randint
comp = randint(0, 10)
print("Sou seu computador...Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
acertou = False
palpite = 0
while not acertou:
	jogador = int(input('Qual é seu palpite: '))
	palpite += 1
	if jogador == comp:
		acertou = True
	else:
		if jogador < comp:
			print('Mais... Tente mais uma vez!')
		elif jogador > comp:
			print('Menos... Tente mais uma vez!')
print('Acertou com {} tentativas.'.format(palpite))