""""r"- Ler - Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existir

"a" - Anexar - Abre um arquivo para anexar, cria o arquivo se ele não existir

"w" - Write - Abre um arquivo para gravação, cria o arquivo se ele não existir

"x" - Criar - Cria o arquivo especificado, retorna um erro se o arquivo existir"""

#Para abrir um arquivo para leitura basta especificar o nome do arquivo:
f = open("ManipulacaoArquivos.txt")
print(f)

#O código acima é o mesmo que:
a = open("ManipulacaoArquivos.txt", "rt")
#Como "r"para leitura e "t"para texto são os valores padrão, você não precisa especificá-los.

#Para abrir o arquivo, use a open()função interna.

#A open()função retorna um objeto de arquivo,
#que possui um read()método para ler o conteúdo do arquivo:
f = open("ManipulacaoArquivos.txt", "r")
print(f.read())
print("===============================")

#Por padrão, o read()método retorna todo o texto
# mas você também pode especificar quantos caracteres deseja retornar:
f = open("ManipulacaoArquivos.txt", "r")
print(f.read(6))
print(f.read(8).strip())
print("===============================")

#Você pode retornar uma linha usando o readline()método:
f = open("ManipulacaoArquivos.txt", "r")
print(f.readline())
print("===============================")

#Ao ligar readline()duas vezes, você pode ler as duas primeiras linhas:
f = open("ManipulacaoArquivos.txt", "r")
print(f.readline())
print(f.readline())
print("===============================")

#Ao percorrer as linhas do arquivo, você pode ler o arquivo inteiro, linha por linha:
f = open("ManipulacaoArquivos.txt", "r")
for x in f:
  print(x)
print("=================================")

#É uma boa prática sempre fechar o arquivo quando você terminar com ele.
f = open("ManipulacaoArquivos.txt", "r")
print(f.readline())
f.close()
print("=================================")

"""Para gravar em um arquivo existente, você deve adicionar um parâmetro à open()função:

"a" - Anexar - será anexado ao final do arquivo

"w" - Escrever - substituirá qualquer conteúdo existente"""

#Abra o arquivo "ManipulacaoArquivos1.txt" e anexe o conteúdo ao arquivo:
f = open("ManipulacaoArquivos1.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("ManipulacaoArquivos1.txt", "r")
print(f.read())
print("=======================================")

#Abra o arquivo "ManipulacaoArquivos2.txt" e sobrescreva o conteúdo:
f = open("ManipulacaoArquivos2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("ManipulacaoArquivos2.txt", "r")
print(f.read())
print('======================================')

"""Crie um novo arquivo
Para criar um novo arquivo no Python, use o open()método com um dos seguintes parâmetros:

"x" - Create - criará um arquivo, retornará um erro se o arquivo existir

"a" - Anexar - criará um arquivo se o arquivo especificado não existir

"w" - Write - criará um arquivo se o arquivo especificado não existir"""

#Crie um arquivo chamado "myfile.txt":
z = open("myfile.txt", "x")

#Crie um novo arquivo, se ele não existir:
c = open("myfile.txt", "w")

"""Para excluir um arquivo, 
você deve importar o módulo do sistema operacional 
e executar sua os.remove()função:

Exemplo
Remova o arquivo "demofile.txt":"""

import os
os.remove("myfile.txt")

#Para evitar um erro,você pode querer verificar se
#o arquivo existe antes de tentar excluí-lo:

import os
if os.path.exists("demofile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")

#Para excluir uma pasta inteira, use o os.rmdir()método:

import os
os.rmdir("myfolder")
