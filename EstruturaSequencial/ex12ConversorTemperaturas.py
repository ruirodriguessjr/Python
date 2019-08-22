#Faça um Programa que peça a temperatura em graus Farenheit, 
#transforme e mostre a temperatura em graus Celsius.
#C = (5 * (F-32) / 9).

t = float(input("Informe a temperatura em Celsius: "))
f = ((t/5)*9) + 32
k = t + 273
print("A temperatura em Celsius é: {:.1f}º graus.".format(t))
print("A temperatura em Farenheit é: {:.1f}º graus.".format(f))
print("A temperatura em Kelvin é: {:.1f}º graus.".format(k))

