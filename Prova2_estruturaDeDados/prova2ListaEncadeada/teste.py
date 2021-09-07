from listaEncadeada import Lista

def main():

    lista1 = Lista()
    lista2 = Lista()
    lista3 = Lista()

    print("---------------------------------------------------")
    menu = True
    while(menu):
        try:
            opcao = int(input("Quantos Elementos deseja por na PRIMEIRA LISTA??? "))
            for i in range(0,opcao):
                dado = input("Digite o Elemento: ")
                lista1.inserirDado(dado)

            print("---------------------------------------------------")
            opcao = int(input("Quantos Elementos deseja por na SEGUNDA LISTA??? "))
            for i in range(0,opcao):
                dado2 = input("Digite o Elemento: ")
                lista2.inserirDado(dado2)

            menu = False
        except(ValueError):
            print("---------------------------------------------------")
            print("Digite um valor válido!!!")

    lista3 = lista3.juntar(lista1,lista2)
    print("----------------- Lista 3 --------------------")
    print(lista3)



main()