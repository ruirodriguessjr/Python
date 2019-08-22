x = range(1, 10)
if (11 in x):
    print(True)
else:
    print(False)
'''Função in quer saber se um valor está contido dentro da minha lista...
Caso queira fazer o valor invertido usar (not in),
para saber se o valor nao está contido dentro da lista.'''
y = range(1, 10)
if (11 not in y):
    print(True)
else:
    print(False)
'''Para saber se 2 valores(informações) diferentes estão dentro da minha lista
uso a expressão (AND) = OPERADOR DE CONJUNÇÃO.'''
a = range(1, 10)
if (1 and 2 in a):
    print(True)
else:
    print(False)
'''Para saber se 1 de 2 valores(informações) diferentes estão dentro da minha lista
uso a expressão (OR) = OPERADOR DE DISJUNÇÃO.'''
b = range(1, 10)
if (10 or 1 in b):
    print(True)
else:
    print(False)
'''Quando eu ultilizo o OR para saber se a expressão logica é TRUE ou FALSE
tenho que ultilizar elas de maneira estruturada por ordem se não ela retorna false
para toda a expressão.'''
c = range(1, 5)
if 11 or 33 in c:
    print(True)
else:
    print(False)
