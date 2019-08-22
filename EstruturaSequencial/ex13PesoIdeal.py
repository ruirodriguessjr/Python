#Tendo como dados de entrada a altura de uma pessoa, 
#construa um algoritmo que calcule seu peso ideal, 
#usando a seguinte fórmula: (72.7*altura) - 58
sexo = str(input("Informe se sex0 [M] - Masculino e [F]Feminino").upper())
if(sexo == "M"):
	alt = float(input("Informe seu altura: "))
	ideal = (72.7 * alt) - 58
	print("Seu peso ideal é: {:.2f}".format(ideal))
elif(sexo == "F"):
	alt = float(input("Informe seu altura: "))
	ideal = (62.1 * alt) - 44.7
	print("Seu peso ideal é: {:.2f}".format(ideal))
else:
	print("Você é Viadinho!!!")