def EstacaoAno(hemisferio,num_dia, num_mes):
    
    
    if (num_mes == 9 and num_dia >= 21) or (num_mes > 9 and num_mes < 12) or (num_mes == 12 and num_dia <= 20):
        return "PRIMAVERA"
    
    elif (num_mes == 12 and num_dia >= 21) or (num_mes >= 1 and num_mes < 3) or (num_mes == 3 and num_dia <= 20):
        return "VERAO"
    
    elif (num_mes == 3 and num_dia >= 21) or (num_mes > 3 and num_mes < 6) or (num_mes == 6 and num_dia <= 20):
        return "OUTONO"
    
    elif (num_mes == 6 and num_dia >= 21) or (num_mes > 6 and num_mes < 9) or (num_mes == 9 and num_dia <= 20):
        return "INVERNO"


num_dia = int(input())
num_mes = int(input())
hemisferio = int(input())
respo = EstacaoAno(num_dia = num_dia, num_mes = num_mes, hemisferio = hemisferio)

print(respo)