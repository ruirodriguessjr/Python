import pymongo
from Atividade import Atividade

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["EscolaDeCursos"]
mycol = mydb["Cursos"]


lista = dict()
lista['descricao'] = str(input("Entre com a Descrição do Curso: "))
lista['data'] = str(input("Entre com Data Inicio do Curso: "))
lista['local'] = str(input("Entre com o Local que será o Curso: "))
lista['tipo'] = str(input("Entre com qual Tipo o Curso é: "))
lista['valor'] = str(input("Entre com o Valor do Curso: "))
lista['participantes'] = str(input("Entre com a Quantidade de Participantes Inscritos: "))


x = mycol.insert_one(lista)

print(x.inserted_id)