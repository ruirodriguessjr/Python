print('='*12)
s = 0
cont = 0
for c in range(1, 7):
    num = int(input('Entre com um número:'))
    if num % 2 == 0:
        s = s + num
        cont = cont + 1
print('Você informou {} números pares e a soma deles é: {}'.format(cont, s))