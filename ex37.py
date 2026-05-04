
numero_inteiro = int(input())
soma = 0 

for i in range(numero_inteiro):
    if i % 3 == 0 or i % 5 == 0:
        soma += i 

print(soma)

