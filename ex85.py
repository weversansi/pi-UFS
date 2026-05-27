
qtde_elementos = int(input())
lista = []
lista_final = []
numeros = input().split()

while True:

    if qtde_elementos == len(numeros):
        for i in numeros:
            lista.append(int(i))

        break

    else:
        print("Erro:")
        print("Digite novamete: ")
        qtde_elementos = int(input())
        numeros = input().split()

    """ Laço While
    Este laço está sendo utilizado para verificar se a quantidade de elementos que o usuário escolheu está igual a 
    quantidade de elementos que foi digitado na lista

    """

for ii in lista:
    if ii not in lista_final:
        lista_final.append(ii)

    """ Laço for
    Este laço for está sendo utilizado para não conter elementos repetidos na lista
    """

#print(lista_final)
print("Menor valor: ",min(lista_final))
print("Posicao: ",lista_final.index(min(lista_final)))

