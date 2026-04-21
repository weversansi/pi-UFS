a = int(input())
b = int(input())
c = int(input())

if (a == 0 or a == 1) and (b == 0 or b == 1) and (c == 0 or c == 1): 
    if a != b and a != c:
        print("A\n")
    elif b != a and b != c:
        print("B\n")
    elif c != a and c != b:
        print("C\n")
    else: 
        print("*\n")
