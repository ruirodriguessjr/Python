#Lendo Notas

cont = nota = soma = 0

while True:
	nota = int(input('Informe uma nota, para sair informe valor diferente de nota: '))
	if nota < 0 or nota > 10:
		break
	if nota >= 0 and nota <= 10:
		soma += nota
		cont += 1
media = soma / cont
print(f'A média das notas são: {media:.2f}')