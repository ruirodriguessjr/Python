#C = Celsius
#F = Farenait
#K = Kelvin
c = float(input('Informe a temperatura em ºC: '))
f = ((c*9)/5)+32
k = c + 273
print('A temperatura em ºC de {}, corresponde a {}ºF, e em ºK corresponde {}'.format(c, f, k))
