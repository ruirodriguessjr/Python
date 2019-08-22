cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[1;31m'}
medida = float(input('Digite uma distancia em metros? '))
cm = medida * 100
mm = medida * 1000
print('{}A medida em metros é{} {}{:.2f}m{}{}, que corresponde '
      'à{} {}{:.2f}cm{} {}e que corresponda{} {}{:.2f}mm{}'.format(cores['vermelho'], cores['limpa'], cores['azul'], medida, cores['limpa'], cores['vermelho'], cores['limpa'], cores['amarelo'], cm, cores['limpa'], cores['vermelho'], cores['limpa'], cores['branco'], mm, cores['limpa']))
