def main():
    '''
    matriz = [ [1, 2, 3, 4],
               [5, 6, 7, 8] ]
    # Mostrando o índice da matriz
    print(matriz[0])
    print(matriz[1])
    print(len(matriz))

    #Acessando linha 1 coluna 1
    print(matriz[1][1])

    '''

    a = [ [1,2,3,4], [5,6], [7,8,9] ]

    '''
    #Percorrendo os índices
    for linha in range(len(a)):
        print(linha)
    '''

    '''
    #Mostrando cada elemento da matriz
    for elemento in a:
        print(elemento)
    '''

    '''
    # Percorrer linhas e colunas
    for linha in range(len(a)):
        for coluna in range(len(a[linha])):
            print(a[linha][coluna])
        print("--------")
    '''
    '''
    #Outra forma de percorrer cada elemento
    for linha in a:
        print(linha)
        for elemento in linha:
            print(elemento)
        print("Saida do loop interno")
    print("Final do for")
    '''

    matriz = [ ["Ana", "123131443"],
               ["Francisco", "32141241"],
               ["João", "9474945"] ]
    print(matriz)
    print("------------------------------------------------------")
    #Remoção
    for i in range(0, len(matriz)):
        if "Francisco" in matriz[i]:
            matriz[i].remove("Francisco")

    #APPEND
    matriz.append(["Ana Paula"])
    #Inserindo matricula em ana paula
    matriz[-1].append("12345")

    #INSERT
    matriz.insert(0,["Ramon","7685490"])

    print(matriz)

main()


