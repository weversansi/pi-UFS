def EstacaoAno(hemisferio, num_dia, num_mes):

    if hemisferio == 0:
        if (num_dia >= 21 and num_mes == 3) or (num_mes > 3 and num_mes < 6) or (num_dia <= 20 and num_mes == 6):
            return "PRIMAVERA"
        
        elif (num_dia >= 21 and num_mes == 6) or (num_mes > 6 and num_mes < 9) or (num_dia <= 20 and num_mes == 9):
            return "VERAO"
        
        elif (num_dia >= 21 and num_mes == 9) or (num_mes > 9 and num_mes < 12) or (num_dia <= 20 and num_mes == 12):
            return "OUTONO"
        
        else:
            return "INVERNO"

    elif hemisferio == 1:
        if (num_dia >= 21 and num_mes == 9) or (num_mes > 9 and num_mes < 12) or (num_dia <= 20 and num_mes == 12):
            return "PRIMAVERA"
        
        elif (num_dia >= 21 and num_mes == 12) or (num_mes == 1 or num_mes == 2) or (num_dia <= 20 and num_mes == 3):
            return "VERAO"
        
        elif (num_dia >= 21 and num_mes == 3) or (num_mes > 3 and num_mes < 6) or (num_dia <= 20 and num_mes == 6):
            return "OUTONO"
        
        else:
            return "INVERNO"


hemisferio = int(input())
num_dia = int(input())
num_mes = int(input())

respo = EstacaoAno(hemisferio, num_dia, num_mes)
print(respo)