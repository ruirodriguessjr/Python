comp = float(input('Digite o comprimento da pista em km: '))
voltas = int(input('Digite total de voltas a serem percorridas: '))
abast = int(input('Digite o número de Abastecimentos: '))
consumo = float(input('Qual a capacidade do tanque do carro em Litros: '))
consumo = ((voltas * comp) / consumo)
comp = (comp * 1000) * voltas

print('Você percorreu um total de {:.2f}m'.format(comp))
print('Seu consumo será de {:.2f}Km/L'.format(consumo))

