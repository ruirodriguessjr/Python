"""Criar um algoritimo em python e leia um arquivo e realize a seguinte operação:
Arquivo de entrada (sequencial):
Andre 1
Ana 2
João 6
Gerar o seguinte arquivo (com os dados do arquivo):
O ????? conhece ?? linguagens de programação. """

#Criando um arquivo chamado "andre1.txt", e escrevendo nele um texto:
andre = open('andre1.txt', 'w')
texto = []
texto.append('O Andre conhece 1 linguagens de programação. ')
andre.writelines(texto)
andre.close()
andre = open("andre1.txt", "r")
print(andre.read())
print()

#Criando um arquivo chamado "ana2.txt", e escrevendo nele um texto:
ana = open('ana2.txt', 'w')
texto = []
texto.append('A Ana conhece 2 linguagens de programação. ')
ana.writelines(texto)
ana.close()
ana = open("ana2.txt", "r")
print(ana.read())
print()

#Criando um arquivo chamado "joao6.txt", e escrevendo nele um texto:
joao = open('joao6.txt', 'w')
texto = []
texto.append('O João conhece 6 linguagens de programação. ')
joao.writelines(texto)
joao.close()
joao = open("joao6.txt", "r")
print(joao.read())
print()



