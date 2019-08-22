# -*- coding: utf-8 -*-

from random import randint
from  time import sleep

computador = randint(0,5)
print ('-=-' * 20)
print('Processando um número entra 0 a 5')
print ('-=-' * 20)
jogador = int((input('Informa um número de 1 a 5: ')))

print ('Processando...')
sleep(3)

if jogador == computador:
    print('Parabéns !!! ')
else:
    print('O número sorteado é {} e não o {}'.format(computador,jogador))