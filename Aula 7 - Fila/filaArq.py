
class Fila():
    def __init__(self):
        self.dados = ["RAMON","Altayr"]

    #MOSTRAR FILA
    def MostrarFila(self):
        return self.dados
    #INSERIR DADOS NA FILA
    def InserirDado(self, newValue):
    	self.dados.append(newValue)
        #self.dados.insert(len(self.dados),newValue)

    #RETIRAR DADO DA FILA
    def ApagarDado(self):
        self.dados.pop(0)

    #RETIRAR DADO ESPECÍFICO DA FILA
    def removerDadoEspecifico(self, valor):
        #Saber a posição do valor desejado
        posicao = self.dados.index(valor)
        #apagando dados de zero até valor valor desejado + 1
        for i in range(0,posicao+1):
            self.dados.pop(0)

    #MOSTRAR TAMANHO DA FILA
    def TamnhoFila(self):
        return len(self.dados)

def main():
    filaVar = Fila()

    filaVar.InserirDado("Leonardo")
    print(filaVar.MostrarFila())

    #filaVar.ApagarDado()
    #print(filaVar.MostrarFila())

    filaVar.removerDadoEspecifico("Altayr")
    print(filaVar.MostrarFila())

    print(filaVar.TamnhoFila())

main()

