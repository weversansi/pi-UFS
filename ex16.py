quantidade_de_diarias = int(input())
quilometragem_rodada = float(input())

# Valores constantes
VALOR_POR_DIA = 90.0 # R$ 90,00 por diária
CADA_DIARIA_QUILOMETRAGEM = 100 # 100 km permito para cada diária
VALOR_POR_QUILOMETRO_ULTRAPASSADO = 12.0 # R$ 12,00 por quilometro ultrapassado 

# Variávies
valor_pagamento = quantidade_de_diarias*VALOR_POR_DIA
quilometragem_permitida = 0
valor_diferenca = 0

for dia in range(quantidade_de_diarias):
    quilometragem_permitida += 100

if quilometragem_rodada > quilometragem_permitida:
    valor_diferenca = (quilometragem_rodada - quilometragem_permitida)*12.00
else:
    valor_diferenca = 0

print(f"{valor_pagamento+valor_diferenca:.2f}") 



