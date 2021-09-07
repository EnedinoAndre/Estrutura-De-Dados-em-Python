def main():
    print("-------------------- Exercício A -----------------------")
    '''
    matriz = [ ["Uniesp","João Pessoa"],["UFCG","Campina Grande"] ]
    print(matriz)
    '''

    print("-------------------- Exercício C -----------------------")
    '''
    matriz1 = [[39, 14, 27], [21, 83, 92], [31, 12, 43]]

    for linha in range(len(matriz1)):
        for coluna in range(len(matriz1[linha])):
            print("Linha:", linha,
                  "- Coluna:", coluna,
                  "- Resultado:", matriz1[linha][coluna] * 7)

    for linha in range(len(matriz1)):
        #print(matriz1[linha])
        matriz1[linha].pop(-1)
        print(matriz1[linha])
    '''

    print("-------------------- Exercício D -----------------------")
    '''
    matrizd = [[1,2,3,4],[5,6,7,8]]

    for linha in range(len(matrizd)):
        matrizd[linha].append(int(input("Digite um valor: ")))
    print(matrizd)
    '''

    print("-------------------- Exercício E -----------------------")
    '''
    matrizE = []
    cont = 0
    
    #Criar Matriz
    for i in range(4):
        linha = []
        for j in range(4):
            print("Linha",i,"Coluna:",j)
            print("----------------------------")
            linha.append(int(input("Digite um valor: ")))
            print("----------------------------")
        matrizE.append(linha)
        
    #Percorrer Matriz
    for linha in range(len(matrizE)):
        for coluna in range(len(matrizE[linha])):
            #Números dos Elementos maiores que 10
            if (matrizE[linha][coluna]) > 10:
                cont +=1
        print(matrizE[linha])

    print("----------------------------")
    print("Números Maiores que 10:",cont)
    '''

    print("-------------------- Exercício F -----------------------")
    matrizF = []

    for i in range(3):
        linha = []
        for j in range(3):
            if j == 0:
                linha.append(input("Digite seu nome: "))
            elif j == 1:
                linha.append(input("Digite matrícula: "))
            elif j == 2:
                linha.append(input("Digite a data de nascimento: "))
        matrizF.append(linha)
    print(matrizF)

main()