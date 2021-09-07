nomess = []
datas_nascimento = []
def Cadastrar(nome,data):
    nomess.append(nome)
    datas_nascimento.append(data)
    return nomess, datas_nascimento

def Listar():
    #Mostrando índices e valores dos arrays
    for indice, valor in enumerate(nomess):
        print(indice,valor)
    for indice,valor in enumerate(datas_nascimento):
        print(indice,valor)

def Remover():
    cont = 0
    while cont == 0:
        opcao = int(input("Deseja Remover por nome ou posição: \n1 - Nome: \n2 - Posição: "))

        if opcao == 1:
            nome1 = input("Qual nome deseja remover: ")

            for indice, valor in enumerate(nomess):
                if valor == nome1:
                    nomess.remove(valor)
                    datas_nascimento.pop(indice)
                    cont = 1

        elif opcao == 2:
            posicao = int(input("Qual posição deseja remover: "))

            for indice, valor in enumerate(nomess):
                nomess.pop(posicao)
                datas_nascimento.pop(posicao)
                cont = 1
        else:
            print("Digite um valor válido")

def main():
    cont1 = 0
    while cont1 == 0:

        try:
            operacao = int(input("O que deseja fazer?\n1 - Cadastrar \n2 - Apagar \n3 - Listar \n4 - Sair"))

            #CADASTRAR
            if operacao == 1:

                cont = 0
                while cont == 0:

                    try:
                        cadastros = int(input("Quantos cadastros você quer fazer: "))

                        i = 0
                        while i < cadastros:
                            nome = input("Digite o nome: ")
                            data_nasci = input("Data de Nascimento (Use '/' para separar): ")
                            Cadastrar(nome, data_nasci)
                            i = i + 1
                        cont = 1

                    except ValueError:
                        print("Digite um valor pedido")

            #APAGAR
            elif operacao == 2:
                Remover()

            #LISTAR
            elif operacao == 3:
                Listar()

            #SAIR
            elif operacao == 4:
                print("Obrigado!")
                cont1 = 1

        except ValueError:
            print("Digite uma opção válida")

main()