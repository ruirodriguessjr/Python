#Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
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