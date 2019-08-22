'''PRÉ-MIRIM: até 8 anos
MIRIM: 9 e 10 anos
PETIZ: 11 e 12 anos
INFANTIL: 13 e 14 anos
JUVENIL: 15 e 16 anos
JUNIOR: 17 a 19 anos
INFANTO-JUVENIL: 13 a 16 anos
JUNIOR-SÊNIOR: 17 anos em diante'''
from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('O atleta nasceu em {}, e tem {} anos.'.format(nasc, idade))
if idade <= 12:
    print('Classificação: Mirim')
elif idade >= 13 and idade < 15:
    print('Classificação: Juvenil')
elif idade >= 15 and idade < 18:
    print('Classificação: Infantil')
elif idade <= 18 and idade < 20:
    print('Classificação: Junior-Sênior')
else:
    idade >= 20
    print('Classificação: Adulto.')


