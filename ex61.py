
salario = float(input())
imposto = 0

if salario >= 0.00 and salario <= 2000.00:
    print("Isento")

else:
    if salario >= 4500: 
        imposto += (salario-4500)*0.28
        salario = 4500

    if salario >= 3000.01 and salario <= 4500.00:
        imposto += (salario-3000)*0.18
        salario = 3000

    if salario >= 2000.01 and salario <= 3000.00:
        imposto += (salario-2000)*0.08

    print(f"R$ {imposto:.2f}")