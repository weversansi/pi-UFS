
num1 = float(input())
num2 = float(input())
num3 = float(input())
cont = 0

media = (num1+num2+num3)/3
lista = [num1, num2, num3]

for num in lista:
    if num > media:
        cont += 1

print(cont)


