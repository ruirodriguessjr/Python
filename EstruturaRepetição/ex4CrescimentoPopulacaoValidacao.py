#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
#Valide a entrada e permita repetir a operação.

a = int(input("Informe a quantidade de população do país A: "))
if(a < 0):
	print("Número de população inexistente!")
while(a < 0):
	a = int(input("Informe a quantidade de população do país A: "))
	if(a < 0):
		print("Número de população inexistente!")
b = int(input("Informe a quantidade de população do país B: "))
if(b < 0):
	print("Número de população inexistente!")
while(b < 0):
	b = int(input("Informe a quantidade de população do país B: "))
	if(b < 0):
		print("Número de população inexistente!")
txa = float(input("Informe a taxa de crescimento da população A: "))
if(txa <= 0):
	print("Taxa Inexistente!")
while(txa <= 0):
	txa = float(input("Informe a taxa de crescimento da população A: "))
	if(txa <= 0):
		print("Taxa Inexistente!")
txb = float(input("Informe a taxa de crescimento da população B: "))
if(txb <= 0):
	print("Taxa Inexistente!")
while(txb <= 0):
	txb = float(input("Informe a taxa de crescimento da população A: "))
	if(txb <= 0):
		print("Taxa Inexistente!")

ano = 0
while (a <= b):
	a += (a * txa) / 100
	b += (b * txb) / 100
	ano += 1

print("População de A: {} habitantes.".format(a))
print("População de B: {} habitantes.".format(b))
print ( "A ultrapassa ou iguala a B em {} anos.".format(ano))