from numpy import double

dicionario = {}
def cadastrar(chave,nome,divida,telefone,endereco):
    dicionario[chave] = [nome,divida,telefone,endereco]

def atualizar(nome,valor):
    for i in dicionario.values():
        if nome in i[0]:
            i[1] = i[1] - valor
            return i[1]

def buscaPorNome(nome):
    chave = 0
    cliente = {}
    for valor in dicionario.values():
        if nome in valor[0]:
            cliente[chave] = valor
            chave = chave + 1

    return cliente

def removerCliente():
    #LISTA DE CHAVES
    listaKeys = []
    #BUSCAR CHAVES COM DÍVIDA MENOR OU IGUAL A ZERO
    for item in dicionario.items():
        if(item[1][1] <= 0):
            #ADICIONAR CHAVES COM DÍVIDA <= ZERO DENTRO DA LISTA DE CHAVES
            listaKeys.append(item[0])

    #PERCORRER LISTA DE CHAVES
    for valor in listaKeys:
        #APAGANDO CHAVES DO DICIONÁRIO
        dicionario.pop(valor)

def mostrar():

    return  dicionario

def main():
    chave = 0

    menu = True

    while menu:
        print("------------------------ MENU ---------------------------")
        operacao = input("A - Cadastro de Cliente: \nB - Atualização de dívida: "
                             "\nC - Remoção de Cliente: \nD - Buscar Cliente: \nM - Mostrar Cadastros: "
                            "\nS - Sair: ")

        if operacao.upper() == "A":
            print("--------------------------------------------------")
            nome = input("Digite nome do Cliente: ")
            divida = double(input("Valor da dívida: "))
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")

            cadastrar(chave,nome,divida,telefone,endereco)
            chave = chave + 1

        if operacao.upper() == "B":
            print("--------------------------------------------------")
            nome = input("Nome do cliente para atualizar a dívida: ")
            valor = double(input("Valor a ser descontado: R$"))
            print("Dívida Atualizada: R$",atualizar(nome,valor))

        if operacao.upper() == "C":
            removerCliente()

        if operacao.upper() == "D":
            print("--------------------------------------------------")
            nome = input("Digite o nome que deseja buscar: ")

            busca = buscaPorNome(nome)
            if busca == {}:
                print("Esse Cliente não Existe")
            else:
                for valor in busca.values():
                    print("Nome: ",valor[0])
                    print("Dívida: R$", valor[1])
                    print("Telefone: ", valor[2])
                    print("Endereço: ", valor[3])

        if operacao.upper() == "M":
            clientes = mostrar()
            for valor in clientes.values():
                print("--------------------------------------------------")
                print("Nome: ", valor[0])
                print("Dívida: R$", valor[1])
                print("Telefone: ", valor[2])
                print("Endereço: ", valor[3])


        if operacao.upper() == "S":
            menu = False

main()