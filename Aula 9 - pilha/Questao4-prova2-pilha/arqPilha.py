class Pilha():
    def __init__(self):
        self.pilha1 = []
        self.pilha2 = []

    def getPilha1(self):
        return self.pilha1
    def getPilha2(self):
        return self.pilha2

    def setPilha1(self, elemento):
        self.pilha1.append(elemento)

    def copiarPilha(self):
        pilhaAuxiliar = []
        for i in self.pilha1[::-1]:
            # EMPILHAR ELEMENTOS DA PILHA 1 EM PILHAaUXULIAR
            pilhaAuxiliar.append(i)

        print("Pilha Auxiliar: ",pilhaAuxiliar)

        for j in pilhaAuxiliar[::-1]:
            # EMPILHAR ELEMENTO DA PILHA AUXILIAR EM PILHA 2
            self.pilha2.append(j)

        return self.getPilha2()