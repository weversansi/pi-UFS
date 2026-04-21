a, b, c = map(float, input().split())
 
pi = 3.14159

print(f"TRIANGULO: {(a*c)/2:.2f}")
print(f"CIRCULO: {pi*(c**2):.2f}")
print(f"TRAPEZIO: {((a+b)*c)/2:.2f}")
print(f"QUADRADO: {b**2:.2f}")
print(f"RETANGULO: {a*b:.2f}")