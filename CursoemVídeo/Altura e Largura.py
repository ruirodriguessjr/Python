cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[1;31m'}
altura = float(input('Digite a altura desejada = '))
largura = float(input('Digite a largura desejada = '))
area = altura * largura
tinta = area / 2
print('Sua parede tem dimensão de {}{:.2f}m{} x {}{:.2f}m{}, e sua área corresponde à {}{:.2f}m²{}'.format(cores['branco'], altura, cores['limpa'], cores['azul'], largura, cores['limpa'], cores['amarelo'], area, cores['limpa']))
print('Para pintar toda a parede será necessário {}{:.2f}lts{} de tinta. '.format(cores['pretoebranco'], tinta, cores['limpa']))
