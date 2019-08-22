#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
#mostrando uma mensagem de erro e voltando a pedir as informações.

nome = str(input("Informe seu nome: ").lower())
senha = str(input("Informe uma senha: ").lower())
if(nome == senha):
	print("Nome igual a senha. Digite Novamente!")
while(nome == senha):
	nome = str(input("Informe seu nome: ").lower())
	senha = str(input("Informe uma senha: ").lower())
	if(nome == senha):
		print("Nome igual a senha. Digite Novamente!")
print("O nome difitado foi: {}".format(nome))
print("A senha digitada foi: {}".format(senha))