valor_produto = float(input())
qtd_anos_garantia = int(input())
valor_total = 0

if qtd_anos_garantia == 1:
    valor_total = (valor_produto*0.03)+valor_produto
elif qtd_anos_garantia == 2:
    valor_total = (valor_produto*0.05)+valor_produto
else:
    valor_total = valor_produto

print(f"{valor_total:.2f}")