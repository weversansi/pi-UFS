kwh_consumidos = float(input())
valor_a_ser_pago = kwh_consumidos*1.50

print(f"Valor a ser pago: R$ {valor_a_ser_pago:.2f} reais")
print(f"Valor a ser pago com desconto: R$ {valor_a_ser_pago-(valor_a_ser_pago*0.15):.2f} reais")