#Faça um programa que calcule o mostre a média aritmética de N notas.

qtd = int(input('Informe quantas notas quer ler: '))
c = 1
soma = n = 0
while c <= qtd:
	while n < 0 and n > 10:
		n = float(input('Informe a {} ª nota: '.format(c)))
		soma = soma + n
		c += 1
media = soma / qtd
print(f'A media das notas é {media:.2f}')
