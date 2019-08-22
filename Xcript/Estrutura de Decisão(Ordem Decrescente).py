#Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
n3 = int(input('Terceiro Número: '))
if n1 > n2 and n1 >n3:
    print(n1)
elif n2 > n3 and n2 > n1:
    print(n2)
elif n3 > n1 and n3 > n2:
    print(n3)
#agora o numero do meio
if n1 > n3 and n1 < n2:
    print(n1)
elif n2 > n1 and n2 < n3:
    print(n2)
elif n3 > n2 and n3 > n1:
    print(n3)
elif n2 < n1 and n2 > n3:
    print(n2)
if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n3 and n2 < n1:
    print(n2)
elif n3 < n1 and n3 < n2:
    print(n3)