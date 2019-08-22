print('Antes de entrar no looping ')
for item in range(0, 10):
    print(item)
    if (item == 6):
        print('A condição  estabelecida retornou True')
        break
    print('Depois de sair so looping ')
'''Usando o break eu posso parar o meu laço no ato onde eu indicar .
ou seja posso fazer um laço para otimizar o meu tempo e espaço, e posso parar ele quando 
meu objetivo for atingido.'''