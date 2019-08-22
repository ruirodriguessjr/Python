#Faça um Programa que peça os 3 lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;
l1= float(input('Primeira medida: '))
l2 = float(input('Segunda Medida: '))
l3 = float(input('Terceira Medida: '))
if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print('É um Triângulo.')
        print('O Triângulo é Equilátero!!!')
    elif l1 != l2 != l3 !=l1:
        print('É um Triângulo.')
        print('É um Triângulo Escaleno!!!')
    else:
        print('É um Triângulo.')
        print('O Triângulo é Isóceles!!!')
else:
    print('Não foi possível formar um Triângulo.')