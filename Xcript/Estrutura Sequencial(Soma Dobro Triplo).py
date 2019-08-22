#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
prod = (n1 * 2) * (n2 / 2)
soma = (n1 * 3) + n3
cubo = n3**3
print('O produto pedido é: {:.2f}, a soma é: {:.2f} e a potência é: {:.2f}'.format(prod, soma, cubo))
