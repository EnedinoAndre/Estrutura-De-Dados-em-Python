
def main():
    matriz = [ [2,3,0],
               [-1,-2,1] ]

    matrizT = []

    #PRIMEIRA COLUNA DA MATRIZ TRANSPOSTA
    for i in range(len(matriz)+1):
        linha = []
        for j in range(len(matriz)-1):
            linha.append(matriz[j][i])
        matrizT.append(linha)
    #SEGUNDA COLUNA DA MATRIZ TRANSPOSTA
    for i in range(len(matriz)+1):
        for j in range(len(matriz)-1):
            matrizT[i].append(matriz[j+1][i])

    print("---------------- Matriz Normal ------------------")
    for linha in range(len(matriz)):
        print(matriz[linha])

    print("-------------- Matriz Tranposta ----------------")
    for linha in range(len(matrizT)):
        print(matrizT[linha])

main()