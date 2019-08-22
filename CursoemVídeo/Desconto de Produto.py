preço = float(input('Quanto custa esse produto? '))
desc = (preço * 5) / 100
valor = preço - desc
print('O preço do produto que custava R${:.2f},\nAgora com 5% de desconto vai custar R${:.2f} '.format(preço, valor))
