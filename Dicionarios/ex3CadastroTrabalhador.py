"""pessoa = {}
pessoa['nome'] = str(input('Nome: ')).upper()
pessoa['idade'] = int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
pessoa['contratação'] = int(input('Ano de Contratação: '))
while pessoa['ctps'] == 0:
    pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
pessoa['salário'] = float(input('Salário: '))
pessoa['aposentadoria'] = 2019 - pessoa['contratação']
pessoa['idade'] = 2019 - pessoa['idade']
print('-='*20)
for k, v in pessoa.items():
    print(f'{k} tem o valor: {v}')"""
from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: ')).upper()
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*20)
for k, v in dados.items():
    print(f'{k} tem o valor: {v}')
