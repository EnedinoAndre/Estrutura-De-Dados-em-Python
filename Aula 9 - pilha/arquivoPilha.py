class Pilha():
    def __init__(self):
        self.ficha = [12,35,21,45,23]
    #MOSTRAR
    def mostrar(self):
        return self.ficha
    #INSERIR
    def inserir(self, novoElemento):
        self.ficha.append(novoElemento)
    #REMOVER
    def removerFicha(self):
        self.ficha.pop()
    #REMOVER POR ELEMENTO ESPECÍFICO
    def removerElementoEspecifico(self, elemento):
        for i in range(len(self.ficha)):
            if (elemento in self.ficha):
                self.removerFicha()
            else:
                break
    # DESCOBRIR ELEMENTO NO TOPO DA PILHA
    def elementoTopoPilha(self):
        return (self.ficha[len(self.ficha)-1])
    #ESVAZIAR FICHA
    def esvaziarPilha(self):
        for i in range(len(self.ficha)):
            self.ficha.pop()
        return self.ficha
