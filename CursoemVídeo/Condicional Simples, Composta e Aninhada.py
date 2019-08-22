cores = {'vermelho':'\033[1;31m','limpa':'\033[m',}
nome = str(input('Digite seu nome? '))
if nome == 'Rui Rodrigues':
    print('Seu nome não é comum de se ver...')
elif nome == 'Aline':
    print('Seu nome é muito comum...')
elif nome == 'Renato':
    print('Você é um cara muito mais importante, pois é Médico...')
else:
    print('Seu nome é tradicional assim como os demais...')
print('Tenha um bom dia, {}{}{}!!!'.format(cores['vermelho'], nome, cores['limpa']))
'''Quando tratamos apenas com o (IF) = Temos uma Estrutura Condicional Simples...
Quando tratamos com o (IF e ELSE) = Temos uma Estrutura Condicional Composta...
Quando tratamos com o (IF, ELIF, ELSE) = Temos uma Estrutura Condicional Aninhada, que significa: 
que temos uma condição dentro da condição e por fim a contradição'''