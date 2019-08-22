#QtdMediaMaiorMenor.py
resp = 'S'
soma = media = cont = maior = menor = 0
while resp in 'Ss':
	n = int(input('Informe um número: '))
	cont += 1
	soma = soma + n
	if cont == 1:
		maior = menor = n
	else:
		if n > maior:
			maior = n
		if n < menor:
			menor = n
	resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))