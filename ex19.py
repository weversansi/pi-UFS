num = int(input())
if num < 0:
    print(-(abs(num) % 10)) # abs() -> Garante que trabalhamos com números positivos
else:
    print(num % 10)