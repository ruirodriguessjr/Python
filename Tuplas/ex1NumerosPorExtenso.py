extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    usu = int(input('Digite um número ( 0 à 20 ): '))
    while usu < 0 or usu > 20:
        usu = int(input('Tente novamente. Digite um número ( 0 à 20 ): '))
    print(f'Você digitou o número {extenso[usu]}')
    print('=' * 30)
    perg = input('Quer continuar? [S/N]: ').upper().strip()[0]
    while perg != 'S' and perg != 'N':
        print('=' * 30)
        perg = input('Responda novamente. Quer continuar, Sim ou Não: ').upper().strip()[0]
    print('=' * 30)
    if perg == 'N':
        break

