# coding: utf-8

import pymongo as mongo
import datetime as DT
import uuid

myclient = mongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Vendas"]
mycol = mydb["Dados Venda"]

class Venda:
    def __init__(self, Descricao = None, Produto = None, Cliente = None, Funcionario = None):
        self.ID = uuid.uuid4().clock_seq
        self.Descricao = Descricao
        self.Data = (DT.datetime.now()).strftime("%Y/%m/%d - %X")
        self.Produto = Produto
        self.Cliente = Cliente
        self.Funcionario = Funcionario

    def toDB(self):
        n = ['_id', 'Descricao', 'Data', 'Produto', 'Cliente', 'Funcionario']
        m = [self.ID, self.Descricao, self.Data, self.Produto, self.Cliente, self.Funcionario]
        j = dict()
        for i in range(len(n)):
            j[f'{n[i]}'] = m[i]
        print(j)
        x = mycol.insert_one(j)
        print(f'Venda inserido com o ID {x.inserted_id}')