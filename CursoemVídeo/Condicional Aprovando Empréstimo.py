from time import sleep
print('='*27)
print('Simulador de Empréstimo')
print('='*27)
emprestimo = float(input('Qual o valor do empréstimo: '))
tempo = int(input('Em quantos anos pretende quitar esse empréstimo: '))
salario = float(input('Qual o valor do seu salário: '))
prestacao = (emprestimo / tempo) / 12
minimo = salario * 30 / 100
print('Para pagar um empréstimo no valor de R${:.2f} em {} anos, '
      'sua prestação será de R${:.2f} '.format(emprestimo, tempo, prestacao))
if prestacao <= minimo:
    sleep(2)
    print('PROCESSANDO..........')
    print('\033[1;32m', 'Empréstimo APROVADO!!!!!!!!''\033[m')
else:
    sleep(2)
    print('PROCESSANDO..........')
    print('\033[1;31m', 'Emprestimo NEGADO!!!''\033[m')
