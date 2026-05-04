
def ClassificadoAluno(media, falta):

    if falta > 10:
        print("REPROVADO POR FALTAS")
        
    elif media < 7:
        print("REPROVADO")
        
    elif media >= 9.5:
        print("APROVADO COM LOUVOR")
        
    else:
        print("APROVADO")


media = float(input())
falta = int(input())

ClassificadoAluno(media, falta)