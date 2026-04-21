custo_por_litro, m3_de_agua_consumidos = map(float, input().split())
valor_pago = (m3_de_agua_consumidos*1000)*custo_por_litro
esgoto = valor_pago-(valor_pago*0.2)
valor_total = valor_pago+esgoto

print(f"{valor_pago:.2f}")
print(f"{esgoto:.2f}")
print(f"{valor_total:.2f}")