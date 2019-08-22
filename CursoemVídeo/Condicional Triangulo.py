print('='*27)
print('===FORMANDO UM TRIÂNGULO===')
print('='*27)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Seundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Minhas retas com valor de {:.1f}, {:.1f} e {:.1f}. Formam um Triângulo.'.format(r1, r2, r3))
else:
    print('Não formam um triangulo.')