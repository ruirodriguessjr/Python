#charset-utf8

#Vetores do Programa
listaFilmes = []
listaAvaliacoes = []

#Dicionário do Programa
filmes = {}

#Variáveis
opcao = 0
avalia = 0

#Inicio do Programa
while opcao != 8:
    print("============================================")
    opcao = int(input('[1] - Inserir Filme\n'
                    '[2] - Listar Filmes Inseridos\n'
                    '[3] - Excluir Filme\n'
                    '[4] - Inserir Avaliação\n'
                    '[5] - Listar Avaliações\n'
                    '[6] - Associar Avaliação ao Filme\n'
                    '[7] - Imprimir Relatório\n'
                    '[8] - Sair\n'
                    'Informe Opção: '))
    if opcao == 1:
        listaFilmes.append(str(input('Qual o Nome do Filme: ')))
    elif opcao == 2:
        for c in enumerate(listaFilmes):
            print(f'Filme: {c}')
    elif opcao == 3:
        pos = int(input('Informe qual Filme quer Excluir seu Número Correspondente: '))
        listaFilmes.pop(pos)
        for c in enumerate(listaFilmes):
            print(f'Filme: {c}')
    elif opcao == 4:
        print("============================================")
        print('Lista de filmes: ')
        for c in enumerate(listaFilmes):
            print(f'Filme: {c}')
            while True:
                avalia = int(input('[1] - Filme Ruim!\n'
                            '[2] - Listar Filme Bom!\n'
                            '[3] - Filme Muito Bom!\n'
                            '[4] - Filme Excelente!\n'
                            'Informe Opção: '))
                if avalia == 1:
                    listaAvaliacoes.append('Filme Ruim!')
                    listaFilmes.append(listaAvaliacoes[:])
                    listaAvaliacoes.clear()
                    print(listaFilmes)
                    break
                elif avalia == 2:
                    listaAvaliacoes.append('Filme Bom!')
                    listaFilmes.append(listaAvaliacoes[:])
                    listaAvaliacoes.clear()
                    print(listaFilmes)
                    break
                elif avalia == 3:
                    listaAvaliacoes.append('Filme Muito Bom!')
                    listaFilmes.append(listaAvaliacoes[:])
                    listaAvaliacoes.clear()
                    print(listaFilmes)
                    break
                elif avalia == 4:
                    listaAvaliacoes.append('Filme Excelente!')
                    listaFilmes.append(listaAvaliacoes[:])
                    listaAvaliacoes.clear()
                    print(listaFilmes)
                    break
       




        


        