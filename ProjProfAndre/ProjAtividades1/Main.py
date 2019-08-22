import pymongo
import uuid
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from cliente import cliente as C
from produto import produto as P
import re


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Clientes"]
mycol = mydb["Dados Cliente"]

myproduct = pymongo.MongoClient("mongodb://localhost:27017/")
mydb1 = myproduct["Produtos"]
mycol1 = mydb1["Dados do Produto"]

while True:
    print('=' * 30)
    print('Cadastro de Clientes e Produtos.')
    print('[1] - Clientes')
    print('[2] - Produtos')
    print('[3] - Funcionário')
    print('[4] - Vendas')
    print('[5] - Sair do Menu')
    cadastro = int(input('Informe que tipo deseja cadastrar: '))
    if cadastro == 1:
        while True:
            n = ['Ler Dados Manualmente: ', 'Ler Dados da Planilha: ', 'Procurar por...', 'Sair do Menu']
            print('=' * 30)
            print('Infome a opção desejada:')
            for i in range(len(n)):
                print(f'[{i+1}] - {n[i]}')
            print('=' * 30)
            opcao = int(input("Infome a opção desejada: "))
            if opcao == 1:
                m = []
                n = ['Nome', 'Telefone', 'Endereco', 'Cidade', 'Estado', 'DataNasc']
                for i in range(len(n)):
                    m.append(input(f'{n[i]}: '))
                a = C(f'{m[0]}', f'{m[1]}', f'{m[2]}', f'{m[3]}', f'{m[4]}', f'{m[5]}')
                a.getJson()
                break
            elif opcao == 2:
                arquivo = open("C:/Users/ruiro/Python/ProjPyCharm/ProjAtividades1/DadosCliente.csv", 'r')
                linhas = arquivo.readlines()
                lista = dict()
                for l in linhas:
                    i = l.replace('\n','').split(';')
                    lista[f'{i[0]}'] = f'{i[1]}'
                for k, v in lista.items():
                    print(f'{k}: {v}')
                x = mycol.insert_one(lista)
                print(f'Inserido na Base de dados com o ID: {x.inserted_id}')
                break
            elif opcao == 3:
                while True:
                    n = ['Nome...', 'Telefone...', 'Endereco...', 'Cidade...', 'Estado...', 'Data de Nascimento...', 'Voltar...']
                    print('=' * 30)
                    print('Tipos de perquisa: ')
                    for i in range(len(n)):
                        print(f'[{i+1}] - {n[i]}')
                    print('=' * 30)
                    tipo = int(input('Tipo desejado: '))
                    if (tipo == 1):
                        print('Pesquisa por nome...')
                        n = str(input(''))
                        for x in mycol.find({"Nome": f"{n}"}):
                            print(x)
                    elif (tipo == 2):
                        print('Pesquisa por Telefone...')
                        n = str(input(''))
                        for x in mycol.find({"Telefone": f"{n}"}):
                            print(x)
                    elif (tipo == 3):
                        print('Pesquisa por Endereço...')
                        n = str(input(''))
                        for x in mycol.find({"Endereco": {"$regex" : re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif (tipo == 4):
                        print('Pesquisa por Cidade...')
                        n = str(input(''))
                        for x in mycol.find({"Cidade": f"{n}"}):
                            print(x)
                    elif (tipo == 5):
                        print('Pesquisa por Estado...')
                        n = str(input(''))
                        for x in mycol.find({"Estado": f"{n}"}):
                            print(x)
                    elif (tipo == 6):
                        print('Pesquisa por Data de Nascimento...')
                        n = str(input(''))
                        for x in mycol.find({"DataNasc": f"{n}"}):
                            print(x)
                    elif (tipo == 7):
                        break
                    else:
                        print('Opção inválida, tente novamente.')
            elif opcao == 4:
                print('Saindo!')
                break
            break

    elif cadastro == 2:
        while True:
            n = ['Ler Dados Manualmente: ', 'Ler Dados da Planilha: ', 'Ler por site:', 'Sair do Menu']
            print('=' * 30)
            print('Infome a opção desejada:')
            for i in range(len(n)):
                print(f'[{i+1}] - {n[i]}')
            print('=' * 30)
            opcao = int(input("Infome a opção desejada: "))
            if opcao == 1:
                m = []
                n = ['Nome', 'Preço', 'data_Entrada', 'data_Saída']
                for i in range(len(n)):
                    m.append(input(f'{n[i]}: '))
                p = P(f'{m[0]}', f'{m[1]}', f'{m[2]}', f'{m[3]}')
                p.getJson()
                break
            elif opcao == 2:
                arquivo = open("C:/Users/ruiro/Python/ProjPyCharm/ProjAtividades1/DadosProdutos.csv", 'r')
                linhas = arquivo.readlines()
                lista = dict()
                for l in linhas:
                    i = l.replace('\n', '').split(';')
                    lista[f'{i[0]}'] = f'{i[1]}'
                print(lista)
                x = mycol1.insert_one(lista)
                print(x.inserted_id)
                break
            elif opcao == 3:
                numeroPagina = 1
                url = 'https://www.extra.com.br/?Filtro=D36611&Ordenacao=_MaisVendidos&paginaAtual={}&ComparacaoProdutos=&AdicionaListaCasamento='.format(
                    numeroPagina)
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                webpage = urlopen(req).read()
                page_soup = soup(webpage, "html.parser")
                nomeCelular = page_soup.findAll("strong", "name fn")

                listNome = []
                listPreco = []

                for container in nomeCelular:
                    descricao = str(container).replace('<strong class="name fn">', '')
                    descricao = descricao.replace('</strong>', '')
                    listNome.append(descricao)

                precos = page_soup.findAll("span", "for price sale")

                for container in precos:
                    preco = str(container).replace('<span class="for price sale">Por: <strong>', '')
                    preco = preco.replace('</strong></span>', '')
                    listPreco.append(preco)

                print("DADOS COLETADOS DA PAGINA WEB:")
                print("Descrição, Preço")


                contador = 0
                for dados in nomeCelular:
                    print("{} - {} ".format(str(listNome[contador]), str(listPreco[contador])))
                    contador = contador + 1

                lista1 = []
                for c in range(len(listNome)):
                    #lista1.append('"{}" : "{}"'.format(listNome[c], listPreco[c]))
                    #valor = dict()
                    #valor = lista1.append(f'{listNome[c]}'  listPreco
                    valor = {
                        "nome" : listNome[c],
                        "preco" : listPreco[c]
                    }
                    lista1.append(valor)

                x1 = mycol1.insert_many(lista1)
                break
    elif cadastro == 3:
        print('opcao 3')
    elif cadastro == 4:
        print('opcao 4')
    elif cadastro == 5:
        print('Saindo...')
        break
