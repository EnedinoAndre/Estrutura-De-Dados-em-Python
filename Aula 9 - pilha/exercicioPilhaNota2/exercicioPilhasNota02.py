class Pilhas():
    def __init__(self):
        self.pilhaP = []
        self.pilhaAux = []

    def inverter(self,pilha):
        for i in range(len(self.pilhaP),0,-1):
            #TRANSFERIR ELEMNTOS DE PILHA P PARA PILHA AUX
            self.pilhaAux.append(i)
            #APAGAR ELEMENTOS DE PILHA P
            self.pilhaP.pop()

        for i in self.pilhaAux:
            #TRANSFERIR ELEMENTOS DE PILHA AUX PARA PILHA P
            self.pilhaP.append(i)

        #PILHA P
        return self.pilhaP

def main():
    objeto = Pilhas()

    pilha = [1,2,3,4,5]

    # INSERIR ELEMENTOS EM PILHA P
    objeto.pilhaP = pilha

    print(objeto.inverter(objeto.pilhaP))
main()