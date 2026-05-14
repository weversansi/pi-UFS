
valor_inicial = float(input())
dias_validos = 0
soma_dos_valores = 0
soma_dos_dias = 0

for i in range(7):

    valor_cada_dia = float(input())
    soma_dos_dias += valor_cada_dia

    if valor_cada_dia >= i - 1:

        soma_dos_valores += 0.50
        dias_validos += 1

print(dias_validos)
print(soma_dos_dias)