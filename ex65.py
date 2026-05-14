def profissao(forca, inteligencia, destreza, furtividade, peso):

    if forca > 5 and inteligencia <= 5 and destreza > 5 and furtividade <= 5 and peso > 5:
        print("Knight")

    elif forca < 5 and inteligencia > 5 and destreza >= 5 and furtividade > 5 and peso <= 5:
        print("Mage")

    elif forca > 5 and inteligencia > 5 and destreza > 5 and furtividade > 5 and peso < 5:
        print("Paladin")

    elif forca > 10 and inteligencia < 5 and destreza < 5 and furtividade < 5 and peso > 5:
        print("Orc")

    else:
        print("Invalida")

forca = int(input())
inteligencia = int(input())
destreza = int(input())
furtividade = int(input())
peso = int(input())

profissao(forca, inteligencia, destreza, furtividade, peso)