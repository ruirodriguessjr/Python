#ContandoVogaisEmTupla
palavras = ('Aprender', 'Programar', 'Linguagem', 'Python',
            'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar',
            'Mercado', 'Programador', 'Futuro')
for c in palavras:
	print(f'\nNa palavra {c} temos a vogal ', end='')
	for letra in c:
		if letra in 'aeiou':
			print(letra.lower(), end='')

