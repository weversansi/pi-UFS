
M = int(input()) 
N = int(input())

if M > N:
    print(f"sem multiplos menores que {N}")
else:
    maior_multiplo = (N // M) * M
    print(maior_multiplo)