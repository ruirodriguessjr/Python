galera = []
pessoa = {}
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por Favor Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += (pessoa['idade'])
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer Continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por Favor apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(galera)
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos.')
print(f'C) Nome da(s) Mulhere(s) cadastrada(s): ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}')
            print()
print('>>> ENCERRADO <<<')
