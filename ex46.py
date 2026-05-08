
nota1, nota2, nota3, nota4 = map(float, input().split())

def AnalisarSituacao(*,nota1, nota2, nota3, nota4):

    media_ponderada = ((nota1*1) + (nota2*2) + (nota3*3) + (nota4*4))/10

    if media_ponderada >= 9:
        return "aprovado com louvor"
    
    elif media_ponderada >= 7:
        return "aprovado"
    
    elif media_ponderada >= 3 and media_ponderada < 7:
        return "prova final"
    
    else:
        return "reprovado"
    
print(AnalisarSituacao(nota1=nota1, nota2=nota2, nota3=nota3, nota4=nota4))