#AnáliseDeDadosDoGrupo
tot18 = 0
totH = 0
totM20 = 0
while True:
	print('-'*27)
	print('  CADASTRE UMA PESSOA  ')
	print('-'*27)
	idade = int(input('Idade: '))
	sexo = ' '
	while sexo not in 'MF':
		sexo = str(input("Informe seu sexo: [M/f]: ")).strip().upper()[0]
		if idade >= 18:
			tot18 += 1
		if sexo == 'M':
			totH += 1
		if sexo == 'F' and idade < 20:
			totM20 += 1
	resp = ' '
	while resp not in "SN":
		resp = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
	if resp == 'N':
			break
			
		
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao total temos {totH} homen(s) cadastrados.')
print(f'E temos {totM20} com menos de 20 anos.')
