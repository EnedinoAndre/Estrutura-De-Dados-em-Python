from numpy import double

dicionario = {}
def cadastrar(chave,nome,divida,telefone,endereco):
    dicionario[chave] = [nome,divida,telefone,endereco]

def atualizar(nome,valor):
    for item in dicionario.items():
        if nome in item[1][0]:
            item[1][1] = item[1][1] - valor
            return item[1][1]

def buscaPorNome(nome):
    chave = 0
    cliente = {}
    for valor in dicionario.values():
        if nome in valor[0]:
            cliente[chave] = valor
            chave = chave + 1

    return cliente

def removerCliente():
    for item in dicionario.items():
        if (item[1][1] <= 0):
            dicionario.pop(item[0])

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
            valor = double(input("Valor a ser descontado: "))
            print("Dívida Atualizada: R$",atualizar(nome,valor))

        if operacao.upper() == "C":
            removerCliente()

        if operacao.upper() == "D":
            print("--------------------------------------------------")
            nome = input("Digite o nome que deseja buscar: ")

            busca = buscaPorNome(nome)
            for valor in busca.values():
                print(valor)

        if operacao.upper() == "M":
            clientes = mostrar()
            for valor in clientes.values():
                print(valor)

        if operacao.upper() == "S":
            menu = False

main()