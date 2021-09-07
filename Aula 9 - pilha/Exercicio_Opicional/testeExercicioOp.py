from arqExercicioOpcional import Pilhas

def main():

    objPilhas = Pilhas()

    decisao = True
    while decisao:
        print("-------------------------------------------------")
        operacao = int(input("Onde deseja adicionar elemento: \n1 - Pilha 01"
                             "\n2 - Pilha 02: \n3 - Sair: "))
        if operacao == 1:
            objPilhas.inserirPilha01(int(input("Digite O Elemento: ")))
        if operacao == 2:
            objPilhas.inserirPilha02(int(input("Digite O Elemento: ")))
        if operacao == 3:
            decisao = False

        print(objPilhas.testarMaisElementos(objPilhas.pilha1,objPilhas.pilha2))

main()