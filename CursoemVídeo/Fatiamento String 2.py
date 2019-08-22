'''Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(),
transformações com replace(), upper(), lower(), capitalize(), title(), strip(),
junção com join().'''
'''Analise de texto:'''
frase = ('Curso em vídeo python')
print(len(frase))
'''Mostra o tamanho da frase'''
frase = ('Curso em vídeo python')
print(frase.count('o'))
'''Conta quantas vezes tem o caracter dentro da variável, sendo que o programa
difere se são letras maiúsculas das minúsculas.
Eu posso fazer a contagem das letras que eu quero achar e posso também 
já fazer o fatiamento junto como por exemplo abaixo:'''
frase = ('Curso em vídeo python')
print(frase.count('o',0,21))
frase = ('Curso em vídeo python')
print(frase.find('android'))
'''find() me mostra a posição onde começa o que foi pedido dentro da função
no caso ele me mostra onde inicia o p = pyt que foi solicitado.'''
'''Quando eu solicito em find('Android'), ou seja uma palavra que não está
dentro da minha variável, ele retorna o valor -1, 
dizendo que essa palavra não se encontra dentro da variável.'''
frase = ('Curso em vídeo python')
print('Curso' in frase)
'''Quando usa o operador (in) ele retorna valor verdadeiro ou falso 
(True, False)'''
'''Transformação de texto'''
frase = ('Curso em vídeo python')
print(frase.replace('python', 'android'))
'''Essa função faz com que se troque a string uma pela a outra. '''
frase = ('Curso em vídeo python')
print(frase.upper())
'''Ele mantém as strings maiúsculas e as minúsculas ele as torna maiúsculas.'''
frase = ('Curso em vídeo python')
print(frase.lower())
'''Já a função lower() faz ao contrário, mantém as minúsculas e transformam
as maiúsculas em minúsculas.'''
frase = ('Curso em vídeo python')
print(frase.capitalize())
'''Ele transforma todas em minúsculas e deixa somente a primeira letra 
do texto em maiúscula.'''
frase = ('Curso em vídeo python')
print(frase.title())
'''Diferente do capitalize(), o title() deixa todas as letras que estão 
separadas por espaço e transforma a primeira letra de cada palavra em maiúscula.'''
frase = ('         Curso em vídeo python         ')
print(frase.rstrip())
'''Essa função elimina os espaços na string mesmo os espaços no meio de algo,
 em paralelo com essa função temos
a função que elimina os espaços para a direita e pra esquerda, usando
rstrip = elimina os espaços da direita, e
lstrip = elimina os espaços da esquerda.'''
'''Divisão de texto:'''
frase = ('Curso em vídeo python')
print(frase.split())
'''Ocorre uma divisão dentro da string considerando os espaços,
ele divide em blocos cada palavra, iniciando a contagem dos caracteres
palavra por palavra, gerando uma lista dentro da cadeia de palavras. 
Dentro da função split() eu posso criar um novo objeto(variavel)
e dividir minhas palavras e ao mesmo tempo mostrar
 algo dentro delas que já está apresentado. Exemplo:'''
frase = ('Curso em vídeo python')
dividido = frase.split()
print(dividido[2])
frase = ('Curso em vídeo python')
print('-'.join(frase.split()))
'''Quando utilizo essa função faço a junção das palavras
ultilizando em seus espaços a junção de algum simbolo ou letra, ou número.'''
'''Lembrando que eu sempre posso ultilizar uma função dentro da outra, 
sem alterar sua funcionalidade e sua origem apenas incrementando melhor 
meu algoritmo.'''
frase = ('Curso em vídeo no python')
print(frase[-1])
print(frase[0:31:1])
'''O zero representa a posição inicial da minha amostra, o 31 a posição final,
e o 1 o pulo que eu quero dar dentro da contagem de strings.'''
s = 'Interando strings'
for c in s:
    print(c)

s = 'interando strings'
indice = 0
while indice < len(s):
    print(indice, s[indice])
    indice += 1

for k,v in enumerate('Ruizão'):
    print(dict(enumerate('{}'.format('Ruizão'))))
    print(k, v)
'''Enumeração de caractere'''