#Faça um programa para o cálculo de uma folha de pagamento,
#sabendo que os descontos são do Imposto de Renda,que depende do salário bruto
#(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
#mas não é descontado (é a empresa que deposita).
#O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
#No exemplo o valor da hora é 5 e a quantidade de hora é 220.
print('='* 30)
print('===== Folha de Pagamento =====')
print('='* 30)
horas = float(input('Horas trabalhadas no dia: '))
semana = horas * 6 #quantidade de dias na semana.
mes = semana * 4 #quantidade de semanas no mês.
valor_hora = float( input('Valor da hora trabalhada: '))
salario_bruto = valor_hora * mes
print(salario_bruto)
sindicato = (salario_bruto * 3) / 100
fgts = (salario_bruto * 8) / 100
inss = (salario_bruto * 11)/ 100
ir = 0
porcentagem = 0
if salario_bruto <= 900.00:
    print('Isento de Imposto de Renda!!! ')
elif salario_bruto > 900.00 and salario_bruto <= 1500.00:
    ir = (salario_bruto * 5) / 100
    porcentagem = (ir / salario_bruto) * 100
elif salario_bruto > 1500.00 and salario_bruto <= 2500.00:
    ir = (salario_bruto * 10) / 100
    porcentagem = (ir / salario_bruto) * 100
else:
    ir = (salario_bruto * 20) / 100
    porcentagem = (ir / salario_bruto) * 100
descontos = sindicato + fgts + inss + ir
salarioLiq = salario_bruto - descontos
print('Salário Bruto: ({} * {})               R$ {:.2f}'.format(valor_hora, mes, salario_bruto))
print('(-)IR ({:.2f})%                              R$ {:.2f}'.format(porcentagem, ir))
print('(-)Inss (11.00%)                            R$ {:.2f}'.format(inss))
print('(-)Fgts (8.00%)                             R$ {:.2f}'.format(fgts))
print('(-)Sindicato (3.00%)                        R$ {:.2f}'.format(sindicato))
print('Total dos descontos                         R$ {:.2f}'.format(descontos))
print('Salário Líquido                             R$ {:.2f}'.format(salarioLiq))