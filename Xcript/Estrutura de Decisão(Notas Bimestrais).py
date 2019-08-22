#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
#e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) / 2
if media > 9.0 and media <= 10.0:
    print('Entre as notas: {:.2f} e {:.2f}, sua média foi: {:.2f}'.format(n1, n2, media))
    print('Você tirou: A')
    print('Você foi APROVADO!!!')
if media > 7.5 and media <= 9.0:
    print('Entre as notas: {:.2f} e {:.2f}, sua média foi: {:.2f}'.format(n1, n2, media))
    print('Você tirou: B')
    print('Você foi APROVADO!!!')
if media > 6.0 and media <= 7.5:
    print('Entre as notas: {:.2f} e {:.2f}, sua média foi: {:.2f}'.format(n1, n2, media))
    print('Você tirou: C')
    print('Você ficou de RECUPERAÇÃO!!!')
if media > 4.0 and media <= 6.0:
    print('Entre as notas: {:.2f} e {:.2f}, sua média foi: {:.2f}'.format(n1, n2, media))
    print('Você tirou: D')
    print('Você foi REPROVADO!!!')
if media  <= 4 and media == 0:
    print('Entre as notas: {:.2f} e {:.2f}, sua média foi: {:.2f}'.format(n1, n2, media))
    print('Você tirou: E')
    print('Você foi REPROVADO!!!')