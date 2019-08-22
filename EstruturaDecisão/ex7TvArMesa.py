#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
tv = float(input("Informe o preço da tv: "))
ar = float(input("Informe o preço da ar: "))
mesa = float(input("Informe o preço da mesa: "))
if(tv < ar and tv < mesa):
	print("O preço da tv é: R$ {:.2f} reais. \nO preço do ar é: R$ {:.2f} reais. \nO preço da mesa é: R$ {:.2f} reais.".format(tv, ar, mesa))
	print("Você deve comprar a TV, por ser o menor preço!")
elif(ar < tv and ar < mesa):
	print("O preço da ar é: R$ {:.2f} reais. \nO preço do tv é: R$ {:.2f} reais. \nO preço da mesa é: R$ {:.2f} reais.".format(ar, tv, mesa))
	print("Você deve comprar a AR, por ser o menor preço!")
elif(mesa < tv and mesa < ar):
	print("O preço da mesa é: R$ {:.2f} reais. \nO preço do tv é: R$ {:.2f} reais. \nO preço da ar é: R$ {:.2f} reais.".format(mesa, tv, ar))
	print("Você deve comprar a MESA, por ser o menor preço!")