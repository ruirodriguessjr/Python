#Faça um Programa que pergunte em que turno você estuda. 
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
turno = str(input("Informe [M] - Matutino ou [V] - Vespertino ou [N] - Noturno: ").lower())
if(turno == "m"):
	print("Bom Dia!")
elif(turno == "v"):
	print("Boa Tarde!")
elif(turno == "n"):
	print("Boa Noite!")
else:
	print("Valor Inválido, Seu Viadinho!")