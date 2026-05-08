
a, b, c = map(int, input().split())


def Omaior(a, b, c):

    maior_ab = (a+b+abs(a-b)) / 2
    maior = (maior_ab + c + abs(maior_ab - c)) / 2

    return f"{int(maior)} eh o maior"

print(Omaior(a, b, c))

