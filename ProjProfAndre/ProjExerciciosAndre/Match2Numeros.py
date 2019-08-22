from random import randint
cont = 0
while True:
    n1 = randint(0, 100)
    n2 = randint(0, 100)
    if n1 != n2:
        cont += 1
    else:
        print('Match!!!')
        print(f'Os números {n1} e {n2}')
        break
print(f'O nº {n1} e o nº {n2} precisaram de {cont} combinações para dar Match!!!')
