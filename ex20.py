largura_mala = float(input())
comprimento_mala = float(input())
altura_mala = float(input())

# Valores constantes, em cm
LARGURA_MAX = 45.0 
COMPRIMENTO_MAX = 56.0
ALTURA_MAX = 25.0

if largura_mala <= LARGURA_MAX and comprimento_mala <= COMPRIMENTO_MAX and altura_mala <= 25:
    print("PERMITIDA")
else:
    print("PROIBIDA")