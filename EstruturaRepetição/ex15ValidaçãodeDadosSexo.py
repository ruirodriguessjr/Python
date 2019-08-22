#Validação de Dados Sexo

sexo = str(input("Informe seu sexo: [M/f]: ")).strip().upper()[0]
while sexo not in "MmFf":
	sexo = str(input("Dados Inválidos. Por Favor, Informe seu sexo: [M/f]: ")).strip().upper()[0]
print("sexo {} registrado com sucesso!".format(sexo))


