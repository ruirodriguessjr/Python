real = float(input("Quanto de dinheiro tem na carteira: "))
dolar = real/3.78
euro = real/4.28
print("Você tem R$ {:.2f} reais.".format(real))
print("Pode comprar US$ {:.2f} dólares.".format(dolar))
print("Pode comprar EUR {:.2f} euros.".format(euro))
