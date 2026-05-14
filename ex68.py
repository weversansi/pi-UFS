valor1 = float(input())
valor2 = float(input())
sinal = input()

while sinal != "&":
    if sinal == "/" and valor2 == 0:
        print("operacao nao pode ser realizada")
    else:
        if sinal == "+":
            valor1 = valor1 + valor2
        elif sinal == "-":
            valor1 = valor1 - valor2
        elif sinal == "*":
            valor1 = valor1 * valor2
        elif sinal == "/":
            valor1 = valor1 / valor2

        print(f"{valor1:.3f}")

    valor2 = float(input())
    sinal = input()