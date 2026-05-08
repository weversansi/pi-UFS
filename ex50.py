numero_de_leituras, capacidade_maxima_do_elevador = map(int, input().split())

ocupacao_atual = 0
resposta = "N"

for _ in range(numero_de_leituras):
    pessoas_que_sairam, pessoas_que_entraram = map(int, input().split())
    ocupacao_atual -= pessoas_que_sairam
    ocupacao_atual += pessoas_que_entraram

    if ocupacao_atual > capacidade_maxima_do_elevador:
        resposta = "S"

print(resposta)