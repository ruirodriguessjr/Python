#Faça um programa que pergunte o preço de três produtos
#e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
p1 = float(input('Digite o 1º valor do Produto: '))
p2 = float(input('Digite o 2º valor do Produto: '))
p3 = float(input('Digite o 3º valor do Produto: '))
if p1 < p2 and p1 < p3:
    print('O Primeiro Produto é mais barato!!! ')
elif p2 < p1 and p2 < p3:
    print('O Segundo Produto é mais barato!!! ')
else:
    print('O Terceiro Produto é o mais barato!!! ')

