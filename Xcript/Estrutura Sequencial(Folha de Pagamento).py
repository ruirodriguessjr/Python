#Faça um Programa que pergunte quanto você ganha por hora
#e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês,
#sabendo-se que são descontados:
#11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.
print('='*30)
print('===== Folha de Pagamento =====')
print('='*30)
valor_hora = float(input('Digite o quanto você ganha por hora: '))
hora_trabalha = float(input('Quantas horas você trabalha no dia: '))
dia = hora_trabalha
semana = dia * 6
mes = semana * 4
salario = (valor_hora * dia) * 30
ir = (salario * 11) / 100
inss = (salario * 8) / 100
sindic = (salario * 5) / 100
print('Seu salário é de: R${:.2f}'.format(salario))
salarioLiq = ((((salario - ir) - inss) - sindic))
print('Já descontado R${:.2f} de Importo de Renda,'
      ' R${:.2f} de INSS e R${:.2f} de Sindicato.'.format(ir, inss, sindic))
print('Você recebeu de salário líquido R${:.2f}'.format(salarioLiq))