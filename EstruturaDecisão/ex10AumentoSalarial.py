#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
#e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input("Informe seu salário: "))
if(salario <= 280.00):
	reajuste = ((salario * 20) / 100)
	newSalario = salario + reajuste
	print("Seu salário antes do reajuste era de R$ {:.2f} reais.".format(salario))
	print("O reajuste do seu salário será de R$ {:.2f} reias.".format(reajuste))
	print("Seu novo salário será de R$ {:.2f} reais.".format(newSalario))
elif(salario > 280.00 and salario <= 700.00):
	reajuste = ((salario * 15) / 100)
	newSalario = salario + reajuste
	print("Seu salário antes do reajuste era de R$ {:.2f} reais.".format(salario))
	print("O reajuste do seu salário será de R$ {:.2f} reias.".format(reajuste))
	print("Seu novo salário será de R$ {:.2f} reais.".format(newSalario))
elif(salario > 700.00 and salario <= 1500.00):
	reajuste = ((salario * 10) / 100)
	newSalario = salario + reajuste
	print("Seu salário antes do reajuste era de R$ {:.2f} reais.".format(salario))
	print("O reajuste do seu salário será de R$ {:.2f} reias.".format(reajuste))
	print("Seu novo salário será de R$ {:.2f} reais.".format(newSalario))
elif(salario > 1500.00):
	reajuste = ((salario * 5) / 100)
	newSalario = salario + reajuste
	print("Seu salário antes do reajuste era de R$ {:.2f} reais.".format(salario))
	print("O reajuste do seu salário será de R$ {:.2f} reias.".format(reajuste))
	print("Seu novo salário será de R$ {:.2f} reais.".format(newSalario))
