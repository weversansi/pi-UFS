
quantidade_livros = int(input())
quantidade_alunos = int(input())
media = quantidade_alunos//quantidade_livros

if media <= 8:
    conceito = "A"
elif media >= 9 and media <= 12 :
    conceito = "B"
elif media >= 13 and media <= 18:
    conceito = "C"
elif media > 18:
    conceito = "D"

print(conceito)