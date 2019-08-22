#Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
print('='*30)
print('== Número do Dia da Semana ===')
print('='*30)
print('[1] - Domingo\n'
      '[2] - Segunda\n'
      '[3] - Terça\n'
      '[4] - Quarta\n'
      '[5] - Quinta\n'
      '[6] - Sexta\n'
      '[7] - Sábado')
opcao = int(input('Digite o número respectivo da semana desejada: '))
if opcao == 1:
    print('Bom Domingo pra você!!!')
elif opcao == 2:
    print('Boa Segunda pra você!!!')
elif opcao == 3:
    print('Boa Terça pra você!!!')
elif opcao == 4:
    print('Boa Quarta pra você!!!')
elif opcao == 5:
    print('Boa Quinta pra você!!!')
elif opcao == 6:
    print('Boa Sexta pra você!!!')
elif opcao == 7:
    print('Bom Sábado pra você!!!')
else:
    print('Opção Indesejada!!!')

