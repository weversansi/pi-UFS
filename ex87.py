
lista = input().split()
lista_final = []

for i in lista:
    lista_final.append(int(i))


elemento = lista_final.pop(len(lista_final)-1)

print(f"O numero {elemento} apareceu {lista_final.count(elemento)+1} vezes")