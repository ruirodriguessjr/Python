#Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.
valor_hora = float(input('Digite o quanto você ganha por hora: '))
hora_trabalha = float(input('Quantas horas você trabalha no dia: '))
dia = hora_trabalha
semana = dia * 6
mes = semana * 4
salario = (valor_hora * dia) * 30
print('Você trabalha {:.2f}hrs por dia, '
      'no mês você trabalha {:.2f}hrs, '
      'e o seu salário é: R${:.2f}'.format(hora_trabalha, mes, salario))