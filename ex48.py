
numero = int(input())
s = 0
contador_3_em_3 = 0
lista_fracoes = []

for num in range(1,numero+1):
    
    contador_3_em_3 += 3
    s += (num/contador_3_em_3)

    lista_fracoes.append(f"{num}/{contador_3_em_3}")

print(" + ".join(lista_fracoes)) #Join usado como separador dos elementos da lista 
print(f"{s:.2f}")