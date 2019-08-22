'''Não resolvido'''

#Faça um programa que calcule as raízes de uma equação do segundo grau,
#na forma ax2 + bx + c. O programa deverá pedir os valores de
#a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero,
#a equação não é do segundo grau e o programa não deve fazer pedir os demais valores,
#sendo encerrado; Se o delta calculado for negativo, a equação não possui raizes reais.
#Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
#informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
#Delta == ((b**2) - (4*a*c))
#x == -b +- ((b**2) - (4*a*c) * 1/2) / (2*a)
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
delta = ((b ** 2) - (4 * a * c))
print('{:.2f}'.format(delta))
if delta < 0:
    print('Não é possível realizar equação, com raiz quadrada negativa. ')
elif delta < 0:
    print('Delta = ',delta,' a equacao não possui raizes reais.')
    print('Resultado Negativo.')
elif delta == 0:
    print('Delta = ', delta,' a equação possui duas raízes iguais.')
    x = ((-1) * b,'+-', (delta ** (1/2)) / (2 * a))
    print('raiz da equacao = ', x)
'''elif delta > 0:
    x1 = ((-1) * b, '+-', (delta ** (1/2)) / (2 * a))
    print('O resultado de x1 é: {:.2f}'.format(x1))
    x2 = ((-1) * b, '+-', (delta ** (1/2)) / (2 * a))
    print('O resultado de x2 é: {:.2f}'.format(x2))
'''


''' print("digite os termos da equacao a, b e c da equacao ax^2 + bx + c")
a = input("digite o termo a ---> ")
if a == 0:
    print("nao eh uma equacao de segundo grau")
else:
    b = input("digite o termo b  ---> ")
    c = input("digite o termo c ---> ")
    delta = (math.pow(b,2) - (4 * a * c))
    if delta < 0:
        print('delta = ",delta," a equacao nao possui raizes reais')
        if delta == 0:
            print('delta = ',delta,' a equacao possui uma raiz')
            raiz = ((-1) * b + (math.sqrt(delta))/(2*a)
            print('raiz da equacao = ', raiz)
            if delta > 0:
                print('delta = ',delta,' a equacao possui duas raizes')
        raiz1 = (-1)* b + math.sqrt(delta)) / (2*a)
        raiz2 = (-1)* b - math.sqrt(delta)) / (2*a)
        print('raiz1 da equacao = ', raiz1)
        print('raiz2 da equacao = ', raiz2)'''