print('=' * 27)
print('==== EMPRESA VAI COM AS OUTRAS ====')
print('=' * 27)
distancia = float(input('Qual a distância em km da sua viagem: '))
print('Você está prestes a começar uma viagem de {:.2f}km.'.format(distancia))
if distancia <= 200:
    valor = (distancia * 0.50)
else:
    valor = (distancia * 0.45)
print('O valor da sua passagem é R${:.2f}'.format(valor))
'''Lembrar sempre da indentação pois se eu colocar o print no local errado
ele não le ou le na hora errada.'''