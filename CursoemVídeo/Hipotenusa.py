'''catopos = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))
hip = (catopos**2 + catadj**2) **(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))'''
'''Solução sem importação da biblioteca'''
from math import hypot
catopos = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))
hip = hypot(catopos, catadj)
print('A hipotenusa vai medir {:.2f}'.format(hip))
'''Posso usar a biblioteca inteira importando toda ela EX: import math, mas se eu fizer isso ocupo espaço na minha memória.'''
