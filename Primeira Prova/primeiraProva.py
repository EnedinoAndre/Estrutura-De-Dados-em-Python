
matriz = [  ["Caoa Chery","Carro A",60000,48],
            ["Capital Fiat","Carro B",80000,60],
            ["Mais","Carro C",50000,48],
            ["Monte Carlo Peugeot","Carro D",75000,60],
            ["Fiori","Carro E",36000,36],
            ["Tambaí","Carro F",48000,40],
            ["Cavalcante Primo","Carro G",77000,60],
            ["Promac","Carro H",150000,60]  ]

#CALCULAR MELHOR OFERTA
def CalculoMatriz(entrada):
    menor = 0
    melhor = []

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            parcela = (matriz[linha][2]) - entrada
            parcela = parcela / (matriz[linha][3])

            if linha == 0:
                menor = matriz[linha][2]
            else:
                if parcela < menor:
                    menor = parcela
                    melhor = matriz[linha]

    print("-------------- A melhor oferta -----------------")

    for linha in range(len(melhor)):
        if linha == 0:
            print("Concessionária:",melhor[linha])
        if linha == 1:
            print("Carro:",melhor[linha])
        if linha == 2:
            print("Valor: R$ %.2f"%melhor[linha])
        if linha == 3:
            print(melhor[linha],"Parcelas de: R$ %.2f"% menor)
            print("------------------------------------------------")

#ADICIONAR OFERTAS
def Adicionar(matriz1):
    matriz.append(matriz1)
    print("Oferta adicionada com sucesso!!!")

#MOSTRAR OFERTAS
def Mostrar():
    print("------------------------------------------------")
    for linha in range(len(matriz)):
        print(matriz[linha])
    print("------------------------------------------------")

#MÉTODO PRINCIPAL
def main():
    cont = 0
    while cont == 0:
        try:
            operacao = int(input("Qual operação deseja fazer?\n"
                                 "1 - Adicionar mais oferta:  \n"
                                 "2 - Simular: \n"
                                 "3 - Mostrar Ofertas: \n"
                                 "4 - Sair: "))
            #ADICIONAR OFERTA
            if operacao == 1:
                matriz = []
                print("------------------------------------------------")
                for linha in range(4):
                    if linha == 0:
                        matriz.append(input("Concessionária: "))
                    if linha == 1:
                        matriz.append(input("Modelo do Carro: "))
                    if linha == 2:
                        matriz.append(int(input("Valor R$: ")))
                    if linha == 3:
                        matriz.append(int(input("Quantidade de Parcelas: ")))
                Adicionar(matriz)
                print("------------------------------------------------")

            #CALCULAR
            if operacao == 2:
                entrada = int(input("Valor da Entrada R$: "))
                CalculoMatriz(entrada)

            #MOSTRAR
            if operacao == 3:
                Mostrar()

            #SAIR
            if operacao == 4:
                print("------------------------------------------------")
                print("Obrigado!!!")
                cont +=1

        except ValueError:
            print("Digite uma opcão válida")

main()