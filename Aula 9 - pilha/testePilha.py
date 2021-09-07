from arquivoPilha import Pilha

def main():
    pilha01 = Pilha()

    #MOSTRAR PILHA
    print(pilha01.mostrar())
    #INSERIR ELEMENTO
    pilha01.inserir(87)
    print(pilha01.mostrar())
    #REMOVER FICHA
    pilha01.removerFicha()
    print(pilha01.mostrar())
    #REMOVER POR ELEMENTO
    pilha01.removerElementoEspecifico(21)
    print(pilha01.mostrar())
    #DESCOBRIR ELEMENTO NO TOPO DA PILHA
    print(pilha01.elementoTopoPilha())
    #ESVAZIAR FICHA
    print(pilha01.esvaziarPilha())
main()