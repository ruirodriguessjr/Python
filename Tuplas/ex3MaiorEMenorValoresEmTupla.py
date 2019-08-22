#MaiorEMenorValoresEmTupla
from random import randint
valor = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteei os valores {valor}')
maior = menor = 0
for c in valor:
	print(f'{c} ', end='')
print(f'\nO maior valor sorteado foi {max(valor)}')
print(f'O maior valor sorteado foi {min(valor)}')