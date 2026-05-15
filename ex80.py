def adicionar_hifen(numero):

    for i in range(1, numero + 1):

        for ii in range(1, i + 1):

            print(i, end="")
            if i > ii:
                print("-", end="")

        print()

numero = int(input())
adicionar_hifen(numero)