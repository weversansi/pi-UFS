
def velkm():

    QTD_DE_AUTOMOVEIS = 3
    lista_de_automoveis = []    
        
    for i in range(QTD_DE_AUTOMOVEIS):
        
        velocidade_inicial = float(input())
        aceleracao = float(input())
        tempo_percurso = float(input())

        velocidade = (velocidade_inicial + (aceleracao*tempo_percurso))*3.6
        lista_de_automoveis.append(velocidade)

    return lista_de_automoveis

print(min(velkm())) # Recupera o menor valor da lista
