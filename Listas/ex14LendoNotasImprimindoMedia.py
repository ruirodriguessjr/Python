#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


listaNotas = []
media = 0
print ('Informe as 4 notas')
for i in range(4):
	listaNotas.append(float(input('Nota '+ str(i+1) + ':')))
	media += listaNotas[i]
media = media/4
print (listaNotas) 
print (media)