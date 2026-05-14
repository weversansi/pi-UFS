def avaliar_risada(risada):

    vogais = "aeiou"
    so_vogais = ""

    if len(risada) < 50:
        
        for c in risada:
            if c in vogais:
                so_vogais += c

        if so_vogais == "":
            return "INVALIDA"

        if so_vogais == so_vogais[::-1]:
            return "ENGRACADA"
        else:
            return "SEM GRACA"
    else:
        return "INVALIDA"

n = int(input())

for i in range(n):
    risada = input().strip()
    print(avaliar_risada(risada))