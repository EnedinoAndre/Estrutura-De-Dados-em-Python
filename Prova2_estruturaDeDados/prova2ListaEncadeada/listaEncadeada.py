from node import Node
class Lista():
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def getCabeca(self):
        return self.cabeca

    def getCauda(self):
        return  self.cauda

    def setCabeca(self, tmp):
        self.cabeca = tmp

    def setCauda(self, tmp):
        self.cauda = tmp

    def inserirDado(self, dado):
        item = Node()
        item.setValor(dado)
        item.setProximo(None)

        if(self.cabeca == None and self.cauda == None):
            self.cabeca = item
        else:
            self.cauda.setProximo(item)

        self.cauda = item

    def printLista(self):
        node = self.cabeca
        while(node):
            print(node.getValor())
            node = node.getProximo()

    def juntar(self, lista1, lista2):
        lista3 = []

        item = lista1.cabeca

        while(item):
            lista3.append(item.valor)
            item = item.proximo

        item = lista2.cabeca

        while(item):
            lista3.append(item.valor)
            item = item.proximo

        return lista3



