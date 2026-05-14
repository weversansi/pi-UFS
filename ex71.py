consumo = int(input())

conta = 7

if consumo > 10:
    if consumo <= 30:
        conta = conta + (consumo - 10) * 1

    elif consumo <= 100:
        conta = conta + 20 * 1
        conta = conta + (consumo - 30) * 2

    else:
        conta = conta + 20 * 1
        conta = conta + 70 * 2
        conta = conta + (consumo - 100) * 5

print(conta)