 
votos = 0
votos_candidato_aliababa = 0
votos_candidato_alcapone = 0
votos_brancos = 0
votos_nulos = 0

while True:

    votos = int(input())

    if votos == -1:
        break
    
    elif votos == 83:
        votos_candidato_aliababa += 1
    
    elif votos == 93:
        votos_candidato_alcapone += 1

    elif votos == 0:
        votos_brancos += 1

    else:
        votos_nulos += 1

votos_total = votos_candidato_alcapone + votos_candidato_aliababa + votos_brancos

if votos_candidato_alcapone > votos_candidato_aliababa:
    vencedor = 93

elif votos_candidato_aliababa > votos_candidato_alcapone:
    vencedor = 83

else:
    print("Empate!") 

print(votos_candidato_aliababa)
print(votos_candidato_alcapone)
print(votos_brancos)
print(votos_nulos)
print(vencedor)
print(f"{(100*votos_candidato_aliababa)/votos_total:.2f}")
print(f"{(100*votos_candidato_alcapone)/votos_total:.2f}")
