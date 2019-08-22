import pymongo

myproduct = pymongo.MongoClient("mongodb://localhost:27017/")
mydb1 = myproduct["Produtos"]
mycol1 = mydb1["Dados do Produto"]

class produto:

    #Método Construtor Com Parâmetros
    def __init__(self, nome, preco, data_entrada, data_saida):
        self.nome = nome
        self.preco = preco
        self.data_entrada = data_entrada
        self.data_saida = data_saida


    #Método Construtor Vazio
    def __init__(self, nome= None, preco= None, data_entrada= None, data_saida= None):
        self.nome = nome
        self.preco = preco
        self.data_entrada = data_entrada
        self.data_saida = data_saida


    #Métodos Getters and Setters
    def setNome(self, nome):
        self.nome = nome

    def getNome(self, nome):
        return self.nome

    def setPreco(self, preco):
        self.preco = preco

    def getPreco(self, preco):
        return self.preco

    def setData_entrada(self, data_entrada):
        self.data_entrada = data_entrada

    def getData_entrada(self, data_entrada):
        return self.data_entrada

    def setData_saida(self, data_saida):
        self.data_saida = data_saida

    def getData_saida(self, data_saida):
        return self.data_saida


    def getJson(self):
        j = dict()
        n = ['Nome', 'Preco', 'Data_Entrada', 'Data_Saida']
        c = [self.nome, self.preco, self.data_entrada, self.data_saida]
        for i in range(len(n)):
            j[f'{n[i]}'] = c[i]
        x = mycol1.insert_one(j)
        print(x.inserted_id)