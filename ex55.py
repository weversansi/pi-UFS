teste = int(input())

for i in range(teste):
    contador = 0
    frase = input().upper()

    for letra in frase:
        if letra in "ADOPQR":
            contador += 1
        elif letra == "B":
            contador += 2

    print(contador)