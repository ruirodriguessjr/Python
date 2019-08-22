#Progressão Aritmética

print("=" * 30)
print(" ==== 10 Termos de uma PA ==== ")
print("=" * 30)
t = int(input("Informe o Primeiro Elemento da PA: "))
r = int(input("Informe a razão da PA: "))
decimo = t + ((10 - 1) * r)
for c in range(t, decimo + r, r):
	print(c, end="↔ ")
print("Acabou!!!")