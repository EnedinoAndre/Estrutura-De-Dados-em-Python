class Fila():
    def __init__(self):
        self.dados = []

    def inserirDados(self,newValue):
        self.dados.append(newValue)
        return self.dados
def main():

    filaVar = Fila()
    print(filaVar.inserirDados("André"))


main()