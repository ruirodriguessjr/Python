class Calculadora:

    #Método Construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #Métodos Getters and Setters
    def setA (self, a):
        self.a = a

    def getA(self):
        return self.a

    def setB(self, b):
        self.b = b

    def getB(self):
        return self.b

    def somar(self):
        return self.a + self.b

    def subtrair(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        return self.a / self.b