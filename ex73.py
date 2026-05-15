
def contar_vogais(teste): # Resolver problema que está somando os contadores

    contador = 0

    for i in range(teste):
        vogais = input().lower()
        frase = input().lower().replace(" ", "")

        for ii in frase:

            if ii in vogais:
                contador += 1
        
        print(contador)
        contador = 0


teste = int(input())

contar_vogais(teste)