#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
n1 = float(input("Informe primeira nota: "))
n2 = float(input("Informe segunda nota: "))
m = (n1 + n2) / 2
if (m < 7):
	print("A média do aluno é: {:.2f} e ele está REPROVADO!".format(m))
elif((m >= 7) and (m < 10)):
	print("A média do aluno é: {:.2f} e ele está APROVADO!".format(m))
else:
	print("A média do aluno é: {:.2f} e ele está APROVADO COM DISTINÇÃO!".format(m))