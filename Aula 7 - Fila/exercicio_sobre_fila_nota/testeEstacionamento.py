from exercicio_sobre_fila_nota.filaCarro import Estacionamento

def main():
    estacionamento_1 = Estacionamento()

    contador = 0
    while contador == 0:
        operacao = int(input("1 - ADICIONAR CARRO NO ESTACIONAMENTO \n"
                             "2 - RETIRAR CARRO DO ESTACIONAMENTO \n"
                             "3 - MOSTRAR SITUAÇÃO DO ESTACIONAMENTO \n"
                             "4 - SAIR \n"))
        print("--------------------------------------------")

        if operacao == 1:
            estacionamento_1.adicionarCarro(input("PLACA DO CARRO: "))
            print("--------- CARRO ADICIONADO COM SUCESSO !!! ----------")

        elif operacao == 2:
            estacionamento_1.retirarCarro(input("DIGITE A PLACA DO CARRO: "))
            print("--------- CARRO RETIRADO!!! ----------")

        elif operacao == 3:
            situacao = estacionamento_1.mostrarEstacionamento()
            if situacao == []:
                print("Estacionamento Está Vazio")
            else:
                for i in range(len(situacao)):
                    print(i+1,"º Carro:",situacao[i])

            print("--------------------------------------------")

        elif operacao == 4:
            print("----------------- OBRIGADO !!! ------------------")
            contador = 1
main()


