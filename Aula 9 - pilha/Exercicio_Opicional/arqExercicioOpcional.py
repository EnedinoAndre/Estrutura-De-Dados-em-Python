class Pilhas():
    def __init__(self):
        self.pilha1 = [23,45,67,87]
        self.pilha2 = [1,2,3,4,5]

    def inserirPilha01(self,elemento):
        self.pilha1.append(elemento)
    def inserirPilha02(self,elemento):
        self.pilha2.append(elemento)

    def testarMaisElementos(self,pilha1,pilha2):
        if (len(self.pilha1) > len(self.pilha2)):
            return True
        else:
            return False