print('='*27)
print('==== Lista de Compras =====')
print('='*27)
preco = float(input('Preço total das compras: R$'))
print('''Qual a forma de pagamento que deseja realizar:
[1] à vista Dinheiro/Cheque com 10% de desconto. '
[2] à vista com cartão com 5% de desconto. ' 
[3] em até 2x no cartão: preço normal.' 
[4] em até 3x até 5x no cartão com acréscimo de 20% de juros.''')
opcao = int(input('Qual é a opção: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('O preço total que era R${:.2f}, agora passa a ser com 10% de desconto R${:.2f}.'.format(preco, total ))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('O preço total que era R${:.2f}, agora passa a ser com 5% de desconto R${:.2f}.'.format(preco, total))
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x e a parcela será de R${:.2f}'.format(parcela))
    print('\nSua compra no final das parcelas será de R${:.2f} SEM JUROS.'.format(total))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcela = total / 3
    print('O valor da parcela em 3x é R${:.2f}, e o total a ser pago é R${:.2f}'.format(parcela, total))
else:
    total = 0
    totalparcelas = 0
    parcela = 0
    print('Opção escolhida não Disponível.')
    print('Total de parcelas foi {}x de R${:.2f}, e o valor final a ser pago será R${:.2f}'.format(totalparcelas, parcela, total))
