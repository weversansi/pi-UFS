
def EstacaoAno(num_dia, num_mes):
    
    if (num_dia >= 21 and num_mes >= 9) or (num_dia <= 20 and num_mes <= 12):
        return "PRIMAVERA"
    
    elif (num_dia >= 21 and num_mes >= 12) or (num_dia <= 20 and num_mes <= 3):
        return "VERAO"
    
    elif (num_dia >= 21 and num_mes >= 3) or (num_dia <= 20 and num_mes <= 6):
        return "OUTONO"
    
    elif (num_dia >= 21 and num_mes <= 6) or (num_dia <= 20 and num_mes <= 9):
        return "INVERNO"     


num_dia = int(input())
num_mes = int(input())

respo = EstacaoAno(num_dia, num_mes)

print(respo)