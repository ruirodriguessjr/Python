#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


nome = str(input("Informe seu Nome: ").lower().strip())
if(len(nome) <= 3):
	print("Informe Novamente!")
while(len(nome) <= 3):
	nome = str(input("Informe seu Nome: ").lower().strip())
	print("Informe Novamente!")

idade = int(input("Informe sua Idade: "))
while(idade < 0 or idade > 150):
	idade = int(input("Idade fora dos Parâmetros. Informe sua Idade: "))

salario = float(input('Informe seu salario: '))
while(salario <= 0):
	salario = float(input('Salário Inexistente. Informe seu salario: '))

sexo = str(input("Informe seu sexo: [F] - Feminino [M] - Masculino: ")).strip().upper()[0]
while sexo not in "MmFf":
	if (sexo == "Ff"):
		break
	elif(sexo == "Mm"):
		break
	else:
		print("Informe Novamente!")


estadoCivil = str(input("Informe seu estado civil: s - Solteiro, c - Casado, v - Viúvo, d - Divorciado: ")).strip().upper()[0]
while(estadoCivil not in "SsCcVvDd"):
	estadoCivil = str(input("Informe seu estado civil: s - Solteiro, c - Casado, v - Viúvo, d - Divorciado: ")).strip().upper()[0]
	if(estadoCivil == "s"):
		break
	elif(estadoCivil == "c"):
		break
	elif(estadoCivil == "v"):
		break
	elif(estadoCivil == "d"):
		break
	else:
		print("Estado Civil Desconhecido. Informar Novamente!")
		
print("Seu nome é: {}".format(nome))
print("Sua idade é: {}".format(idade))
print("Seu salário é: R$ {:.2f}".format(salario))
print("Seu sexo é: {}".format(sexo))
print("Seu estado Civil: {}".format(estadoCivil))