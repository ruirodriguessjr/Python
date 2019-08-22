print()
print('Antes de entrar no looping ')
for i in range(0, 10, 1):
    if (i%2==0):
        continue
    if (i > 5):
        break
    print(i)
else:
    print("Depois do lopping")

'''Usando a função continue Essa função finaliza uma repetição porém ela não termina a execução 
da nossa repetição, quando a instrução é verdadeira ele volta para o inicio do looping,
quando é falsa ele segue lendo a linha de baixo do laço..'''