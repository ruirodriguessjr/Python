from random import randint # biblioteca que sorteia.
from time import sleep # Biblioteca de tempo do python
computador = randint(0, 2) # Faz o computador sortear o número
print('-=-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar....')
print('-=-' * 30)
jogador = int(input('Em que número eu pensei: ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Você acertou. Sem graça... Parabéns')
else:
    print('Errou, eu pensei em {} e você em {} tente de novo...kkkkkkkk'.format(computador, jogador))

