#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
from datetime import date
print('=' * 27)
print('====== ANO BISSEXTO =======')
print('=' * 27)
ano = int(input('Digite um ano para saber se ele é bissexto ou não: '))
if ano == 0:
    ano = date.today().year
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto.'.format(ano))
else:
    print('O ano {} não é Bissexto.'.format(ano))