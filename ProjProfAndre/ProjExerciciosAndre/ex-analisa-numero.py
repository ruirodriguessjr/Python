# -*- coding: utf-8 -*-

#
# Criar um programa que leia um numero de 4 posições e imprima
# Unidade, Dezena, Centena e Milhar
#

num = int(input('Informe o número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print ('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))