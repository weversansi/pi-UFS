n = int(input())
candidato = list(map(float, input().split()))
concorrente = list(map(float, input().split()))

maior = 0.0

for i in range(n):
    vantagem = candidato[i] - concorrente[i]
    if vantagem > maior:
        maior = vantagem

print(f"{maior:.2f}")