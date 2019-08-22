# coding: utf-8

import pymongo as mongo
import uuid

myclient = mongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Clientes"]
mycol = mydb["Dados Cliente"]

class Cliente:
    def __init__(self, Nome = None, Telefone = None, Endereco = None, Cidade = None, Estado = None, DataNasc = None):
        self.Nome = Nome
        self.ID = uuid.uuid4().time_low
        self.Telefone = Telefone
        self.Endereco = Endereco
        self.Cidade = Cidade
        self.Estado = Estado
        self.DataNasc = DataNasc

    def setID(self, ID):
        self.ID = ID

    def getJsonCli(self):
        cliente = {
            'Nome': self.Nome,
            '_id': self.ID,
            'Telefone': self.Telefone,
            'Endereco': self.Endereco,
            'Cidade': self.Cidade,
            'Estado': self.Estado,
            'DataNasc': self.DataNasc
        }
        return cliente

    def toDB(self):
        n = ['Nome', '_id', 'Telefone', 'Endereco', 'Cidade', 'Estado', 'DataNasc']
        m = [self.Nome, self.ID, self.Telefone, self.Endereco, self.Cidade, self.Estado, self.DataNasc]
        j = dict()
        for i in range(len(n)):
            j[f'{n[i]}'] = m[i]
        print(j)
        x = mycol.insert_one(j)
        print(f'Cliente inserido com o ID {x.inserted_id}')