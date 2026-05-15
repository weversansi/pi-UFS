def ePrimo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1

    if contador == 2:
        return True
    else:
        return False


x = int(input())
y = int(input())

if ePrimo(x) == False:
    print(f"O numero {x} nao eh primo")
elif ePrimo(y) == False:
    print(f"O numero {y} nao eh primo")
else:
    soma = x + y

    if ePrimo(soma) == True:
        print(f"A soma de {x} e {y} eh um primo")
    else:
        print(f"A soma de {x} e {y} nao eh um primo")