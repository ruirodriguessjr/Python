preco = int(input("Informe qual o preço do produto: "))
novo = preco - (preco * 5) / 100
print("O preço do produto é: R$ {:.2f} reais. \nE o novo preço com desconto é: R$ {:.2f} reais.".format(preco, novo))