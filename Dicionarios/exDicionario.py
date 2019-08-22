print('Criando um Dicionário:')
dados = {'Nome':'Rui', 'Idade':'31', 'Sexo':'M'}
print(dados)
print('Imprimindo apenas um item pelo nome atributo dele:')
print(dados['Nome'])
print('Adicionando um item ao Dicionario:')
dados['Esposa'] = 'Vanessa'
print(dados)
print('Deletando item do Dicionario:')
del dados['Sexo']
print(dados)

filme1 = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas'
}
filme2 = {
    'titulo': 'Avangers',
    'ano': 2012,
    'diretor': 'Jass Whendon'
}
filme3 = {
    'titulo': 'Matrix',
    'ano': 1999,
    'diretor': 'Wachowski'
}
print('Pegando Tipos de Parâmetros diferentes do meu Dicinario:')
print(filme1.values())
print(filme1.keys())
print(filme1.items())
print('Estrutura de Repetição com Dicionário:')
for keys, values in filme1.items():
    print(f'O {keys} é {values}')
print('Adicionando meus dicionarios em listas:')
locadora = list()
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)
print('Imprimindo itens dentro de cada posição da lista.')
print('Cada posição é um dicionário inteiro.')
print(locadora[0]['ano'])
print(locadora[1]['titulo'])
print(locadora[2]['diretor'])

pessoas = {'nome':'Rui', 'sexo':'M', 'idade':31}
print(pessoas)

for i in pessoas.keys():
    print(i)
print()
for i in pessoas.values():
    print(i)
print()
for i, j in pessoas.items():
    print(i, j)
print()
for i in pessoas.items():
    print(i)
print()
for i, j in pessoas.items():
    print(f'{i} = {j}')
print()

print('Método copy() faz com que eu copie o item de de dicionario ou lista para outro.')
print('Diferente de quando eu copiava em lista assim [:].')
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    print(e)
print()
print('Passando os valores do dicionario para uma lista')
print('Imprimindo o dicionario formatado dentro da lista')
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
