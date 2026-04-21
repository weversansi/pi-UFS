salario = float(input())
aumento_porcentual = float(input())
novo_salario = ((aumento_porcentual/100)*salario)+salario

print(f"Seu salario teve aumento de {aumento_porcentual:.0f} %, passando de R$ {salario} para R$ {novo_salario}")

