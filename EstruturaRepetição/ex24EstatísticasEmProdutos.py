#EstatísticasEmProdutos
print('-'*30)
print('  Loja Super Baratão ')
print('-'*30)
mais = totmil = soma = menor = maior= menorPreco = 0
barato = ''
while True:
	nome = str(input('Nome do Produto: '))
	preco = float(input('Preço: R$ '))
	mais += 1
	soma = soma + preco
	if preco > 1000:
		totmil += 1
	if mais == 1 or preco < menor:
		menor = preco
		barato = nome
	resp = ' '
	while resp not in "SN":
		resp = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
	if resp == 'N':
			break
print('---------- Fim do Programa -----------')
print(f'O total da compra foi R$ {soma} reais. ')
print(f'Temos {mais} produto(s) custando mais de R$ 1000.00 reais.')
print(f'O produto mais barato foi a {barato} que custa R$ {menor:.2f} reais.')