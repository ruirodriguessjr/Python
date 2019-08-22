a = 10
b = 26
c = 66
x = int(input('Digite um número: '))
#if (x == a or x == b or x == c):
if (x in [a,b,c]):
    print('O número está contido')
else:
    print('O número não está contido')
cores = ['amarelo', 'azul', 'verde', 'branco']
while True:
    cor = input('Digite o nome de uma cor, ou 0 para sair do programa: ')
    if (cor == '0'):
        print('Saindo.....')
        break
    if cor in cores:
        print('Esta cor está contida.')
        break
    else:
        print('Esta cor não está contida.')
        break
'''Poderia usar a expressão for, pois while vai rodar o programa até a informação ser falsa.
já na expressão for, eu rodaria o programa até que minha solicitação seja atendida.'''
