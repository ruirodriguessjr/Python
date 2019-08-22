import pymongo as mongo
from datetime import date

myclient = mongo.MongoClient("mongodb://localhost:27017/")
mydb3 = myclient["Vendas"]
mycol3 = mydb["Dados Vendas"]

class venda:

    #Método Construtor Com Parâmetros
    def __init__(self, id, descricao, produto, funcionario, cliente, data):
        self.id = id
        self.descricao = descricao
        self.produto = produto
        self.funcionario = funcionario
        self.cliente = cliente
        self.data = date.today()

    def realizarVenda(self, cliente, funcionario, produto):
        self.cliente = cliente
        self.funcionario = funcionario
        self.produto = produto





