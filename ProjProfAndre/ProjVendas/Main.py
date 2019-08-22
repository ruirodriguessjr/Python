# coding: utf-8

import pymongo as mongo
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as Soup
from Clientes import Cliente as Cl
from Funcionarios import Funcionario as Fu
from Produtos import Produto as Pr
from Vendas import Venda as Ve


myclient = mongo.MongoClient("mongodb://localhost:27017/")  # Comunicação com a base de dados
mydbcli = myclient["Clientes"]
mycolcli = mydbcli["Dados Cliente"]
mydbfunc = myclient["Funcionarios"]
mycolfunc = mydbfunc["Dados Funcionario"]
mydbprod = myclient["Produtos"]
mycolprod = mydbprod["Dados Produto"]
mydbven = myclient["Vendas"]
mycolven = mydbven["Dados Venda"]

while True:  # Menu principal
    n = ['Clientes', 'Funcionários', 'Produtos', 'Vendas', 'Sair']
    print('=' * 30)
    print('Tipos de perquisa: ')
    for i in range(len(n)):
        print(f'[{i + 1}] - {n[i]}')
    print('=' * 30)
    opcao = int(input('>>> '))
    if opcao == 1:  # Opções referentes aos clientes
        while True:  # Menu de opções refetentes aos clientes
            n = ['Cadastro Manual', 'Cadastro via Planilha', 'Pesquisa', 'Voltar']
            print('=' * 30)
            print('Tipos de perquisa: ')
            for i in range(len(n)):
                print(f'[{i + 1}] - {n[i]}')
            print('=' * 30)
            opcao = int(input('>>>'))
            if opcao == 1:  # Inserção manual de cadastro de cliente
                print('Catastro Manual')
                n = ['Nome', 'Telefone', 'Endereco', 'Cidade', 'Estado', 'DataNasc']
                d = []
                for i in range(len(n)):
                    d.append(input(f'{n[i]}'))
                c = Cl(d[0], d[1], d[2], d[3], d[4], d[5])
                c.toDB()
            elif opcao == 2:  # Inserção via planilha '.csv' de cadastro de cliente
                arq = input('Informe o diretório do arquivo .csv\n>>> ')
                arquivo = open(f"{arq}", 'r')
                linhas = arquivo.readlines()
                lista = []
                for l in linhas:
                    i = l.replace('\n', '').split(',')
                    lista.append(i[1])
                c1 = Cl(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5])
                c1.toDB()
            elif opcao == 3:  # Pesquisa referente aos clientes
                while True:  # Menu de pesquisa referente aos clientes
                    n = ['Nome', 'Telefone', 'Endereco', 'Cidade', 'Estado', 'Data de Nascimento',
                         'Voltar']
                    print('=' * 30)
                    print('Tipos de perquisa: ')
                    for i in range(len(n)):
                        print(f'[{i + 1}] - {n[i]}')
                    print('=' * 30)
                    tipo = int(input('Tipo desejado: '))
                    if tipo == 1:  # Pesquisa de cliente via nome
                        print('Pesquisa por nome')
                        n = str(input(''))
                        for x in mycolcli.find({"Nome": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 2:  # Pesquisa de cliente via telefone
                        print('Pesquisa por Telefone')
                        n = str(input(''))
                        for x in mycolcli.find({"Telefone": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 3:  # Pesquisa de cliente via endereço
                        print('Pesquisa por Endereço')
                        n = str(input(''))
                        for x in mycolcli.find({"Endereco": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 4:  # Pesquisa de cliente via cidade
                        print('Pesquisa por Cidade')
                        n = str(input(''))
                        for x in mycolcli.find({"Cidade": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 5:  # Pesquisa de cliente via estado
                        print('Pesquisa por Estado')
                        n = str(input(''))
                        for x in mycolcli.find({"Estado": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 6:  # Pesquisa de cliente via data de nascimento
                        print('Pesquisa por Data de Nascimento')
                        n = str(input(''))
                        for x in mycolcli.find({"DataNasc": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 7:  # Retorno ao menu de 'Opções referentes aos clientes'
                        break
                    else:  # Condição de tratamento para inserção de opção inválida
                        print('Opção inválida, tente novamente.')
            elif opcao == 4:  # Retorno ao menu principal
                break

    elif opcao == 2:  # Opções referentes aos funcionários
        while True:  # Menu de opções referentes aos funcionários
            n = ['Cadastro Manual', 'Cadastro via Planilha', 'Pesquisa', 'Voltar']
            print('=' * 30)
            print('Tipos de perquisa: ')
            for i in range(len(n)):
                print(f'[{i + 1}] - {n[i]}')
            print('=' * 30)
            opcao = int(input('>>>'))
            if opcao == 1:  # Inserção manual de cadastro de funcionário
                print('Catastro Manual')
                n1 = ['Nome', 'Telefone', 'Endereco', 'Cidade', 'Estado', 'DataNasc', 'Salario']
                d1 = []
                for i in range(len(n1)):
                    d1.append(input(f'{n1[i]}'))
                f = Fu(d1[0], d1[1], d1[2], d1[3], d1[4], d1[5], d1[6])
                f.toDB()
            elif opcao == 2:  # Inserção via planilha '.csv' de cadastro de funcionário
                arq = input('Informe o diretório do arquivo .csv\n>>> ')
                arquivo = open(f"{arq}", 'r')
                linhas = arquivo.readlines()
                lista = []
                for l in linhas:
                    i = l.replace('\n', '').split(',')
                    lista.append(i[1])
                f1 = Fu(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6])
                f1.toDB()
            elif opcao == 3:  # Pesquisa referente aos funcionários
                while True:  # Menu de pesquisa referente aos funcionários
                    n = ['Nome', 'Telefone', 'Endereco', 'Cidade', 'Estado', 'Data de Nascimento', 'Salário', 'Voltar']
                    print('=' * 30)
                    print('Tipos de perquisa: ')
                    for i in range(len(n)):
                        print(f'[{i + 1}] - {n[i]}')
                    print('=' * 30)
                    tipo = int(input('Tipo desejado: '))
                    if tipo == 1:  # Pesquisa de funcionário via nome
                        print('Pesquisa por nome')
                        n = str(input(''))
                        for x in mycolfunc.find({"Nome": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 2:  # Pesquisa de funcionário via telefone
                        print('Pesquisa por Telefone')
                        n = str(input(''))
                        for x in mycolfunc.find({"Telefone": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 3:  # Pesquisa de funcionário via endereço
                        print('Pesquisa por Endereço')
                        n = str(input(''))
                        for x in mycolfunc.find({"Endereco": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 4:  # Pesquisa de funcionário via cidade
                        print('Pesquisa por Cidade')
                        n = str(input(''))
                        for x in mycolfunc.find({"Cidade": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 5:  # Pesquisa de funcionário via estado
                        print('Pesquisa por Estado')
                        n = str(input(''))
                        for x in mycolfunc.find({"Estado": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 6:  # Pesquisa de funcionário via data de nascimento
                        print('Pesquisa por Data de Nascimento')
                        n = str(input(''))
                        for x in mycolfunc.find({"DataNasc": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 7:  # Pesquisa de funcionário via salário
                        print('Pesquisa por Salário')
                        n = str(input(''))
                        for x in mycolfunc.find({"Salario": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 8:  # Retorno ao menu de 'Opções referentes aos funcionários'
                        break
                    else:  # Condição de tratamento para inserção de opção inválida
                        print('Opção inválida, tente novamente.')
            elif opcao == 4:  # Retorno ao menu principal
                break

    elif opcao == 3:  # Opções referentes aos produtos
        while True:  #Menu de opções referentes aos produtos
            n = ['Cadastro Manual', 'Cadastro via Planilha', 'Cadastro via Site', 'Pesquisa', 'Voltar']
            print('=' * 30)
            print('Tipos de perquisa: ')
            for i in range(len(n)):
                print(f'[{i + 1}] - {n[i]}')
            print('=' * 30)
            opcao = int(input('>>> '))
            if opcao == 1:  # Inserção manual de cadastro de produto
                print('Catastro Manual')
                n = ['Nome', 'Descricao', 'Preco']
                d = []
                for i in range(len(n)):
                    d.append(input(f'{n[i]}'))
                p = Pr(d[0], d[1], d[2])
                p.toDB()
            elif opcao == 2:  # Inserção via planilha '.csv' de cadastro de produto
                arq = input('Informe o diretório do arquivo .csv\n>>> ')
                arquivo = open(f"{arq}", 'r')
                linhas = arquivo.readlines()
                lista = []
                for l in linhas:
                    i = l.replace('\n', '').split(',')
                    lista.append(i[1])
                p1 = Pr(lista[0], lista[1], lista[2])
                p1.toDB()
            elif opcao == 3:  # Inserção via url de cadastro de produto
                numeroPagina = 1
                url = f'https://www.extra.com.br/?Filtro=D36611&Ordenacao=_MaisVendidos&paginaAtual=' \
                    f'{numeroPagina}&ComparacaoProdutos=&AdicionaListaCasamento='
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                webpage = urlopen(req).read()
                page_soup = Soup(webpage, "html.parser")
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
                # for c in range(len(listNome)):
                #    lista1.append('"{}" : "{}"'.format(listNome[c], listPreco[c]))
                #    valor = dict()
                #    valor = lista1.append(f'{listNome[c]}'  listPreco
                #    valor = {
                #        "nome": listNome[c],
                #        "preco": listPreco[c]
                #    }
                #    lista1.append(valor)
                for i in lista1:
                    p1 = Pr('Celular', i[0], i[1])
                    p1.toDB()
            elif opcao == 4:  # Pesquisa referente aos produtos
                while True:  # Menu de pesquisa referente aos produtos
                    n = ['Nome', 'Descricao', 'Preço', 'Data de Entrada']
                    print('=' * 30)
                    print('Tipos de perquisa: ')
                    for i in range(len(n)):
                        print(f'[{i + 1}] - {n[i]}')
                    print('=' * 30)
                    tipo = int(input('Tipo desejado: '))
                    if tipo == 1:  # Pesquisa de produto via nome
                        print('Pesquisa por nome')
                        n = str(input(''))
                        for x in mycolfunc.find({"Nome": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 2:  # Pesquisa de produto via descrição
                        print('Pesquisa por Descricao')
                        n = str(input(''))
                        for x in mycolfunc.find({"Descricao": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 3:  # Pesquisa de produto via preço
                        print('Pesquisa por Preço')
                        n = str(input(''))
                        for x in mycolfunc.find({"Preco": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 4:  # Pesquisa de produto via data de entrada
                        print('Pesquisa por Data de Entrada')
                        n = str(input(''))
                        for x in mycolfunc.find({"DtEntrada": {"$regex": re.compile(n, re.IGNORECASE)}}):
                            print(x)
                    elif tipo == 5:  # Retorno ao menu de 'pesquisa referente aos produtos'
                        break
                    else:  # Condição de tratamento para inserção de opção inválida
                        print('Opção inválida, tente novamente.')
            elif opcao == 5:  # Retorno ao menu de 'opções referente aos produtos'
                break
            else:
                print('Opção inválida, tente novamente.')
    elif opcao == 4:  # Opções referentes às vendas
        while True:  # Menu de opções referente às vendas
            n = ['Realizar Venda', 'Consultar Histórico', 'Voltar']
            print('=' * 30)
            print('Tipos de perquisa: ')
            for i in range(len(n)):
                print(f'[{i + 1}] - {n[i]}')
            print('=' * 30)
            opcao = int(input('>>> '))
            if opcao == 1:  # Realização de venda
                pvalue = int(input('Informe o ID do produto para venda\n>>> '))
                cvalue = int(input('Informe o ID do cliente comprador\n>>> '))
                fvalue = int(input('Informe o seu ID de funcionário\n>>> '))
                description = input('Descrição da venda\n>>> ')

                prod = ''
                cli = ''
                func = ''

                for p in mycolprod.find({'_id': pvalue}):
                    prod = list(p.values())
                for p in mycolcli.find({'_id': cvalue}):
                    cli = list(p.values())
                for p in mycolfunc.find({'_id': fvalue}):
                    func = list(p.values())

                p1 = Pr(prod[1], prod[2], prod[3])
                p1.setID(prod[0])
                p1.setDtEntrada(prod[4])

                c1 = Cl(cli[1], cli[2], cli[3], cli[4], cli[5], cli[6])
                c1.setID(cli[0])

                f1 = Fu(func[1], func[2], func[3], func[4], func[5], func[6], func[7])
                f1.setID(func[0])

                v1 = Ve(description, p1.getJsonProd(), c1.getJsonCli(), f1.getJsonFunc())
                v1.toDB()
            elif opcao == 2:  # Listagem do histórico de vendas
                for v in mycolven.find():
                    print(v)
            elif opcao == 3:  # Retorno ao menu de 'opcoes refetente aos produtos'
                break
    elif opcao == 5:  # Fim da execução do programa
        print('Saindo')
        break
