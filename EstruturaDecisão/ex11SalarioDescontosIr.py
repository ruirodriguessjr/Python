#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
#mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
#No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        #Salário Bruto: (5 * 220)        : R$ 1100,00
        #(-) IR (5%)                     : R$   55,00  
        #(-) INSS ( 10%)                 : R$  110,00
        #FGTS (11%)                      : R$  121,00
        #Total de descontos              : R$  165,00
        #Salário Liquido                 : R$  935,00

hora = float(input("Informe qual o valor da sua hora de trabalho: "))
qtdHora = int(input("Informe a quantidade de horas que você trabalha por semana: "))
mes = qtdHora * 4
salarioBruto = mes * hora 
if (salarioBruto <= 900):
	ir = (salarioBruto * 0) / 100
	inss = (salarioBruto * 10) / 100
	fgts = (salarioBruto * 11) / 100
	totDescontos = ir + inss
	salarioLiquido = salarioBruto - totDescontos 
	print("""+ Salário Bruto : R$ {:.2f}
	- IR (-) : R$ {:.2f}
	- INSS (10%) : R$ {:.2f}
	- FGTS (11%) : R$ {:.2f}
	- Total de Descontos : R$ {:.2f}
	= Salário Liquido : R$ {:.2f}""".format(salarioBruto, ir, inss, fgts, totDescontos, salarioLiquido))
elif(salarioBruto > 900 and salarioBruto <= 1500):	
	ir = (salarioBruto * 5) / 100
	inss = (salarioBruto * 10) / 100
	fgts = (salarioBruto * 11) / 100
	totDescontos = ir + inss
	salarioLiquido = salarioBruto - totDescontos 
	print("""+ Salário Bruto : R$ {:.2f}
	- IR (5%) : R$ {:.2f}
	- INSS (10%) : R$ {:.2f}
	- FGTS (11%) : R$ {:.2f}
	- Total de Descontos : R$ {:.2f}
	= Salário Liquido : R$ {:.2f}""".format(salarioBruto, ir, inss, fgts, totDescontos, salarioLiquido))
elif(salarioBruto > 1500 and salarioBruto <= 2500):	
	ir = (salarioBruto * 10) / 100
	inss = (salarioBruto * 10) / 100
	fgts = (salarioBruto * 11) / 100
	totDescontos = ir + inss
	salarioLiquido = salarioBruto - totDescontos 
	print("""+ Salário Bruto : R$ {:.2f}
	- IR (10%) : R$ {:.2f}
	- INSS (10%) : R$ {:.2f}
	- FGTS (11%) : R$ {:.2f}
	- Total de Descontos : R$ {:.2f}
	= Salário Liquido : R$ {:.2f}""".format(salarioBruto, ir, inss, fgts, totDescontos, salarioLiquido))
else:
	ir = (salarioBruto * 20) / 100
	inss = (salarioBruto * 10) / 100
	fgts = (salarioBruto * 11) / 100
	totDescontos = ir + inss
	salarioLiquido = salarioBruto - totDescontos 
	print("""+ Salário Bruto : R$ {:.2f}
	- IR (20%) : R$ {:.2f}
	- INSS (10%) : R$ {:.2f}
	- FGTS (11%) : R$ {:.2f}
	- Total de Descontos : R$ {:.2f}
	= Salário Liquido : R$ {:.2f}""".format(salarioBruto, ir, inss, fgts, totDescontos, salarioLiquido))