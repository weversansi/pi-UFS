def tipo_triangulo():
    while True:
        linha = input().strip()

        if linha == "FIM":
            break

        lado1, lado2, lado3 = map(int, linha.split())

        if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
            print("INVALIDO")
        elif lado1 == lado2 == lado3:
            print("EQUILATERO")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("ISOSCELES")
        else:
            print("ESCALENO")

tipo_triangulo()