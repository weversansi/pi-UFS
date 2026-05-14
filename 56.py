
numero = int(input())

for i in range(numero):
    frase_ou_palavra = input().lower().replace(" ", "") # Replace troca 

    if frase_ou_palavra[::-1] == frase_ou_palavra :
        print("SIM")

    else:
        print("NAO")
