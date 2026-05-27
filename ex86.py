
quantidade_de_alunos = int(input())
soma_notas = 0
lista_notas = []
notas_acima = 0
notas_abaixo = 0

for i in range(quantidade_de_alunos):
    notas = float(input())
    lista_notas.append(notas)


media_notas = sum(lista_notas)/quantidade_de_alunos

limite_acima = media_notas * 1.1
limite_abaixo = media_notas * 0.9

for ii in lista_notas:
    if ii > limite_acima:
        notas_acima += 1

    elif ii < limite_abaixo:
        notas_abaixo += 1


print(f"{media_notas:.2f}")
print(f"{notas_acima}")
print(f"{notas_abaixo}")