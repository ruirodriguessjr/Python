"""Criar um algoritmo em python que leia a idade:
a. Se for maior de 18, escrever: “Você tem %% anos, você é maior de idade”
b. Se for igual a 18, escrever: “Você tem %% anos”
c. Se for menor de 18: “Você tem %% anos, você é menor de idade”"""

idade = int(input('Informe sua idade: '))
if idade > 18:
    print(f'Você tem {idade} anos. Você é maior de idade.')
elif idade == 18:
    print(f'Você tem {idade} anos.')
elif idade < 18:
    print(f'Você tem {idade} anos. Você é menor de idade.')