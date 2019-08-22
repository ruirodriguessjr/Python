lista = list('Rui, Você ainda vai ser muito bem sucedido')
print(lista)
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista1)
lista1 = lista1[1] * lista1[4]
print(lista1)
'''esses são alguns jeitos de ordernar uma lista pelas suas posições.
Posso também fazer isolando um objeto inteiro dentro da lista sem separa- los.
Basta eu acrescentar uma "(,), antes de fechar o parenteses."'''
lista2 = list(('Rui Programador',))
print(lista2)
'''Sem a (,), ele ficaria assim...'''
lista3 = list(('Rui Programador'))
print(lista3)
'''Diferença entre LISTA e TUPLA, é que [Lista é entre cochetes], e (Tupla é entre parenteses).
Posso também utilizar uma lista dentro da lista.'''
lista4 = [['a','b','c'],[1,2,3],[0.1,0.2,0.3]]
print(lista4)
print(lista4[0])
'''Caso eu queira retornar um numero dentro da cadeia da lista.
Ou seja, seleciono a lista dentro da cadeia, e depois seleciono o elemento dentro da lista.'''
print(lista4[0][2])
print(len(lista4))
print(lista4)
'''Caso eu queira adicionar itens concatenar para com a lista eu posso adicionar
tanto no começo quanto no final, nesse caso adicionei a lista o [0] e [6]'''
lista5 = [1,2,3,4,5]
lista5 = [0] + lista5 + [6]
print(lista5)
'''Para facilitar eu tenho uma função que se chamada adiciona direto a lista.
Porém eu só consigo adicionar apenas um objeto(numero)'''
lista5.append(7)
print(lista5)
''' ou eu adiciono uma lista a mais'''
lista5.append([7])
print(lista5)
'''Para excluir um item de uma lista eu posso usar a função del, ela elimina
o item de acordo com a sua posição dentro da lista, mas individualmente.'''
del(lista5[2:4])
print(lista5)
'''caso queira apagar todos os itens da nossa lista, basta seguirmos a seguinte função.'''
lista5.clear()
print(lista5)
'''Temos outra maneira de excluir apenas um item, ele se chama pop().
só que nesse caso sua contagem de exclusão automatica será sempre a ultima expressão.
caso eu queira excluir uma determinada tenho que informar.'''
lista5 = [1,2,3,4,5]
lista5 = [0] + lista5 + [6]
print(lista5)
lista5.pop()
print(lista5)
lista5.pop(0)
print(lista5)
'''Caso eu queira enumerar meus itens de listas posso fazer assim:'''
lista = ['aaa','bbb','ccc','ddd']
print(list(enumerate(lista)))
'''Semelhante ao append(), existe outra função que faz com que eu adicione itens, 
escolhendo a posição onde adiciona- las.'''
lista = ['aaa','bbb','ccc','ddd']
lista.insert(4, 'eee')
print(lista)
'''Para alterar o valor dentro da lista em sua posição, basta eu receber a alteração
como lista, e informar sua posição, assim automaticamente ele altera minha lista.'''
lista[1] = 'bbbbbbb'
print(lista)

