preco_eua = float(input())
preco_brasil = float(input())
cotacao_dolar = float(input())

valor_convertido = (preco_eua * cotacao_dolar) / 3.8

print(f"Gasolina EUA: R$ {valor_convertido:.2f}")
print(f"Gasolina Brasil: R$ {preco_brasil:.2f}")

if valor_convertido < preco_brasil:
    print("Mais barata nos EUA")

elif valor_convertido > preco_brasil:
    print("Mais barata no Brasil")

else:
    print("Igual")