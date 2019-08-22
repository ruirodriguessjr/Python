#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.
hora = float(input("Informe qual o valor da sua hora de trabalho: "))
qtdHora = int(input("Informe a quantidade de horas que você trabalha por semana: "))
mes = qtdHora * 4
salario = mes * hora 
print("Você trabalha {:.2f} horas por mês.\nE seu salário é: R$ {:.2f} reais.".format(mes, salario))
