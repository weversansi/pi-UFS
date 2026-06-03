numeros = []

for i in range(101):
    numeros.append(int(input()))

ultimo = numeros[100]

for i in range(100):
    if numeros[i] == ultimo:
        print(i)