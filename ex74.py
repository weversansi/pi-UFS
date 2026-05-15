
investimento_inicial, taxa_juros, anos = input().split()

investimento_inicial = float(investimento_inicial)
taxa_juros = float(taxa_juros)
anos = int(anos)

redimento = 0

trimestre = int((12 * anos) /3)

for i in range(trimestre):

    redimento = investimento_inicial*taxa_juros
    investimento_inicial += redimento

    print(f"Rendimento: {redimento:.2f} Montante: {investimento_inicial:.2f}")