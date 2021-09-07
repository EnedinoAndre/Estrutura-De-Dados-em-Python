class Estacionamento():
    #CONSTRUTOR
    def __init__(self):
        self.estacionamento = []

    #ADICIONAR
    def adicionarCarro(self, carro):
        self.estacionamento.append(carro)

    #TIRAR DA FILA
    def retirar(self,placa):
        placaBoolean = False
        for i in self.estacionamento:
            if i == placa:
                pos = self.estacionamento.index(placa)
                
                for i in range(0,pos + 1):
                    self.adicionarCarro(self.estacionamento[0])
                    self.estacionamento.pop(0)
                self.estacionamento.pop()
                placaBoolean = True

        return placaBoolean

    #MOSTRAR
    def mostrarEstacionamento(self):
        return self.estacionamento

#EXECUTAR
def main():

    #OBJETO
    estacionamento_1 = Estacionamento()

    contador = 0
    while contador == 0:
        try:
            print("------- QUAL OPERAÇÃO DESEJA REALIZAR? --------")
            operacao = input("A - ADICIONAR CARRO NO ESTACIONAMENTO: \n"
                                "R - RETIRAR CARRO DO ESTACIONAMENTO: \n"
                                "S - MOSTRAR SITUAÇÃO DO ESTACIONAMENTO: \n"
                                "X - SAIR: ")

            #ADICIONAR
            if operacao.upper() == 'A':
                print("---------------- ADICIONAR -----------------")
                estacionamento_1.adicionarCarro(input("PLACA DO CARRO: "))
                print("--------------------------------------------")

            #RETIRAR
            elif operacao.upper() == 'R':
                print("----------------- RETIRAR ------------------")
                placa = input("DIGITE A PLACA DO CARRO: ")
                situacaoPlaca = estacionamento_1.retirar(placa)
                if situacaoPlaca == False:
                    print("O CARRO NÃO ESTÁ ESTACIONADO")
                elif situacaoPlaca == True:
                    print("O CARRO SAIU DO ESTACIONAMENTO")

                print("--------------------------------------------")

            #MOSTRAR ESTACIONAMENTO
            elif operacao.upper() == 'S':
                print("------------- ESTACIONAMENTO ---------------")
                situacao = estacionamento_1.mostrarEstacionamento()

                #VALIDAÇÃO DE ESTACIONAMENTO
                if situacao == []:
                    print("Estacionamento Está Vazio")
                else:
                    for i in range(len(situacao)):
                        print(i+1,"º Carro:",situacao[i])

                print("--------------------------------------------")

            #SAIR DO MENU
            elif operacao.upper() == 'X':
                print("----------------- OBRIGADO !!! ------------------")
                contador = 1

            #ERRO DE OPÇÃO
            else:
                print("------------ DIGITE UMA OPÇÃO CERTA --------------")

        #ERRO DE VALOR
        except ValueError:
            print("DIGITE UMA OPCÃO CORRETA")
main()
