
num1 = int(input())
num2 = int(input())
num3 = int(input()) 

if num1 == num2 and num2 == num3:
    print(1)
elif num1 != num2 and num2 != num3:
    print(2)
elif num1 == num2 or num2 == num3:
    print(3)

