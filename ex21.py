diametro_bola = float(input())
altura_caixa, largura_caixa, profundidade_caixa = map(float, input().split())

if diametro_bola <= min(altura_caixa, largura_caixa, profundidade_caixa):
    print("S")
else:
    print("N")