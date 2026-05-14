
menor = None
maior = None
soma = 0
total = 0
n = 0

while True:
    linha = input().strip()
    
    if linha == "*":
        break
    
    x, y = linha.split(",")
    x = int(x.strip())
    y = int(y.strip())
    
    s = x + y
    
    if menor is None or s < menor:
        menor = s
    if maior is None or s > maior:
        maior = s
    
    soma += s
    total += x + y
    n += 1

print(f"menor soma: {menor}")
print(f"maior soma: {maior}")
print(f"media dos pares: {soma / n:.2f}")
print(f"media de todos: {total / (n * 2):.2f}")