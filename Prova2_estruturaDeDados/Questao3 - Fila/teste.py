from filaNumeros import Fila

fila = Fila()

def main():
    fila = Fila()

    cont = 0
    decisao = True
    while(decisao):
        print("----------------------------------------------")
        opcao = input("Escolha uma Opção \nA - Adicionar: \nE - Excluir Negativos: \nS - Sair: ")

        if (opcao.upper() == "A"):
            print("----------------------------------------------")
            try:
                repeticao = int(input("Quantos números deseja por na lista??? "))
                for i in range(repeticao):
                    numero = int(input("Número: "))
                    fila.adicionarNumeros(numero)
                print("Números adicionados!!!")

            except(ValueError):
                print("Digite um valor válido!!!")

        if (opcao.upper() == "E"):
            print("----------------- Resultado -----------------------")

            if fila.numeros == []:
                print("A Fila está vazia")
            elif fila.retirarNumero() == 0:
                print("A fila não contem números negativos")
            else:
                fila.retirarNumero()
                print(fila.mostrarNumeros())

        if (opcao.upper() == "S"):
            decisao = False
main()