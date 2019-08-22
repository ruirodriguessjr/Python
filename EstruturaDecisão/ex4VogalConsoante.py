#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input("Informe uma letra: ").lower())
if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra =="u"):
	print("A letra digitada é uma vogal!")
else:
	print("A letra digitada não é uma vogal!")
