from random import randint
print('=' * 27)
print('PROGRAMA SUA VIDA VALE MAIS')
print('=' * 27)
speed = randint(0, 140)
velocidade = speed
m1 = 280.00
m2 = m1 + (m1 * 10) / 100
m3 = m2 + (m1 * 50) / 100
m4 = m3 + (m1 * 100)/ 100
if speed <= 30:
    print('Você está muito devagar, pode atrapalhar a via...')
else:
    if speed >= 30 and speed <= 60:
        print('Você está dentro do limite permitido. Bom Passeio...')
    else:
        if velocidade > 60 and velocidade <= 80:
            print('Sua multa será de R$ {:.2f}.'.format(m1))
        else:
            if velocidade > 80 and velocidade <= 100:
                print('Sua multa será de R$ {:.2f}.'.format(m2))
            else:
                if velocidade > 100 and velocidade <= 140:
                    print('Sua multa será de R$ {:.2f}.'. format(m3))
                else:
                    print('Sua multa será de R$ {:.2f}.'.format(m4))