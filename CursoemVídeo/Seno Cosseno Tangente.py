'''Método Importando toda a biblioteca:'''
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
'''Caso eu queira usar apenas as funções descriminadas da biblioteca math poderia fazer assim:
from math import radians, sin, cos, tan
sendo assim, apenas essas operações da bibliotecas seriam utilizadas reduzindo minha memória ultilizada.
Apenas lembrando de retirar o math.(módulos) pois fiminuindo meu espaço ele não é necessário.'''

