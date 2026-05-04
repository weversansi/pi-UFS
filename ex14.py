
pontuacao = 0
PARTIDAS = 6
lista = []


for i in range(PARTIDAS):
    pontuacao = int(input())
    lista.append(pontuacao)

if sum(lista) >= 100:
    print("Classificado")
else:
    print("Eliminado") 