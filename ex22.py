kwh_consumidos = int(input())
valor_kwh = 0

if kwh_consumidos >= 0 and kwh_consumidos <= 99:
    valor_kwh = kwh_consumidos*1.35
    preco = 1.35

elif kwh_consumidos >= 100 and kwh_consumidos <= 299:
    valor_kwh = kwh_consumidos*1.55
    preco = 1.55

elif kwh_consumidos >= 300 and kwh_consumidos <= 574:
    valor_kwh = kwh_consumidos*1.75
    preco = 1.75

else:
    valor_kwh = kwh_consumidos*2.15
    preco = 2.15

if valor_kwh >= 35:
    if kwh_consumidos > 300:
        valor_taxa = (valor_kwh*0.1)
        print(f"{valor_kwh+valor_taxa:.2f}")
        print(preco)
    else:
        print(f"{valor_kwh:.2f}")
        print(preco)

else:
    valor_kwh = 35
    print(f"{valor_kwh:.2f}")
    print(preco)