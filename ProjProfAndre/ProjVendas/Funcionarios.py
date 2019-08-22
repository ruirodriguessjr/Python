# coding: utf-8

import pymongo as mongo
import uuid

myclient = mongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Funcionarios"]
mycol = mydb["Dados Funcionario"]

class Funcionario:
    def __init__(self, Nome = None, Telefone = None, Endereco = None, Cidade = None, Estado = None, DataNasc = None, Salario = None):
        self.Nome = Nome
        self.ID = uuid.uuid4().time_hi_version
        self.Telefone = Telefone
        self.Endereco = Endereco
        self.Cidade = Cidade
        self.Estado = Estado
        self.DataNasc = DataNasc
        self.Salario = Salario

    def setID(self, ID):
        self.ID = ID

    def getJsonFunc(self):
        funcionario = {
            'Nome': self.Nome,
            '_id': self.ID,
            'Telefone': self.Telefone,
            'Endereco': self.Endereco,
            'Cidade': self.Cidade,
            'Estado': self.Estado,
            'DataNasc': self.DataNasc,
            'Salario': self.Salario
        }
        return funcionario

    def toDB(self):
        n = ['Nome', '_id', 'Telefone', 'Endereco', 'Cidade', 'Estado', 'DataNasc', 'Salario']
        m = [self.Nome, self.ID, self.Telefone, self.Endereco, self.Cidade, self.Estado, self.DataNasc, self.Salario]
        j = dict()
        for i in range(len(n)):
            j[f'{n[i]}'] = m[i]
        print(j)
        x = mycol.insert_one(j)
        print(f'Funcionário inserido com o ID {x.inserted_id}')