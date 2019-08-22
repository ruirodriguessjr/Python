#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
#e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador
#e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
#informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.
salario = float(input('Digite seu salário: '))
print('Seu salário antes do reajuste era de R${:.2f}'.format(salario))
if salario <= 280.00:
    novo_salario = salario + ((salario * 20) / 100)
    aumento = novo_salario - salario
    porcentagem = ((novo_salario - salario) / salario) * 100
elif salario > 280.00 and salario < 700.00:
    novo_salario = salario + ((salario * 15) / 100)
    aumento = novo_salario - salario
    porcentagem = ((novo_salario - salario) / salario) * 100
elif salario >= 700.00 and salario < 1500.00:
    novo_salario = salario + ((salario * 10) / 100)
    aumento = novo_salario - salario
    porcentagem = ((novo_salario - salario) / salario) * 100

else: 
    novo_salario = salario + ((salario * 5) / 100)
    aumento = novo_salario - salario
    porcentagem = ((novo_salario - salario) / salario) * 100
print('O salario antes do reajuste era R$ {:.2f}'.format(salario))
print('O percentual de aumento de {:.2f}%'.format(porcentagem))
print('O valor do aumento foi de R$ {:.2f}'.format(aumento))
print('Seu novo salário será de R$ {:.2f}'.format(novo_salario))