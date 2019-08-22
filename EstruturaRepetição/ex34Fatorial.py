n = int(input('Numero: '))
c = n
f = 1
while c > 0 and c < 61:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')