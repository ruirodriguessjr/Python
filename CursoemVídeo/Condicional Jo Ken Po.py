from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA ''')
jogador = int(input('Qual a sua jogada: '))
print('O computador escolheu {}'.format(itens[computador]))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=-=-=-=-=-=-=-=-==-=-=-=')
print('Jogador jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[computador]))
print('=-=-=-=-=-=-=-=-==-=-=-=')
if computador == 0: #Jogou pedra
    if jogador == 0:
        print('Empate!!!')
    elif jogador == 1:
        print('Jogador Vence!!')
    elif jogador == 2:
        print('Computador Vence!!!')
    else:
        print('Jogada Inválida!!!')
elif computador == 1: #Jogou papel
    if jogador == 0:
        print('Computador Vence!!!')
    elif jogador == 1:
        print('Empate!!!')
    elif jogador == 2:
        print('Jogador Vence!!!')
    else:
        print('Jogada Inválida!!!')

elif computador == 2:  #jogou tesoura
    if jogador == 0:
        print('Jogador Vence!!!')
    elif jogador == 1:
        print('Computador Vence!!!')
    elif jogador == 2:
        print('Empate!!!')
    else:
        print('Jogada Inválida!!!')


