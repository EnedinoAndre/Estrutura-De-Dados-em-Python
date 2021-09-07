from arqPilha import Pilha

def main():
    objeto1Pilha = Pilha()
    pilha2 = []

    menu = True
    while(menu):
        print("---------------------------------------------------")
        opcao = input("Escolha uma opção \n A - Adcionar Elementos: \n C - Copiar Elementos: \n S - Sair: ")

        if opcao.upper() == "A":
            try:
                print("---------------------------------------------------")
                quantidade = int(input("Quantos Elementos Deseja Empilhar: "))
                for i in range(quantidade):
                    elemento = input("Digite o elemento: ")
                    objeto1Pilha.setPilha1(elemento)
            except(ValueError):
                print("---------------------------------------------------")
                print("Digite um valor válido")

        if opcao.upper() == "C":
            print("---------------------------------------------------")
            print("Pilha 1: ",objeto1Pilha.getPilha1())
            pilha2 = objeto1Pilha.copiarPilha()
            print("Resultado pilha 2: ",pilha2)

        if opcao.upper() == "S":
            menu = False
main()