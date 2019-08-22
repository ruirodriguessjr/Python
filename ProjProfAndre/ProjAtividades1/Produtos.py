# coding: utf-8

import pymongo as mongo
import datetime as DT
import uuid

myclient = mongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Produtos"]
mycol = mydb["Dados Produto"]

class Produto:
    def __init__(self, Nome = None, Descricao = None, Preco = None):
        self.Nome = Nome
        self.ID = uuid.uuid4().time_mid
        self.Descricao = Descricao
        self.Preco = Preco
        self.DtEntrada = (DT.datetime.now()).strftime("%Y/%m/%d - %X")

    def setID(self, ID):
        self.ID = ID

    def setDtEntrada(self, DtEntrada):
        self.DtEntrada = DtEntrada

    def getJsonProd(self):
        produto = {
            'Nome': self.Nome,
            '_id': self.ID,
            'Descricao': self.Descricao,
            'Preco': self.Preco,
            'DtEntrada': self.DtEntrada
        }
        return produto

    def toDB(self):
        n = ['Nome', '_id', 'Descricao', 'Preco', 'DtEntrada']
        m = [self.Nome, self.ID, self.Descricao, self.Preco, self.DtEntrada]
        j = dict()
        for i in range(len(n)):
            j[f'{n[i]}'] = m[i]
        print(j)
        x = mycol.insert_one(j)
        print(f'Produto inserido com o ID {x.inserted_id}')