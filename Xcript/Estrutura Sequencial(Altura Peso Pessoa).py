#Tendo como dados de entrada a altura de uma pessoa,
#construa um algoritmo que calcule seu peso ideal,
#usando a seguinte fórmula: (72.7*altura) - 58
'''alt = float(input('Digite sua altura: '))
form = (72.7 * alt) - 58
print(form)'''
#Tendo como dados de entrada a altura e o sexo de uma pessoa,
#construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 (h = altura)
#Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
sexo = str(input('Digite [1] para homem e [2] para mulher: '))
alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
if sexo == 1:
	peso_ideal = (72.7 * alt) - 58
else:
	peso_ideal = (62.1 * alt) - 44.7
if peso < peso_ideal:
    print('Está abaixo do peso...')
elif peso == peso_ideal:
    print('Etá no peso ideal...')
else:
    print('Está acima do peso...')