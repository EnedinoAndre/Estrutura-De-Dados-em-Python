class Node():
    def __init__(self):
        self.valor = None
        self.proximo = None

    def __str__(self):
        return str(self.valor)

    def getValor(self):
        return  self.valor

    def getProximo(self):
        return  self.proximo

    def setValor(self, novoValor):
        self.valor = novoValor

    def setProximo(self, novoProximo):
        self.proximo = novoProximo