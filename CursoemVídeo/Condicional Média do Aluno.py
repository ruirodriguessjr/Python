n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Aluno tirou nota {:.1f} e {:.1f} e sua média foi {}.'.format(n1, n2, m))
    print('REPROVADO.')
elif m >= 5 and m < 7:
    print('Aluno tirou nota {:.1f} e {:.1f} e sua média foi {}.'.format(n1, n2, m))
    print('RECUPERAÇÃO.')
else:
    m >= 7
    print('Aluno tirou nota {:.1f} e {:.1f} e sua média foi{}.'.format(n1, n2, m))
    print('APROVADO.')