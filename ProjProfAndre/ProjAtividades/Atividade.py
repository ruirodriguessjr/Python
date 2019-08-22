class Atividade:

    #Método Construtor
    def __init__(self, id, descricao, data, local, tipo, valor, participantes):
        self.id = id
        self.descicao = descricao
        self.data = data
        self.local = local
        self.tipo = tipo
        self.valor = valor
        self.participantes = participantes

    #Métodos Getters and Setters
    def setId(self, id):
        self.id = id

    def getId(self, id):
        return self.id

    def setDescricao(self, descricao):
        self.descicao = descricao

    def getDescricao(self, descricao):
        return self.descicao

    def setData(self, data):
        self.data = data

    def getData(self, data):
        return self.data

    def setLocal(self, local):
        self.local = local

    def getLocal(self, local):
        return self.local

    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self, tipo):
        return self.tipo

    def setValor(self, valor):
        valor
    def getValor(self, valor):
        return self.valor

    def setParticipantes(self, participantes):
        self.participantes = participantes

    def getParticipantes(self, participantes):
        return self.participantes