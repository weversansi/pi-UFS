
num1 = int(input())
num2 = int(input())

inicio = min(num1, num2) # Garantindo um inicio
final = max(num1, num2) # Garantindo um final
lista = [] # Criando uma lista

for numero in range(inicio, final+1): # +1 serve para não deixar o último termo de fora 
    if numero > 0:
        lista.append(numero) # Adicionando elementos em uma lista, com append()

print(sum(lista)) # Somando elementos de uma lista