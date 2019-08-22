'''Triângulo equilátero: possui os três lados com medidas iguais. AB = BC = AC
Triângulo isósceles: possui dois lados com medidas iguais. XY = XZ
Triângulo escaleno: possui os três lados com medidas diferentes. AB != BC != AC'''
x = float(input('Comprimento do primeiro segmento: '))
y = float(input('Comprimento do segundo segmento: '))
z = float(input('Comprimento do terceiro segmento: '))
if x < y + z and y < z + x and z < x + y:
    print('Os segmentos podem formar um Triângulo ', end='')
    if x == y == z:
        print('Equilátero.')
    elif x != y != z != x:
        print('Escaleno.')
    else:
        print('Isóceles.')
else:
    print('Os segmentos acima não formam Tirângulo.')
'''Meu bloco de comandos IF, posso fazer a condição dentro da condição.'''

