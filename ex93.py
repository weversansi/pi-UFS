
numero_de_apostas = int(input())
armazena_apostas = []
quantidade_vencedores = 0

for i in range(numero_de_apostas):

    apostas = set(map(int, input().split(",")))
    armazena_apostas.append(apostas)
resultado_vencedor = set(map(int, input().split()))

for ii in armazena_apostas:
    if ii  >= resultado_vencedor:
        quantidade_vencedores += 1


print("Total de ganhadores:",quantidade_vencedores)