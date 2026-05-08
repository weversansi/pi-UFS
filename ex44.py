comprimento1 = int(input())
comprimento2 = int(input())
comprimento3 = int(input())
comprimento4 = int(input())

def eRetangulo(c1, c2, c3, c4):
    lados = sorted([c1, c2, c3, c4])
    # Retorna True se os dois primeiros são iguais e os dois últimos são iguais
    return lados[0] == lados[1] and lados[2] == lados[3]

# Chamada da função e saída conforme o retorno
if eRetangulo(comprimento1, comprimento2, comprimento3, comprimento4):
    print("RETANGULO")
else:
    print("NAO EH UM RETANGULO")