lista = ['Rui','Vanessa','Maria','Vera','Ruizão','Aline','Vinícius']
print(lista)
lista.reverse()
print(lista)
'''A execução do método reverse() faz com que seja lida a lista de trás pra frente.'''
lista.reverse()
print(lista)
lista.sort()
print(lista)
'''Diz pra eu ordenar a lista de forma organizada teoricamente alfabetica.
Caso eu queira fazer o mesmo só que de sentido oposto do alfabeto segue a função.'''
lista.sort(reverse=True)
print(lista)
'''Para saber a quantidade de elementos da nossa lista basta: '''
print(len(lista))
lista.insert(1, 'Ruizão')
lista.insert(7, 'Ruizão')
print(lista)
print(lista.count('Ruizão'))
print('A quantidade de Ruizão contido na lista é de {} vezes.'.format(lista.count('Ruizão')))
'''Para achar a posição do vetor, ou seja, do indice que deseja dentro da lista, você pode 
usar a função index()'''
print(lista.index('Vera'))
'''Caso eu tenha mais que uma ocorrencia de indice igual dentro da lista
meu index() vai retornar somente a primeira posição, ou seja, onde acontece a primeira
vez a amostra do indice.'''
