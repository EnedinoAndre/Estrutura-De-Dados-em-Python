def main():

    matriz = [[{ },{ },{ }],
              [{ },{ },{ }],
              [{ },{ },{ }]]

    print("---------- JOGUINHO DA VELHA MAROTO -----------")
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):

            #CONTROLAR ERRO DE POSIÇÃO PREENCHIDA
            cont = 0
            while cont == 0:

                #ÍNDICE CORRETO
                try:
                    l = int(input("Escolha a linha: "))
                    c = int(input("Escolha a coluna: "))

                    #POSIÇÃO VAZIA
                    if matriz[l][c] == { }:
                        print("---------------------------")
                        valor = input("Escolha 'X' ou 'O': ")

                        #RECEBER X OU O
                        if valor.lower() =='x' or valor.lower() =='o':
                            matriz[l][c] = valor
                            # MOSTRAR O JOGO APÓS O JOGADOR ADICIONAR O VALOR
                            print("---------------------------")
                            print(matriz[0])
                            print(matriz[1])
                            print(matriz[2])
                            print("---------------------------")
                            cont += 1

                        #ERRO DE VALOR
                        else:
                            print("---------------------------")
                            print("Digite o valor pedido!!!")
                            print("---------------------------")

                    #ERRO DE POSIÇÃO PREENHIDA
                    else:
                        print("---------------------------")
                        print("Essa posição já está preenchida")
                        print("---------------------------")

                #ERRO DE ÍNDICE
                except IndexError:
                    print("---------------------------")
                    print("Digite o campo certo")
                    print("---------------------------")

    print("--------- OBRIGADO POR JOGAR -----------")

main()