n1 = int(input('Digite um número? '))
n2 = int(input('Outro número? '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
raiz = 81**(1/2)
#Operadores conseguem multiplicar situações também.
#'Oi' + 'Ola' = OiOla
#'Oi'*5 = OiOiOiOiOi
#'='*20 = '====================='
#end=' ' Serve para não quebrar linha.
#\n Significa Quebra de linha
print('A soma é {}, \nO produto é {}, \nA divisão é {:.3f}'.format(s,m,d),end=' ')
print('\nDivisão inteira é {}, \nE a potencia é {}, \nE a raiz é {}'.format(di,e,raiz))


