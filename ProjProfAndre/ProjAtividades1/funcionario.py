import pymongo as mongo

myclient = mongo.MongoClient("mongodb://localhost:27017/")
mydb2 = myclient["Funcionario"]
mycol2 = mydb["Dados Funcionario"]

class funcionario:

    #Método Construtor
    def __init__(self, nome, telefone, endereco, cidade, estado, dataNasc, salario):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.dataNasc = dataNasc
        self.salario = salario


    #Métodos Getters and Setters
    def setNome(self, nome):
        self.nome = nome

    def getNome(self, nome):
        return self.nome

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getTelefone(self, telefone):
        return self.telefone

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco(self, endereco):
        return self.endereco

    def setCidade(self, cidade):
        self.cidade = cidade

    def getCidade(self, cidade):
        return self.cidade

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self, estado):
        return self.estado

    def setDataNasc(self, dataNasc):
        self.dataNasc = dataNasc

    def getDataNasc(self):
        return self.dataNasc

    def setSalario(self, salario):
        self.salario = salario

    def getSalario(self):
        return self.salario

    def __str__(self):
        return Funcionario {
            "Nome":
        }

    def getJson(self):
        j = dict()
        n = ['Nome', 'Telefone', 'Endereco', 'Cidade', 'Estado', 'DataNasc', 'Salario']
        c = [self.nome, self.telefone, self.endereco, self.cidade, self.estado, self.dataNasc, self.salario]
        for i in range(len(n)):
            j[f'{n[i]}'] = c[i]
        x = mycol2.insert_one(j)
        print(x.inserted_id)