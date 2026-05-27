qtde_numero = int(input())
lista_numeros = input().split()
lista_final = []


while True:
    if qtde_numero == len(lista_numeros):
        for i in lista_numeros:
            lista_final.append(int(i))
        break
    else:
        print("Quantidade de números não batem")
        print("Por favor, digite novamente a lista de números")
        lista_numeros = input().split()


invertido = lista_final[::-1]
decrescente = sorted(lista_final, reverse=True)
elemento = lista_final.pop(0)
lista_deslocamento = []  # Inicializa a lista vazia

lista_deslocamento = lista_final.copy()  # Copia a lista após o pop
lista_deslocamento.append(elemento)      # Adiciona o elemento removido no final

print("")
print(*invertido)
print(*lista_deslocamento)
print(*decrescente)