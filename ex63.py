
num1  = int(input())
num2  = int(input())

cont = 0
for i in range(1, 50):
    if i % num1 == 0 and i % num2 == 0:
        cont += 1

print(cont)