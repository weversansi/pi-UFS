
escolha = input().lower()
a = int(input())
b = int(input())
c = int(input())
conta = 0


if escolha == "a":
    conta = (a+b+c)/3

elif escolha == "h":
    conta = 3/((1/a)+(1/b)+(1/c))

elif escolha == "g":
    conta = (a*b*c)**(1/3)
    
print(f"{conta:.3f}")

