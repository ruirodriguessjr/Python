'''Abaixo de 17	Muito abaixo do peso
Entre 17 e 18,49	Abaixo do peso
Entre 18,5 e 24,99	Peso normal
Entre 25 e 29,99	Acima do peso
Entre 30 e 34,99	Obesidade I
Entre 35 e 39,99	Obesidade II (severa)
Acima de 40	Obesidade III (mórbida)'''

peso = float(input('Qual o seu peso em:(kg) '))
alt = float(input('Qual a sua altura:(m) '))
imc = peso / (alt * 2)
print('Seu PESO é {:.1f}Kg, sua ALTURA é {:.1f}m e seu IMC é {:.1f}.'.format(peso, alt, imc))
if imc < 18.50:
    print('Abaixo do Peso.')
elif 18.5 <= imc < 25:
    print('Peso Normal.')
elif 25 <= imc < 30:
    print('Acima do Peso.')
elif 30 <= imc < 35:
    print('Obesidade I.')
elif 35 <= imc < 40:
    print('Obesidade II.')
else:
    print('Obesidade Mórbida.')
