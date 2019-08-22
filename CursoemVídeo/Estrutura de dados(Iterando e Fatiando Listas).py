'''Nesse cado estou usando a função enumarete que também substitui a função range(),
sendo que tanto um quanto o outro a resposta será praticamente a mesma,
dependendo do que eu for usar. Onde eu posso fazer meu contador chamado de IDC(INDICE),
contar juntamente com meus itens da lista,
e somar o valor 10 a cada um dos itens dando o resultado da operação
item da lista + 10.'''
lista = [1,2,3,4,5]
for idc,  item in enumerate(lista):
    lista[idc] += 10
print(lista)
'''O passo do lista é emelhante ao range(),
pois ele tem sua estrutura de inicio, fim e passo.'''