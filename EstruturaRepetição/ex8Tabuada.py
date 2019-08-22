#Tabuada

tab = int(input("Informe a tabuada que deseja fazer: "))
for i in range(0, 11):
	print("{} X {} = {}".format(tab, i, tab*i))