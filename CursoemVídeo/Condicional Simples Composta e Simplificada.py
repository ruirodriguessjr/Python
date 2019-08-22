nome = str(input('Digite seu nome: '))
if nome == 'Rui Rodrigues':
    print('Você é um bosta...Arrombado...sem diploma.')
else:
    print('Você é importante todos te admiram...')
print('Bom dia, {}'.format(nome))
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
'''if m >= 6:
    print('Parabéns você passou de ano.')
else:
    print('Você repetiu, vamos começar de novo.')'''
'''Psso fazer também uma maneira simplificada do print com IF e ELSE dentro do parenteses:'''
print('Parabéns' if m >= 6 else 'Estude mais')
'''Se chama de condicional Simplificada.'''