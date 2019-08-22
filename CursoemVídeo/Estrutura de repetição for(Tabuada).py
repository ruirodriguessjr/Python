num = int(input("Digite um número para saber sua tabuada: "))
for c in range(0, 11):
    r = num * c
    print('{} x {} = {}'.format(num, c, r))

