#JogoDoParOuImpar

from random import randint

print('=-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*15)
v = 0
while True:
	jogador = int(input('Digite um valor: '))
	computador = randint(0, 10)
	total = jogador + computador
	tipo = ' '
	while tipo not in 'PI':
		tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
	print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} ', end='')
	print('Deu par' if total % 2 == 0 else 'Deu Impar')
	if tipo == 'P':
		if total % 2 == 0:
			print('Você Venceu!!!')
			v += 1
		else:
			print('Você Perdeu!!!')
			break
	elif tipo == 'I':
		if total % 2 == 1:
			print('Você Venceu!!!')
			v += 1
		else:
			print('Você Perdeu!!!')
			break
	print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes.')