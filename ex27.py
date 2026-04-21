num = int(input())

if num > 0:
    if num % 2 == 0:
        print("POSITIVO PAR")
    else:
        print("POSITIVO IMPAR")
elif num < 0:
    if num % 2 == 0:
        print("NEGATIVO PAR")
    else:
        print("NEGATIVO IMPAR")
else:
    print("NULO")