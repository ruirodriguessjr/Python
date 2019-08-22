cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[1;31m'}
nome = input('Qual é o seu nome? ')
print('{}Muito prazer em te conhecer {}{}'.format(cores['vermelho'], nome, cores['limpa']))
print('{}Muito prazer em te conhecer {:<20}!!!{}'.format(cores['vermelho'], nome, cores['limpa']))
print('{}Muito prazer em te conhecer {:>20}!!!{}'.format(cores['vermelho'], nome, cores['limpa']))
print('{}Muito prazer em te conhecer {:^20}!!!{}'.format(cores['vermelho'], nome, cores['limpa']))
print('{}Muito prazer em te conhecer {:=^20}!!!{}'.format(cores['vermelho'], nome, cores['limpa']))

