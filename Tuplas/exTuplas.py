lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[0])
print(lanche[1])
print(lanche[-1])
print(lanche[2])
print(lanche[-2])
print(lanche[3])
print(lanche[-3])
print(lanche[-4])
print(lanche[1:3])
print(lanche[0:2])

#Tuplas são Imutáveis.
#lanche[1] = 'Regrigerante'
#print(lanche[1]) 
for comida in range(0, len(lanche)):
	print(f'Eu vou comer {comida} ')

for cont in range(0, len(lanche)):
	print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
	print(f'Eu vou comer {comida} na posição {pos}')

for cont in enumerate(lanche):
	print(cont) 
print('Comi muito, por isso sou Gordo!!!')

print(sorted(lanche)) #Organiza a tupla em ordem alfabética.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(d) #Concatenando Tuplas.
print(len(c)) #Conta quantos itens tem dentro da minha tupla
print(c.count(2)) # Conta quantos números 2 tem dentro da minha tupla
print(c.index(8)) # mostra a posição onde está meu item na tupla