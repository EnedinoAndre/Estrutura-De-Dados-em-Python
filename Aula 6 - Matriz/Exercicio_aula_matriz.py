def main():
    matriz = [ [39,14,27], [21,83,92], [31,12,43] ]

    for linha in range (len(matriz)):
        for coluna in range (len(matriz[linha])):
            print("Linha:",linha,
                  "- Coluna:",coluna,
                  "- Resultado:",matriz[linha] [coluna] * 7 )

main()