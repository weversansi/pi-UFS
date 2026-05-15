num1, num2 = input().split()

num1 = int(num1)
num2 = int(num2)

for i in range(1, num2 + 1):
    print(i, end="")

    if i % num1 == 0:
        print()
    else:
        print(" ", end="")