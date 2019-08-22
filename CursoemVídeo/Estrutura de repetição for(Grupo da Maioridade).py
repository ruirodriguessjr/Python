from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em que Ano a {}ª pessoa nasceu: '.format(pessoas)))
    idade = atual - nasc
    if idade >= 21:
        totmaior = totmaior + 1

    else:
        idade < 21
        totmenor = totmenor + 1
print('Ao todo tivemos {} de pessoas de maior de idade'.format(totmaior))
print('Ao todo tivemos {} de pessoas de menor de idade'.format(totmenor))

