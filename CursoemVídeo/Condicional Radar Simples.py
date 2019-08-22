#from random import randint
print('=' * 27)
print('PROGRAMA SUA VIDA VALE MAIS')
print('=' * 27)
velocidade = float(input('Qual a velocidade  atual do seu carro: '))
if velocidade > 80:
    print('Multado você excedeu o limite de velocidade de 80km/h')
    multa = (velocidade - 80) * 7
    print('O valor de multa que você irá pagar é de R$ {:.2f}'.format(multa))
print('Bom dia, Dirija com segurança!!!')