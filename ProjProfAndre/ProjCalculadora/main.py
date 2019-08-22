from Calculadora import Calculadora

def imprimir():
    print('='*20)
    print(f'Valor de A: {calculo.getA()}')
    print(f'Valor de B: {calculo.getB()}')
    print('As 4 operações com os valores passados são:')
    print(f' + = {calculo.somar()}')
    print(f' - = {calculo.subtrair()}')
    print(f' * = {calculo.multiplicar()}')
    print(f' / = {calculo.dividir()}')

# Instancear Classe Calculadora
calculo = Calculadora(1, 2)


# Imprimir Dados
imprimir()

#Alterar Informações
calculo.setA(4)
calculo.setB(5)

# Imprimir Dados
imprimir()