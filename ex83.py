
numero = int(input())
lista = input().split()
lista2 = []

for i in lista:
    lista2.append(int(i))


aux = []

for num in lista2:
    if num not in aux:
        aux.append(num)

lista2 = aux
lista2.sort()
print(*lista2)

