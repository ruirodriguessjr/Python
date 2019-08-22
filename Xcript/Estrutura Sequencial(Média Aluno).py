#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
n3 = float(input('Terceira Nota: '))
n4 = float(input('Quarta Nota: '))
media = (n1 + n2 + n3 + n4) / 4
if media <= 5:
    print('Sua média foi {:.2f}. Reprovado!!!'.format(media))
elif (media > 5) and (media <= 7):
    print('Sua média foi {:.2f}. Recuperação!!!'.format(media))
else:
    print('Sua média foi {:.2f}. Aprovado'.format(media))