#Faça um Programa que converta metros para centímetros.
metros = float(input('Digite uma medida em metros: '))
cm = metros * 100
mm = metros * 1000
print('Foi digitado {:.2f}m.\n'
    'Transformando em cemtímetos fica {:.2f}cm.\n'
    'E convertido em milímetros fica {:.2f}mm.'.format(metros, cm, mm))