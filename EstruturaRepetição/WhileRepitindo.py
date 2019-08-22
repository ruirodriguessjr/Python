#WhileRepitindo
c = 1
while c < 10:
	print(c, end=' ')
	c += 1
print('Fim')

n = 1
while n != 0:
	n = int(input('Informe um valor: '))
print('Fim')

resp = 'S'
while resp == 'S':
	n = int(input('Informe um valor: '))
	resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]