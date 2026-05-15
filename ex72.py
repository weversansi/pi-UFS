
numero1, numero2 = map(int, input().split())
lista = []

for i in range(numero1, numero2+1):

    if i % 5 == 0:
        lista.append(str(i))

print("|".join(lista))




