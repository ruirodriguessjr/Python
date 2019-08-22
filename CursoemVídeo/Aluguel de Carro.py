cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'azul':'\033[1;34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[1;31m'}
dias = int(input('Quantos dias alugado: '))
km = float(input('Quantos Km foram rodados: '))
pago = (dias * 60)+(km * 0.15)
print('{}O total a ser pago foi de{} {}{:.2f}{}'.format(cores['vermelho'], cores['limpa'], cores['azul'], pago, cores['limpa']))

