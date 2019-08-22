salario = float(input('Qual é o seu salário? '))
aumento = (salario*15/100)
novo = aumento + salario
print('Seu salário passara à valer agora R${:.2f}'.format(novo))
