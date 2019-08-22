d1 = {}
print(type(d1))
d2 = dict()
print(type(d2))
d1['aaa'] = 1000
print(d1)
d1['bbb'] = 2000
d1['ccc'] = 3000
d1['ddd'] = 4000
print(d1['aaa'])
'''Cada elemento da lista deve estar vinculado 
a um tipo de dado diferente e não a estancias diferentes.
no caso eu tenho 'aaa' vinculado à 1000 e assim sucessivamente.
Dicionários eu normalmente associo eles á uma variavel
cujo eu posso mesmo assim atribuir um valor á mesma.'''
cel = {
    991622323:'Vanessa',
    981029787:'Rui',
    33393834:'Casa',
    991297771:'Ruizão'
    }
print(cel)
print(len(cel))
'''Função Len Conta quantos itens na lista.
Função Del exclui item da lista na posição entre [].'''
#del(cel[991622323])
#print(cel)
'''Função Keys() retorna a chaves, os números relacionados(ex: 991622323).
A Função Values(), retorna só os valores que estao relacionados as chaves(ex: Vanessa).
A Função Get(), retorna o valor quando digitado a chave (ex: 991622323 == Vanessa). '''
print(cel.keys())
print(cel.values())
print(cel.get(991622323))
'''Temos a função Popitem(), onde ela retorna um elemento da nossa chave
e depois exclui da lista. Quantas vezes eu fizer retira de um em um.'''
print(cel)
print(cel.popitem())
print(cel)
print(cel.popitem())
print(cel)
print(cel.popitem())
print(cel)
print(cel.popitem())
print(cel)
'''Para adicionar novos componentes dentro das minhas chaves basta adicionar
a função Update(), ela acrescenta números relacionados em variável para a lista.'''
cel2 = {41844898:'Vó Marly',33356359:'PB Kids'}
cel.update(cel2)
print(cel)
'''Uma lista não pode ser associada a dicionário como chave de valor.'''
