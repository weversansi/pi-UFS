
conte_sim = 0
conte_nao = 0
conte_nulo = 0

while True:

    votacao = input().upper()

    if votacao == "ENCERRAR":
        break

    if votacao == "SIM":
        conte_sim += 1

    elif votacao == "NAO":
        conte_nao += 1

    elif votacao == "NULO":
        conte_nulo += 1

if conte_sim > (conte_nao+conte_nulo):
    print("COM FOGOS")
else:
    print("SEM FOGOS")
