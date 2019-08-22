print('=' * 27)
print('====== SALÁRIO DOS FUNCIONÁRIOS ======')
salario = float(input('Qual é o salário do funcionário esse ano: '))
if salario <= 2500.00:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f}, passa a ganhar R$ {:.2f}'.format(salario, novo))
