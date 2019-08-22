print('=-'*15)
print('=== Números Multiplos de 3 ===')
print('=-'*15)
s = 0
cont = 0
for c in range(1, 501, 2):
     if c % 3 == 0:
        s = s + c
        cont = cont + 1

print('A soma de todos os {} valores solicitados é {}'.format(cont, s))
