#Faça um Programa que peça a temperatura em graus Farenheit,
#transforme e mostre a temperatura em graus Celsius.
#C = (5 * (F-32) / 9).
f = float(input('Digite a temperatura em Farenheit: '))
c = (5 * (f - 32) / 9)
print('O valor convertido em Celsius é {:.2f}º'.format(c))
#Faça um Programa que peça a temperatura em graus Celsius,
#transforme e mostre em graus Farenheit.
c = float(input('Digite a temperatura em Celsius: '))
f = (1.8 * c) + 32
print('O valor convertido em Farenheit é: {:.2f}º'.format(f))

